import numpy as np
import pandas as pd
from scipy import stats

def replace_column_w_nan(df, list_of_columns, replace):
    for column in list_of_columns:
        df[column] = df[column].replace(to_replace=replace, value=np.nan)
    print("{}'s have been replaced with nan in all of these columns {}".format(replace, list_of_columns))
    
def drop_na_rows(df, list_of_columns):
    # inplace=True is important to have. Without it, the .dropna() returns a NoneType Object
    df.dropna(axis=0, subset=list_of_columns, inplace=True)
    print("na rows from these columns ,{}, have been removed.".format(list_of_columns))

def drop_columns(df, list_of_columns):
    df.drop(axis=1, columns=list_of_columns, inplace = True)
    print("{} have been dropped".format(list_of_columns))

def strip_spaces(df):
    df = df.applymap(lambda x: x.strip() if type(x) == str else x)

def check_duplicates(df):
    if df.duplicated().sum():
        print("there are duplicates")
    else:
        print("You're all clear")

def get_z_score(df_column):
    zscore_list = np.abs(stats.zscore(df_column))
    return zscore_list

def remove_outliers(df, list_of_columns):
    for column in list_of_columns:
        
        df.reset_index(inplace=True,drop=True)
        
        column_zscore = get_z_score(df[column])
        enumerated_column_z_score = enumerate(column_zscore)
        
        for index, element in enumerated_column_z_score:
            if element > 3:
                df = df.drop([index])
    return df