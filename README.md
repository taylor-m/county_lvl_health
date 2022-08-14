# county_lvl_health_analysis

## Details:
federal Health Resource and Service Administration makes available the Area Health Resource File (AHRF) database - a comprehensive county-level database of demographic and available healthcare options nationwide

**data URL:** https://data.hrsa.gov/data/download?data=AHRF#AHRF

### Output objectives:
1. python class
    - parse
    - normalize
2. simple utilities
   - demographic and health care details**
    - county level or state level
3. export data to CSV
4. analysis in jupyter notebook

### initial analysis objectives:
    1. view what different types of data are included in the given fields
        - which columns provide descriptive information about the samples
    2. identify levels of organization and grouping levels
    3. look at the documentation and identify features with excess info and no added descriptive value
        - 7418 initially imported columns
    4. identify 10-20 initial features for analysis that will likely have the least multicollinearity
    5. identify & create a plan for dealing with missing data
    6. create functions for data standardization/scaling
    7. visualization
    8. dictate early notes, hypotheses, and questions

### Utility functions
    1. standardize_data()
    2. create_year_column()
    3. create_var_legend()
    4. create_dataframe()
    5. filter_input_features()
    6. geo_map()
    
### Output files
    1. variable_legend.csv --> summarized file with key for data ids 
    2. non_health_vars.csv --> non_health descriptive fields 
    3. health_vars.csv --> healthcare descriptive fields
    4. misc_vars.csv  --> other misc non-descriptive fields

### Files
    county_level_analysis.ipynb  --> jupyter-notebook with analysis code for data cleaning and exploration of the dataset
    health_lvl_analysis_class.py --> python file with class and multiple submethods created for handling the data import, cleaning, and some analysis to work of off
    hlvl_util.py
    
### Visualizations
    - visualizations will be saved to the 'figures' folder as .png file types that can be viewed outside of the notebook
    

        