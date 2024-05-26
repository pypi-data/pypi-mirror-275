
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Next: (continue) try to use it with GarageName & GarageNameBrand
import pandas as pd
import seaborn as sns
import sys
from dataclasses import dataclass, field
from typing import Literal, Union, List, Optional
import logging
import time
from pathlib import Path
from auto_pricing_techincal_groupping import Groupping, py_to_2d_list
# sys.path.append(r"C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\03 Modeling")
# import lib03_modeling as ml

sys.path.append(r"C:\Users\n1603499\OneDrive - Liberty Mutual\Documents\19 MyPythonLibrary\03 Modeling")
import Clustering as ml
import pydantic
from pydantic import PositiveFloat, BaseModel

def auto_groupping_run():
    dev_mode = True
    # use_init_rela is True than init_group_by_base_level_avg
    # if False use init_grouping
    use_init_rela = True
    diff_rela_good = 0.01
    group_prefix_name = "M"
    weight_dict = {'DriverCity': ["Ho Chi Minh", "Ha Noi", "Dong Nai", "Binh Duong", 
                            "Ba Ria - Vung Tau", "Da Nang", "Lam Dong", "Nghe An", 
                            "Hai Phong", "Bac Ninh", "Long An", "Tay Ninh", 
                            "Dak Lak", "Thai Nguyen", "Binh Phuoc", "Others"]
                   ,
                   'weight':[46.68895968, 15.93154485, 4.660712971, 3.807950797, 2.534122477, 2.466003679, 2.366129121, 1.519140249, 1.311331547, 1.284999744, 1.240629106, 1.208051676, 0.987418931, 0.947676729, 0.947645277, 12.09768316]
                   }
    
    weight_dict = {'Model': ["Fortuner", "GLC", "CX5", "Ranger", "Innova", 
                                  "Ecosport", "CR-V", "Everest", "C-Class", 
                                  "Camry", "Others", "E-Class", "SantaFe", 
                                  "Vios", 3008, "Mazda_3", "Rest"]

                   ,
                   'weight':[6.404793394, 5.545541954, 5.04452879, 4.838141842, 4.578196474, 4.306171217, 4.178043505, 4.084559297, 2.923275916, 2.579257884, 2.49300565, 2.081754833, 2.035950969, 1.946814753, 1.617765656, 1.605237953, 43.73695991]
                   }
    
    weight_dict = {'Model': ["Others", "SAI GON FORD", "BEN THANH FORD", "TOYOTA LY THUONG KIET", "MER NGOI SAO Q7", "MER NGOI SAO TRUONG CHINH", "HONDA MY DINH", "TOYOTA DONG SAI GON", "THACO BIEN HOA", "HYUNDAI BAC NINH", "THACO DALAT", "TOYOTA HIROSHIMA", "HAXACO VO VAN KIET", "CITY FORD", "TAY FORD", "Rest"]
                   ,
                   'weight': [44.69239563, 5.102947152, 3.518216353, 3.182926663, 2.193047274, 1.629196243, 1.464867454, 1.30416915, 1.137868577, 1.065340091, 1.070003958, 1.013024448, 0.974273066, 0.954020341, 0.86312292, 29.83458068]

                   }

    dict_group = {
        'Dak Lak (Only)': ["Dak Lak"],
        'Thai Nguyen (Only)': ["Thai Nguyen"],
    }
    session_name = "GarageName_01"
    saved_folder = r'C:\Users\n1603499\OneDrive - Liberty Mutual\Documents\19 MyPythonLibrary\08 WorkRelated'

    df_weight = pd.DataFrame(weight_dict)
    group_obj = Groupping(df_weight,session_name,saved_folder,diff_rela_good)
    
    val_str: str
    
    i = 0
    base_level_avg = []
   
    group_modeling = [0.796966954, 0.796966954, 0.796966954, 0.87272271, 0.796966954, 0.796966954, 0.796966954, 0.796966954, 0.796966954, 0.796966954, 0.796966954, 0.796966954, 0.796966954, 0.796966954, 0.796966954, 0.796966954]
    group_valid = [0.831430825, 0.831430825, 0.831430825, 0.883521041, 0.831430825, 0.831430825, 0.831430825, 0.831430825, 0.831430825, 0.831430825, 0.831430825, 0.831430825, 0.831430825, 0.831430825, 0.831430825, 0.831430825]



    while i < 10:
        
        if dev_mode:
            if i == 0:
                if use_init_rela:
                    modeling_2d = group_modeling
                    validation_2d = group_valid
                    group_obj.init_group_by_base_level_avg(modeling_2d,validation_2d,group_prefix_name= group_prefix_name)
                else:
                    modeling_2d_start = [[0.817543751, 0.810260495, 0.917111386], [0.848960175, 0.869893649, 0.866310899], [0.815782391, 0.835862259, 0.866310899], [0.853314686, 0.83656395, 0.899851938], [0.875628677, 0.867153981, 0.903853834], [1.118889979, 1.108604791, 0.873579675], [1.086807006, 0.935220036, 1.033391756], [1.066859679, 0.97532397, 1.033391756], [0.954048567, 0.932008972, 0.873579675], [1.118753329, 0.994048147, 1.033391756], [0.813152426, 0.809474192, 0.899851938], [0.932993139, 0.956449836, 0.863504243], [0.924920496, 1.057070104, 0.731130587], [0.969709058, 0.963754445, 0.812205402], [0.790915196, 0.862163562, 0.903853834], [0.92800273, 0.968863884, 0.838365892]]
                    validation_2d_start = [[0.811297774, 0.805570448, 0.930648394], [0.835771794, 0.852748294, 0.891305186], [0.840070073, 0.841564887, 0.891305186], [0.796326847, 0.834226777, 0.859257016], [0.919294849, 0.869059851, 0.965881272], [1.135715345, 1.113219278, 0.913828921], [1.039388676, 0.93717378, 1.019576143], [1.067876639, 0.961453891, 1.019576143], [0.948239183, 0.927246079, 0.913828921], [1.060677546, 0.978739325, 1.019576143], [0.794621137, 0.805156709, 0.859257016], [0.863306892, 0.939351505, 0.813323117], [0.983682934, 1.075258394, 0.801224157], [1.02226959, 0.943293886, 0.806501837], [0.772740757, 0.85536548, 0.965881272], [0.936436292, 0.966976608, 0.870720448]]

                    modeling_2d = modeling_2d_start
                    validation_2d = validation_2d_start
                    group_obj.init_grouping(modeling_2d, validation_2d)
            else:
                # modeling_2d = [[0.767593357, 0.776449712, 0.796966954], [0.783419841, 0.777977073, 0.796966954], [0.805916493, 0.823542722, 0.796966954], [1.04160303, 1.027258831, 0.87272271], [1.005588095, 0.996206534, 0.796966954], [1.083449379, 0.978518007, 0.796966954], [0.965079535, 0.975462181, 0.796966954], [0.863359316, 0.785910918, 0.796966954], [0.944561005, 0.838894075, 0.796966954], [1.134841742, 1.072403194, 0.796966954], [1.308467611, 1.137391738, 0.796966954], [0.84989693, 0.963910192, 0.796966954], [1.09849791, 1.009394595, 0.796966954], [0.822586853, 0.821193033, 0.796966954], [0.772174179, 0.848023508, 0.796966954], [0.95593559, 0.961632381, 0.796966954]]
                # validation_2d = [[0.766919178, 0.776965821, 0.831430825], [0.77731292, 0.762749426, 0.831430825], [0.831362346, 0.810357207, 0.831430825], [1.009853625, 0.99559842, 0.883521041], [0.961454295, 0.987756763, 0.831430825], [0.969123211, 0.967310553, 0.831430825], [0.954428179, 0.94415676, 0.831430825], [0.803347511, 0.787993184, 0.831430825], [0.945172219, 0.860902178, 0.831430825], [1.121058887, 1.032470225, 0.831430825], [1.293783415, 1.126831078, 0.831430825], [0.916471885, 0.963668334, 0.831430825], [1.08301337, 0.997108972, 0.831430825], [0.823028223, 0.805490032, 0.831430825], [0.796435718, 0.834833481, 0.831430825], [0.950065221, 0.953850135, 0.831430825]]
                text_input = input('\n Enter the modeling Observed ,Fitted, BaseLevel Avg as 2d list:\n\n')
                modeling_2d = py_to_2d_list(text_input)
                
                text_input = input('\n Enter the validation Observed, Fitted, BaseLevel Avg as 2d list:\n\n')
                validation_2d = py_to_2d_list(text_input)
                
                group_obj.update_groupping(modeling_2d, validation_2d)
        # production mode
        else:
            if i == 0:
                group_obj.init_group_by_base_level_avg(group_modeling,group_valid,group_prefix_name= group_prefix_name)


            text_input = input('\n Enter the modeling Observed ,Fitted, BaseLevel Avg as 2d list:\n\n')
            modeling_2d = py_to_2d_list(text_input)
            
            text_input = input('\n Enter the validation Observed, Fitted, BaseLevel Avg as 2d list:\n\n')
            validation_2d = py_to_2d_list(text_input)
            
            group_obj.update_groupping(modeling_2d, validation_2d)
            
                  
        i += 1
    print('From auto_groupping_run')

def main():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # logging.basicConfig(level = logging.DEBUG)
    auto_groupping_run()
    # print('From main')


if __name__ == '__main__':
    main()