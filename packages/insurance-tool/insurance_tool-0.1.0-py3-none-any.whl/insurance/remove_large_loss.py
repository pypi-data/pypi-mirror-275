# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:17:59 2024

@author: n1603499
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def large_loss_cal(df,reserve_col,claim_count_col,reserve_range,
                    segment_combine = None
                    ):
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    reserve_sort = sorted(reserve_range,reverse=True)
    
    sum_loss_list = []
    claim_count_list = []
    avg_loss_list = []
    
    total_claim_count = df[claim_count_col].sum()
    total_reserve = df[reserve_col].sum()
    
    for cut_off in reserve_sort:
        # sum of loss from 0 until excluding the cut_off
        sum_loss = df.loc[df[reserve_col] >= cut_off, reserve_col].sum() / total_reserve
        claim_count = df.loc[df[reserve_col] >= cut_off, claim_count_col].sum() / total_claim_count
        avg_loss = sum_loss / claim_count
        
        sum_loss_list.append(sum_loss)
        claim_count_list.append(claim_count)
        avg_loss_list.append(avg_loss)
    
    calculated_df = pd.DataFrame({
        'loss_cost': reserve_sort,
        'sum_loss_cost': sum_loss_list,
        'claim_count': claim_count_list,
        'avg_loss': avg_loss_list,
        
        })
    return calculated_df


def plot_remove_large_loss(df,loss_cost_col,claim_count_col,large_loss_range):
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    calculated_df = large_loss_cal(df,loss_cost_col,claim_count_col,large_loss_range)
    
    plt.figure(figsize=(10,6))
    plt.title("Sum of Loss")
    ax1 = sns.lineplot(
        data=calculated_df, x="loss_cost", y="sum_loss_cost",
        
    )
    ax1.set_ylabel('Sum of Loss Cost')
    
    plt.figure(figsize=(10,6))
    # ax2 = ax1.twinx()
    plt.stackplot(calculated_df["loss_cost"], calculated_df["claim_count"],alpha=0.5)
    
    # sns.barplot(
    #     x = "loss_cost", 
    #     y = "claim_count",
    #     data = calculated_df,
    #     color='orange', 
    #     alpha=0.5,
    #     # ax = ax2,
    
        
    # )
    # ax2.grid(False)
    # ax2.set_ylabel('claim count proportion')
    
    plt.figure(figsize=(10,6))
    sns.lineplot(
        data=calculated_df, x="loss_cost", y="avg_loss",
        
    )
    # plt.figure(figsize=(10,6))
    
    return calculated_df

data_path = r"C:/Users/n1603499/OneDrive - Liberty Mutual/Documents/15.02 ARM DS/2024/Project 12_HK Non-tesla motor scoring_in progress/04 AvE Dashboard/HK_Motor_Scored.csv"
df = pd.read_csv(data_path)


loss_range01 = np.arange(10_000, 50_000, 1_000)
loss_range02 = np.arange(0, 100_000, 1_000)

loss_range03 = np.arange(200_000, 800_000, 1_000)

loss_cost_col = "RESERVE_AMOUNT"
claim_count_col = "CLAIM_COUNT"
test01 = plot_remove_large_loss(df,loss_cost_col,claim_count_col,loss_range01)
test02 = plot_remove_large_loss(df,loss_cost_col,claim_count_col,loss_range02)
test02 = plot_remove_large_loss(df,loss_cost_col,claim_count_col,loss_range03)


data = {'C': 20, 'C++': 15, 'Java': 30, 'Python': 35}
courses = list(data.keys())
values = list(data.values())

# Create a figure
fig = plt.figure(figsize=(10, 5))

# Plot the bar chart
plt.bar(courses, values, color='maroon', width=0.4)
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()

loss_df = large_loss_cal(df,loss_cost_col,claim_count_col,loss_range01)
loss_df2 = loss_df.head(10)
plt.bar(
        loss_df2["loss_cost"], 
        loss_df2["sum_loss_cost"],
        
        )
sns.barplot(x="loss_cost", y="claim_count", data=loss_df2,color="orange")

plt.stackplot(loss_df["loss_cost"], loss_df["claim_count"],alpha=0.5)


# Define DataFrame (replace with your actual data)
df = pd.DataFrame({
    'period': [1, 2, 3, 4, 5, 6, 7, 8],
    'team_A': [20, 12, 15, 14, 19, 23, 25, 29],
    'team_B': [5, 7, 7, 9, 12, 9, 9, 4],
    'team_C': [11, 8, 10, 6, 6, 5, 9, 12]
})

# Create a basic area chart
plt.stackplot(df.period, df.team_A)
plt.xlabel('Period')
plt.ylabel('Values')
plt.title('Basic Area Chart')
plt.show()

