import numpy as np
import pandas as pd
from scipy import stats

def replace_column_w_nan(df, list_of_columns, replace):
    for column in list_of_columns:
        df[column] = df[column].replace(to_replace=replace, value=np.nan)
    print("Replaced {} values from these columns:{}".format(replace, list_of_columns))
    
def drop_na_rows(df, list_of_columns):
    df.dropna(axis=0, subset=list_of_columns, inplace=True)
    print("Removed NA rows from these columns:{}.".format(list_of_columns))

def drop_columns(df, list_of_columns):
    df.drop(axis=1, columns=list_of_columns, inplace = True)
    print("Dropped these columns:{}".format(list_of_columns))

def strip_spaces(df):
    df = df.applymap(lambda x: x.strip() if type(x) == str else x)
    print("stripped leading/trailing spaces from all cells of string type")

def check_duplicates(df):
    if df.duplicated().sum():
        print("there are duplicates")
    else:
        print("You're all clear of duplicates")

def remove_outliers(df, list_of_columns, zthreshold=3):
    """zthreshold is an optional parameter default set to 3"""
    for column in list_of_columns:
        df.reset_index(inplace=True,drop=True)
        column_zscore = get_z_score(df[column])
        df = drop_high_zscores(df, column_zscore, zthreshold)
    print("Removed outliers from these columns:{}".format(list_of_columns))
    return df

def get_z_score(df_column):
    zscore_list = np.abs(stats.zscore(df_column))
    return enumerate(zscore_list)

def drop_high_zscores(df, enumerated_zscores,zthreshold):
    for index, element in enumerated_zscores:
        if element > zthreshold:
            df = df.drop([index])
    return df

