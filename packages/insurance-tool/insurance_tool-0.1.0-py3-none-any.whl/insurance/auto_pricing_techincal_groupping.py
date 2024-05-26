# Semi- Automated Technical Grouping for pricing

# Next: change_to_group(semi done) it now returns the change in group_name
# But not sure how to go from here
# 'Upper' means I need to split more group(it's higher than the current groupping that I have)
# 'Lower' means I need to split more group(it's lower than the current groupping that I have)
#  need to verify that this is the correct logic first


# update_groupping

# make_group_name: done

# total: > 14.5 hrs


# before Feb,26, 24: >3.5  hrs 
# Feb 26,24: +6 hrs
# Mar 31,24: +5 hrs

# v01 => Grouuping,
#   init_grouping: Done
# v02 => make_group_make: in progress
# v03 => change_to_group: already produce the suggested groupping
#   but need to verify and think about how to use this info
# v04 => seems to work but need more testing
# v05 => saved_name


# Addtional feature01
# 01) create a function in Groupping called input_groupping => to allow the direct input of groupping instead of finding by itself
# 02) in sns.plot can we add the level name


import pandas as pd
import seaborn as sns
import sys
from dataclasses import dataclass, field
from typing import Literal, Union, List, Optional
import logging
import time
from pathlib import Path
# sys.path.append(r"C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\03 Modeling")
# import lib03_modeling as ml

sys.path.append(r"C:\Users\n1603499\OneDrive - Liberty Mutual\Documents\19 MyPythonLibrary\03 Modeling")
import Clustering as ml
import pydantic
from pydantic import PositiveFloat, BaseModel

@dataclass
class Groupping:
    from pathlib import Path
    df_weight: pd.DataFrame
    saved_name: str
    saved_folder: Union[str,Path] = field(default="")
    diff_rela_good: float = field(default=0.05)
    history_table: list[pd.DataFrame] = field(default_factory=list)
    # input 2d list of Observed Avg & Fitted Avg
    """
    saved_name is the name of object saved
    """

    def __post_init__(self) -> None:
        from pathlib import Path
        self.variable_name = self.df_weight.columns[0]
        self.df_weight['weight_rank'] = self.df_weight['weight'].rank(ascending=False)
        self.variable_name = self.df_weight.columns[0]
        self.saved_name = self.saved_name if ".pickle" in self.saved_name else self.saved_name + ".pickle"

        self.saved_path = Path(self.saved_folder) / self.saved_name

        self.group_info_history = list()
        self.only_1_level_history = list()
        self.highest_level_history = list()
        self.lowest_level_history = list()
        self.n_groups_history = dict()
        
    def init_group_by_base_level_avg(
            self,
            modeling: Union[None, list[float]] = None,
            validation: Union[None, list[float]] = None,
            limit_group_name: int = 3,
            group_prefix_name:str = "G",
            group_start_inx: int = 1,
            ):
        """
        initialize groupping from base level averge(reletivity)

        modeling & validation can't be None at the same time

        save: latest_group_index, latest_group, history_table,group_prefix_name
        """
        

        base_level_info = pd.DataFrame(
            {
            'modeling_base_level_avg': modeling ,  
            'valid_base_level_avg': validation,
            }

        )
        base_level_info[self.variable_name] = self.df_weight.iloc[:,0]
        group_name = group_prefix_name + str(group_start_inx)
        self.latest_group_index = group_start_inx
        self.latest_group = group_name

        group_name_df = base_level_info[[self.variable_name]]
        group_name_df[group_name] = base_level_info['modeling_base_level_avg'].rank(method='dense')
        self.make_group_name(group_name_df,base_level_info,limit_group_name)
        
        # it would have no history_table
        self.history_table.append(group_name_df)
        self.group_prefix_name = group_prefix_name
        self.limit_group_name = limit_group_name
        print('From init_group_by_base_level_avg')

        
    def init_grouping(self,
            modeling: List[List[PositiveFloat]],
            validation: List[List[PositiveFloat]],
            group_prefix_name:str = "G",
            group_start_inx: int = 1,
            limit_group_name = 3
                     ) -> None:
        # append history_table,
        #  append via self.make_group_name
            #  append group_info_history, only_1_level_history, n_groups_history

        # save:  group_prefix_name, latest_group_index, latest_group, limit_group_name
        self.group_prefix_name = group_prefix_name
        variable_name = self.df_weight.columns[0]
        group_name = group_prefix_name + str(group_start_inx)

        to_adj_rela = self.model_valid_diff(modeling,validation)
        
        # over_predict: to_adj_avg_group
        # under_predict: group(I want to keep it seperate)
        over_predict = to_adj_rela.loc[to_adj_rela['curr_adj'] == 'Decrease']
        under_predict = to_adj_rela.loc[to_adj_rela['curr_adj'] == 'Increase']

        title = f"{group_name} Groupping"

        
        over_predict = ml.auto_cluster(over_predict, col_name='to_adj_avg',graph_title = f'{title} for over predicted levels')
        under_predict = ml.auto_cluster(under_predict, col_name='to_adj_avg',graph_title = f'{title} for under predicted levels')

        n_group_over_predict = over_predict['to_adj_avg_group'].max()
        over_predict = over_predict.rename(columns = {'to_adj_avg_group': group_name})
        under_predict[group_name] = under_predict['to_adj_avg_group'] + n_group_over_predict + 1
        under_predict = under_predict.drop(columns = ['to_adj_avg_group'])

        total_group = pd.concat([over_predict,under_predict])
        
        to_adj_rela = df_XLookup(to_adj_rela,total_group,variable_name,variable_name,group_name)
        to_adj_rela[group_name] = to_adj_rela[group_name].fillna(n_group_over_predict + 1)
        to_adj_rela[group_name] = to_adj_rela[group_name].astype('int')
# base_level_info contains the current relativity information
        base_level_info = self.get_base_level_info(modeling,validation)


        self.history_table.append(to_adj_rela) 
        self.latest_group_index = group_start_inx
        self.latest_group = group_name
        self.limit_group_name = limit_group_name
        group_info = self.make_group_name(to_adj_rela,base_level_info,limit_group_name)


        print('From init_grouping')
    
    def increment_group(self):
        self.previous_group = self.latest_group
        self.latest_group_index += 1
        self.latest_group = self.group_prefix_name + str(self.latest_group_index)
        
        
    def update_groupping(
            self,
            modeling: List[List[PositiveFloat]],
            validation: List[List[PositiveFloat]]
                     ) -> None:
        # modify: latest_group
        # save:
        # append 

        
        prev_group_info = self.history_table[-1]
        curr_group_info = prev_group_info.copy()
        curr_group_info = curr_group_info[[self.variable_name,self.latest_group]]
        self.increment_group()
        curr_group_name = self.latest_group

        modeling_base_level_avg = []
        valid_base_level_avg = []

        for row in modeling:
            _, _, curr_relativity = row
            modeling_base_level_avg.append(curr_relativity)
        
        for row in validation:
            _, _, curr_relativity = row
            valid_base_level_avg.append(curr_relativity)

        to_adj_avg = self.model_valid_diff(modeling,validation,diff_rela_good= self.diff_rela_good)
        # get the group information
        to_adj_avg = df_XLookup(
                        to_adj_avg,
                        df_lookup=curr_group_info,
                        lookup_col= self.variable_name,
                        key_col= self.variable_name,
                        return_col= self.previous_group,
                        )
        
        base_level_avg_df = self.get_base_level_info(modeling,validation)
        # base_level_avg_df = pd.DataFrame({
        #     'modeling_base_level_avg': modeling_base_level_avg,
        #     'valid_base_level_avg': valid_base_level_avg
        #     })
        
        # base_level_avg_df[variable_name] = self.df_weight.iloc[:,0]
#  to decide which group it should belong to
# we have to set every relativity/ current_rela
# then we would find the closest from avg_rela and choose to go with that group
        to_adj_avg[curr_group_name + "_scratch"] = to_adj_avg.apply(
                lambda row:self.change_to_group(
                    row[self.variable_name],
                    row['curr_adj'],
                    base_level_avg_df,
                    row['to_adj_avg'],
                    row[self.previous_group]
                    ),
                axis = 1
                
                )
        to_adj_avg[curr_group_name] = to_adj_avg[curr_group_name + "_scratch"].rank(method = 'dense')
        # copy to clipboard
        to_adj_avg.to_clipboard()
        # insert time.sleep to allow mutiple copies in the clipboard
        # https://stackoverflow.com/questions/67092159/copy-multiple-items-to-clipboard-in-python
        time.sleep(1)
        to_adj_avg[curr_group_name].to_clipboard()

        self.history_table.append(to_adj_avg) 
        group_name_df = self.make_group_name(to_adj_avg,base_level_avg_df)
        group_name_df.to_clipboard()
        self.saved_to_pickle()
        print('From update_groupping')
    
    def change_to_group(
            self,
            level_name:str,
            adj: Literal['Increase','Decrease','Only','Inconsistent'],
            base_level_avg_df: pd.DataFrame, 
            to_adj_avg: pd.DataFrame,
            current_group: Union[int,None],
            use_avg: Literal['both','modeling','validation'] = 'both'
                        ):
        """ 
        this function tries to evaluate which groupping it should belong to
        based on the input information 
        """
        # use_avg would decide which data of relativity it would be based on
        variable_name = self.df_weight.columns[0]
        modeling_base = base_level_avg_df.loc[base_level_avg_df[variable_name] == level_name, 'modeling_base_level_avg'].values[0]
        valid_base = base_level_avg_df.loc[base_level_avg_df[variable_name] == level_name, 'valid_base_level_avg'].values[0]
        # get the previous groupping from history_table
        if self.history_table[-1] is not None:
            # if len(history_table.columns) > 2 when init_group_by_base_level_avg which has no previous_group
            
            # if len(self.history_table[-1].columns) > 2:
            #     chosen_group = self.previous_group
            # else:
            chosen_group = self.previous_group

            curr_group = self.history_table[-1][[variable_name, chosen_group]]
# it would be None if I initialize with init_group_by_base_level_avg


        rebase_compute = base_level_avg_df.copy()

        if adj in ['Inconsistent']:
            print(f"no change level '{level_name}': because it's {adj}")
            return current_group
        elif adj in ['Only']:
            print(f"no change level '{level_name}': because this level already contained 1 element.")
            return current_group
        elif adj in ['Good']:
            print(f"no change level '{level_name}': because this level already good.")
            return current_group
        
        if self.history_table[-1] is not None:
            rebase_compute = rebase_compute.merge(curr_group, on = variable_name)
        # create 2 new cols: modeling_rebase,valid_rebase
        rebase_compute['modeling_rebase'] = rebase_compute['modeling_base_level_avg'] / modeling_base
        rebase_compute['valid_rebase'] = rebase_compute['valid_base_level_avg'] / valid_base
        rebase_compute['rebase_avg'] = (rebase_compute['modeling_rebase'] + rebase_compute['valid_rebase']) / 2

        if use_avg in ['both']:
            rebase_compute['select_rebase'] = rebase_compute['rebase_avg'] 
        elif use_avg in ['modeling']:
            rebase_compute['select_rebase'] = rebase_compute['modeling_rebase'] 
        elif use_avg in ['validation']:
            rebase_compute['select_rebase'] = rebase_compute['modeling_rebase'] 
        else:
            raise ValueError("Invalid use_avg: Only ['both','modeling','validation'] is allowed ")
        

        if adj in ['Decrease']:
            rebase_filter = rebase_compute.loc[rebase_compute['select_rebase'] < 1]
            row_pick = df_closest_value(rebase_filter,'select_rebase',to_adj_avg)
        elif adj in ['Increase']:
            rebase_filter = rebase_compute.loc[rebase_compute['select_rebase'] > 1]
            row_pick = df_closest_value(rebase_compute,'select_rebase',to_adj_avg)

    # still have no condition to split the group in between
    # only allow the upper and lower group to split

        if len(row_pick) > 0:
            to_level_name = row_pick[chosen_group]
            closest_rela = row_pick['select_rebase']
        # if len(row_pick) == 0 when it's already the highest or lowest level
        #  I can use this condition instead of finding which is already the higest
        else:
            # the upper and lower group is named 'Upper' and 'Lower' for now
            if adj in ['Decrease']:
                to_level_name = current_group - 1
            elif adj in ['Increase']:
                to_level_name = current_group +1


        
        # print('From change_to_group')
        return to_level_name



    
    def make_group_name(self, input_df: pd.DataFrame,
                        base_level_avg : pd.DataFrame,
                        limit_group_name: int = 3,
                        ) -> pd.DataFrame:
        """
        what's the input_df???
        """
        #  append group_info_history, only_1_level_history, n_groups_history
        # 
        if True:
        # if len(self.group_info_history) == 0:

            variable_name = self.df_weight.columns[0]
            group_name = self.latest_group
            groupping = input_df[[variable_name,group_name]]
            groupping[group_name] = groupping[group_name].astype('int')
            # groupping.loc[:, group_name] = groupping[group_name].astype('int')
            groupping = groupping.merge(self.df_weight, on = variable_name, how='left')
            groupping = groupping.merge(base_level_avg, on = variable_name, how='left')
            groupping.to_clipboard()
            n_groups = groupping[group_name].max()
            groupping.loc[:, group_name] = groupping[group_name].astype('int')
            value_count_df = pd.DataFrame(groupping[group_name].value_counts()).reset_index()
    
            element_df = groupping.groupby(group_name)[[
                variable_name,'weight','weight_rank','modeling_base_level_avg','valid_base_level_avg']].agg(
                {
                    variable_name: list,
                    'weight': sum,
                    'weight_rank': list,
                    'modeling_base_level_avg': 'mean',
                    'valid_base_level_avg': 'mean'
                }).reset_index()
            
            element_df = pd.merge(element_df, value_count_df, on=group_name, how='left')
            element_df = element_df.rename(columns = {variable_name: 'elements', 
                                                      'weight': 'sum_weight',
                                                      'count':'n_elements'
                                                      })
            element_df = swap_columns(element_df, 'n_elements', 'elements')
            # Group by index and aggregate matching group names into lists
    
            # if count == 1 then and (Only) to the level
            # if count <= limit_group_name use the full name
            # else use the higest weight + '+'
    
            element_df['level_name'] = element_df.apply(
                lambda row: self._make_group_text(row['elements'], row['weight_rank'],limit_group_name  ),
                
                axis=1)
            element_df = swap_columns(element_df, 'level_name', 'weight_rank')
            # get the index of levels that has only 1 element
            only_1_level_group_idx = element_df.loc[element_df['n_elements'] == 1,group_name].tolist()
            # get the name of levels that has only 1 element
            only_1_level_group = groupping.loc[groupping[group_name].isin(only_1_level_group_idx), variable_name].tolist()

            self.group_info_history.append(element_df)
            self.only_1_level_history.append(only_1_level_group)
            self.n_groups_history[group_name] = n_groups
            return element_df
        else:
            pass      # helper_df is used to decide which group it should go to 
        
        logging.debug('From make_group_name')
    
    def _make_group_text(self, elements, weight_rank, limit_group_name):
        # has to be rank not the actual weights
        element_weights = list(zip(elements,weight_rank))
        element_weights.sort(key = lambda x: x[1], reverse=False)
        higest_w_element = element_weights[0][0]
        
        elements_sorted, _ = zip(*element_weights)
        elements_sorted = list(elements_sorted)
        if len(elements) > limit_group_name:
            level_name = f'{higest_w_element} +'
        elif len(elements) == 1:
            level_name = f'{higest_w_element}(Only)'
        else:
            level_name_temp = ', '.join(elements_sorted)
            level_name = replace_last(level_name_temp,", ", " &") 
        print(f'From _make_group_text: level_name is: {level_name}')
        return level_name

    def get_base_level_info(self,
                         modeling: List[List[PositiveFloat]],
                         validation: List[List[PositiveFloat]]):
        variable_name = self.df_weight.columns[0]
        modeling_base_level_avg = []
        valid_base_level_avg = []
        for row in modeling:
            obs, predict, base_level_avg = row
            modeling_base_level_avg.append(base_level_avg)
        
        for row in validation:
            obs, predict, base_level_avg = row
            valid_base_level_avg.append(base_level_avg)


        base_level_avg = pd.DataFrame({'modeling_base_level_avg': modeling_base_level_avg,
                            'valid_base_level_avg': valid_base_level_avg
                            })
        
        # add level name to base_level_avg
        base_level_avg[variable_name] = self.df_weight.iloc[:,0]

        return base_level_avg


    def model_valid_diff(self,
                         modeling: List[List[PositiveFloat]],
                         validation: List[List[PositiveFloat]],
                         diff_rela_good = 0.05
                         ):
        """ 
        diff_rela_good is the range of accepting current relativity as 'Good'
        if it's 0.05 then it would consider 0.95 - 1.05 consistent change as 'Good'
        """
        # calculate column ['Decrease','Increase','Inconsistent']
        # We want to add 'Only' in the to_adj_info columns 'adj'
        
        variable_name = self.df_weight.columns[0]
        modeling_adjustment = []
        #  valid = validation
        valid_adjustment = []

        modeling_relativity = []
        valid_relativity = []
        for row in modeling:
            obs, predict, curr_relativity = row
            relativity_diff = obs / predict
            modeling_adjustment.append(relativity_diff)
            modeling_relativity.append(curr_relativity)
        
        for row in validation:
            obs, predict, curr_relativity = row
            relativity_diff = obs / predict
            valid_adjustment.append(relativity_diff)
            valid_relativity.append(curr_relativity)

        
        to_adj_rela = pd.DataFrame({'to_adj_modeling': modeling_adjustment,
                                    'to_adj_valid': valid_adjustment
                                    })
        
        to_adj_rela[variable_name] = self.df_weight.iloc[:,0]

        to_adj_rela['to_adj_avg'] = (to_adj_rela['to_adj_modeling'] + to_adj_rela['to_adj_valid']) /2
        
        # created new col: curr_adj
        to_adj_rela['curr_adj'] = 'Inconsistent'

        # Conditions for 'Increase' or 'Decrease', with additional check for 'Good'
        to_adj_rela.loc[(to_adj_rela['to_adj_modeling'] > 1) &
                        (to_adj_rela['to_adj_valid'] > 1) &
                        (to_adj_rela['to_adj_modeling'] >= 1 + diff_rela_good), 'curr_adj'] = 'Increase'

        to_adj_rela.loc[(to_adj_rela['to_adj_modeling'] < 1) &
                        (to_adj_rela['to_adj_valid'] < 1) &
                        (to_adj_rela['to_adj_valid'] <= 1 - diff_rela_good), 'curr_adj'] = 'Decrease'

        # Additional conditions for setting 'Good'
        to_adj_rela.loc[(to_adj_rela['to_adj_modeling'] > 1) &
                        (to_adj_rela['to_adj_valid'] > 1) &
                        (to_adj_rela['to_adj_modeling'] < 1 + diff_rela_good) & 
                        (to_adj_rela['to_adj_valid'] < 1 + diff_rela_good)

                        , 'curr_adj'] = 'Good'

        to_adj_rela.loc[(to_adj_rela['to_adj_modeling'] < 1) &
                        (to_adj_rela['to_adj_valid'] < 1) &
                        (to_adj_rela['to_adj_modeling'] > 1 - diff_rela_good) &
                        (to_adj_rela['to_adj_valid'] > 1 - diff_rela_good)
                        
                        , 'curr_adj'] = 'Good'

        if len(self.group_info_history) > 0:
        #  if we declare using init_group_by_base_level_avg
        #  it would have no history_table
            
            group_info = self.group_info_history[-1]
            history_table = self.history_table[-1]
            only_1_level_group = self.only_1_level_history[-1]

            if history_table is not None:
                # if len(history_table.columns) == 2 when use init_group_by_base_level_avg
                # when use init_group_by_base_level_avg it would have no prior adj
                if len(history_table.columns) > 2:
                    to_adj_rela['previous_adj'] = history_table['curr_adj']
            # create new col: only_1_in_group helper column to help change curr_adj to 'Only'
            to_adj_rela['only_1_in_group'] = False
            to_adj_rela.loc[(to_adj_rela[variable_name].isin(only_1_level_group)), 'only_1_in_group'] = True
            
            # to_adj_rela.loc[(to_adj_rela['only_1_in_group']), 'curr_adj'] = 'Only'
            
        print()
        return to_adj_rela
    
    def saved_to_pickle(self):
        import pickle
        with open(self.saved_path, "wb") as file:
            pickle.dump(self, file)
    
    # @property
    # def saved_name(self):
    #     return self.saved_name

    # @saved_name.setter
    # def saved_name(self, new_saved_name):
    #     # this import seems to cause some issue of not continuing the code
    #     # from pathlib import Path
    #     self.saved_name = new_saved_name
    #     self.saved_path = Path(self.saved_folder) / self.saved_name
        
    # class Config:
    #     arbitrary_types_allowed = True
            
def _get_base_level_avg(lst: List[List[float]]):
    result = []
    for row in lst:
        _,_,base_avg = result.append(base_avg)
    return result

# ################################### Helper functions ########################
def replace_last(s: str, oldvalue, newvalue):
    last_comma_index = s.rfind(oldvalue)
    if last_comma_index != -1:
        s = s[:last_comma_index] + newvalue + s[last_comma_index + 1:]
    return s

def swap_columns(df, col1, col2):
    """Swap two columns in a DataFrame."""
    column_list = list(df.columns)
    col1_index, col2_index = column_list.index(col1), column_list.index(col2)
    
    # Swap the positions in the column list
    column_list[col2_index], column_list[col1_index] = column_list[col1_index], column_list[col2_index]
    
    # Reorder the DataFrame according to the new column list
    return df[column_list]

    

def py_to_2d_list(text: str) -> List[List[float]]:
    # Split the input text by commas and convert each value to a float
    rows = text.split("], [")
    out_list = []
    for row in rows:
        row_values = [float(val) for val in row.strip("[]").split(", ")]
        out_list.append(row_values)
    return out_list

def df_XLookup(df_main, df_lookup, lookup_col, key_col, return_col, inplace=True):
    """
    Perform an XLOOKUP-like operation on DataFrames.

    Parameters:
        df_main (pd.DataFrame): Main DataFrame.
        df_lookup (pd.DataFrame): Lookup DataFrame.
        lookup_col (str or list[str]): Column(s) in df_main to use for lookup.
        key_col (str): Column in df_lookup to match with lookup_col.
        return_col (str or list[str]): Column(s) in df_lookup to return.
        inplace (bool, optional): If True, modifies df_main in-place. Otherwise, returns a new DataFrame. Default is True.

    Returns:
        pd.DataFrame: Modified df_main if inplace=True, otherwise a new DataFrame.
    """
    # Ensure lookup_col is a list
    if not isinstance(lookup_col, list):
        lookup_col = [lookup_col]

    # Merge DataFrames
    merged_df = pd.merge(df_main, df_lookup, left_on=lookup_col, right_on=key_col, how='left')

    # Keep only the specified return columns
    if isinstance(return_col, str):
        return_col = [return_col]  # Convert single column name to list

    if inplace:
        for col in return_col:
            df_main[col] = merged_df[col]
        return df_main
    else:
        return merged_df[return_col]

def df_closest_upper_value(df: pd.DataFrame, col: str, lookup_value: float) -> pd.Series:
    """
    Find the row in a DataFrame where the value in a specified column
    is closest but strictly higher than a given lookup value.
    
    Parameters:
    - df : pd.DataFrame
        The DataFrame to search.
    - col : str
        The name of the column in the DataFrame to compare against the lookup_value.
    - lookup_value : float
        The value to find the closest upper match for in the specified column.
        
    Returns:
    - pd.Series
        A pandas Series object representing the row in the DataFrame where
        the column's value is closest but strictly higher than the lookup_value.
        If no such value exists, an empty Series is returned.
    """
    # Filter DataFrame to only include rows where the column value is strictly higher than lookup_value
    filtered_df = df.loc[df[col] > lookup_value]
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return pd.Series(dtype='float')
    
    # Find the index of the row with the closest value that is strictly higher than lookup_value
    closest_index = (filtered_df[col] - lookup_value).idxmin()
    
    # Return the row with the closest upper value
    return df.loc[closest_index]


def df_closest_lower_value(df: pd.DataFrame, col: str, lookup_value: float) -> pd.Series:
    """
    Find the row in a DataFrame where the value in a specified column
    is closest but strictly lower than a given lookup value.

    Parameters:
    ----------
    df : pd.DataFrame
        The DataFrame to search.
    col : str
        The name of the column in the DataFrame to compare against the lookup_value.
    lookup_value : float
        The value to find the closest lower match for in the specified column.

    Returns:
    -------
    pd.Series
        A pandas Series object representing the row in the DataFrame where
        the column's value is closest but strictly lower than the lookup_value.
        If no such value exists, an empty Series is returned.
    """
    # Filter DataFrame to only include rows where the column value is strictly lower than lookup_value
    filtered_df = df.loc[df[col] < lookup_value]
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return pd.Series(dtype='float')
    
    # Calculate the difference and find the index of the row with the closest value that is strictly lower
    closest_index = (lookup_value - filtered_df[col]).idxmin()
    
    # Return the row with the closest lower value
    return df.loc[closest_index]

def df_closest_value(df: pd.DataFrame, col: str, lookup_value: float) -> pd.Series:
    """
    Find the row in a DataFrame where the value in a specified column
    is closest to a given lookup value.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to search.
    column_name : str
        The name of the column in the DataFrame to compare the lookup_value against.
    lookup_value : float
        The value to find the closest match for in the specified column.

    Returns
    -------
    pd.Series
        A pandas Series object representing the row in the DataFrame where
        the column's value is closest to the lookup_value. If the DataFrame
        is empty or the column does not exist, an empty Series is returned.

    Examples
    --------
    >>> data = {'x1': [2.5, 2.6, 3.0, 2.4, 2.565, 2.575], 'x2': ['A', 'B', 'C', 'D', 'E', 'F']}
    >>> df = pd.DataFrame(data)
    >>> closest_value(df, 'x1', 2.568)
    x1    2.565
    x2        E
    Name: 4, dtype: object
    """
    if col not in df.columns:
        # Return an empty Series if the column does not exist
        return pd.Series(dtype='object')

    try:
        # Compute the absolute difference and find the index of the smallest difference
        closest_index = (df[col] - lookup_value).abs().idxmin()
        # Return the row with the closest value
        return df.loc[closest_index]
    except ValueError:
        # Return an empty Series if the DataFrame is empty or another error occurs
        return pd.Series(dtype='object')

