'''
UTILITY FUNCTIONS FOR HEALTH_LVL CLASS
'''

# package import
# import numpy as np
# import pandas as pd
# import seaborn as sns
# import plotly.express as px
# from sas7bdat import SAS7BDAT 


# =============================================================================================
#    REFORMAT_INPUT_DATA_FILE
# =============================================================================================

def reformat_input_data_file(file, input_type='sas', output_type='csv'):
    
    if input_type == 'sas' and output_type == 'csv': 
        # SAS file location
        file = 'AHRF_2020-2021_SAS\AHRF_2020-2021_SAS\AHRF2021.sas7bdat'

        #importing data from sas file as dataframe
        with SAS7BDAT(file, skip_header=False) as reader:
            df = reader.to_data_frame()
    #     df.head()
        file_out = file.replace('.sas7bdat', '.csv')
#         file_out = 'AHRF_2020-2021_SAS\AHRF_2020-2021_SAS\AHRF2021.csv'

    df.to_csv(file_out)

# =============================================================================================
#    STANDARDIZE_DATA
# =============================================================================================
def standardize_data(vals):
    # lowercase standardization
    cols = vals
    for i in range(len(cols)):
    #     print(i)
        lowercase = cols[i].lower()
        lowercase = lowercase.strip()
    #         print(lowercase)
        cols[i] = lowercase
        cols[i] = cols[i].replace(' ', '_')
        cols[i].replace('/', '')
    #replacing all dashes with underscores
        cols[i] = cols[i].replace('-', '_')
        cols[i] = cols[i].replace('______', '_')
        cols[i] = cols[i].replace('___', '_')
        cols[i] = cols[i].replace('__', '_')
        
    return cols

# =============================================================================================
#    CREATE_YEAR_COLUMN
# =============================================================================================
def create_year_column(input_df):
    #     input_df = non_health_vars
    has_years_idx = list(input_df[input_df.var_id.str.contains('_') == True].index)
    no_years_idx = list(input_df[input_df.var_id.str.contains('_') == False].index)

    input_df['data_year'] = 0
    #     input_df.loc[has_years_idx, 'data_year'] = 
    #         print(input_df.loc[has_years_idx, 'var_id'].str.split('_'))
    input_df.loc[has_years_idx, 'var_id'] = input_df.loc[has_years_idx, 'var_id'].str.split('_')
    #     print(input_df.var_id)
    input_df.data_year = input_df.var_id.astype('int', errors='ignore')
    #     print(input_df.data_year)
    take_year = lambda x: x[1]
    # print(input_df.loc[has_years_idx, 'data_year'])
    # print(input_df.data_year)
    for i in has_years_idx:
        year = int(input_df.loc[i, 'data_year'][1])
    #     print(year)
        input_df.loc[i, 'data_year'] = int(year)
    # print(input_df)
    input_df.loc[no_years_idx, 'data_year'] = 0

    for i in has_years_idx:
        var_id = input_df.loc[i, 'var_id'][0]
        input_df.loc[i, 'var_id'] = var_id
    # print(input_df)
    output_df = input_df.copy()
    return output_df

# =============================================================================================
#    CREATE_VAR_LEGEND
# =============================================================================================
def create_var_legend(input_file, file_type, delimiter='\t'):
    # importing data from documentation to create zipped variable dictionary
    #importing the var info chart from txt; copied var chart to new file
    txt_dict = input_file[1]
    dtype = file_type[1]
    
    if dtype == 'sas':
        #importing data from sas file as dataframe
        with SAS7BDAT(file, skip_header=False) as reader:
            df = reader.to_data_frame()
    elif dtype == 'csv':
        #importing data from csv file as dataframe
        txt_dict = filepath
        df = pd.read_csv(txt_dict, sep=delimiter)

    idx = txt[txt.FIELD.str.startswith('*') == True].index

    #dropping rows with only asterisk dividers
    var_legend = txt.drop(index=idx, axis=0)
    # looking at var df without starred rows & creating a field_cat category/section each field falls under
    # var_legend = txt.loc[idx, :]
    # print(var_legend.head())
    legend_df = var_legend.copy()

    idx = legend_df[legend_df['VARIABLE NAME'].isna() == True].index
    legend_df.drop(index=idx, inplace=True)
    # legend_df.head()

    drops = var_legend.FIELD[idx]
    drops = drops[drops.str.startswith('*') == False]
    drops = drops[drops.str.startswith('   ') == False]
    # print(drops)

    legend_df['field_category'] = 0
    legend_df.head()

    for idx in (drops.index):
        cat = str(drops[[idx]].values)
        legend_df.loc[idx:, 'field_category'] = cat

    legend_df.field_category = legend_df.field_category.str.slice(2,-2)
    # legend_df.field_category.fillna('none', inplace=True)
    # legend_df.head(50)

    idx = legend_df[legend_df.FIELD != 'FIELD']
    variable_legend = idx.copy()
    # variable_legend.head()

    variable_legend.columns = standardize_data(list(variable_legend.columns))
    variable_legend.fillna('na', inplace=True)
    # print(variable_legend.head())

    variable_legend.field_category = standardize_data(list(variable_legend.field_category))
    # print(variable_legend.field_category.unique())

    variable_legend.field = standardize_data(list(variable_legend.field))
    # variable_legend.head()
    variable_legend.field = variable_legend.field.str.replace('_', '')
    legend_dict = dict(zip(list(variable_legend.field), standardize_data(list(variable_legend.variable_name))))
    
    export_df = pd.DataFrame([list(legend_dict), list(legend_dict.values())]).T
    export_df.columns = ['var_id', 'var_name']
    # export_df.head()

    export_df_w_year = create_year_column(export_df)
    export_df_w_year.to_csv('feature_vars/variable_legend.csv')
    
    return export_df_w_year

# =============================================================================================
#    CREATE_DATAFRAME
# =============================================================================================
def create_dataframe(input_file, file_type, delimiter='\t'):
    dtype = health_lvl.file_type[0]
    file = health_lvl.input_data[0]
    if dtype == 'sas':
        #importing data from sas file as dataframe
        with SAS7BDAT(file, skip_header=False) as reader:
            df = reader.to_data_frame()
    elif dtype == 'csv':
        #importing data from csv file as dataframe
        txt_dict = filepath
        txt = pd.read_csv(txt_dict, sep=delimiter)

    with SAS7BDAT(file, skip_header=False) as reader:
        df = reader.to_data_frame()

    # insert null rates across variables
    na_rates = df.isna().mean().sort_values(ascending=False)
    na_rates = pd.DataFrame([na_rates.index, list(na_rates)]).T
    na_rates.columns = ['var_id', 'null_rate']
#         na_rates.head()

    # merge null rates into dataframe
    trans_df = df.T
    trans_df = trans_df.reset_index().rename(columns={'index':'var_id'})
    tdf = trans_df.merge(na_rates, how='left')
    tdf.set_index('var_id', inplace=True)
    df_updated = tdf.T
#         df_updated.head()
    df_updated.to_csv('feature_vars/updated_dataframe.csv')
    return df_updated

# =============================================================================================
#    FEATURE_INPUT_FEATURES
# =============================================================================================
def filter_input_features(df_updated, feature_list, var_legend):
    non_health_vars = pd.read_csv('feature_vars/non_health_vars.csv', index_col=0)
    health_vars = pd.read_csv('feature_vars/health_vars.csv', index_col=0)
    misc_vars = pd.read_csv('feature_vars/misc_vars.csv', index_col=0)

    non_health_vars.data_year.fillna(0, inplace=True)

    # non_health_vars_w_year = create_year_column(non_health_vars)
    non_health_vars.data_year = non_health_vars.data_year.astype('int')

    features_df = pd.concat(feature_list)
    features_df['var_year_id'] = features_df.var_id.astype('str', errors='ignore') + (features_df.data_year.astype('int', errors='ignore')).astype('str')
    features_df.var_year_id
#     features_df
    # filtering out all fields that are not in the non_health and health variable lists selected prevesiously
    var_list = [val for val in list(df_updated.columns) if val in (list(features_df.var_year_id) + list(features_df.var_id))]
    # len(var_list)

    filtered_vars = df_updated[var_list]
#     filtered_vars

# renaming the feature variable column names with the variable name dictionary (legend_dict) created earlier
    filtered_vars = filtered_vars.rename(columns = legend_dict)
    return filtered_vars

# =============================================================================================


