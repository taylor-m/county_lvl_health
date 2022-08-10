# package import
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import hlvl_util as hlvl
from hlvl import create_var_legend, create_dataframe, filter_input_features
from sas7bdat import SAS7BDAT 


class health_lvl():
    
    def __init__(self, level_description, filepath, file_type=['sas', 'csv']):
        health_lvl.level_description = level_description

    def data_init(self):
        health_lvl.input_data = filepath
        health_lvl.file_type = file_type

        health_lvl.data = create_dataframe(health_lvl.input_data, health_lvl.file_type)
        health_lvl.var_data = create_var_legend(health_lvl.input_data, health_lvl.file_type)
        return health_lvl.data, health_lvl.var_data
    
    process_input = property(data_init)
                 
    def set_feature_list(self, features_list):
        health_lvl.features = filter_input_features(health_lvl.data, health_lvl.var_data, features_list)
        return health_lvl.features
    
    