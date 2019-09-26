import numpy as np
import pandas as pd


# this function works
# df_KC.sqft_basement = df_KC.sqft_basement.replace(to_replace='?', value=np.nan)
def replace_column_w_nan(df, list_of_columns, replace):
    for column in list_of_columns:
        df[column] = df[column].replace(to_replace=replace, value=np.nan)
    print("{}'s have been replaced with nan in all of these columns {}".format(replace, list_of_columns))





def drop_na_rows(df, list_of_columns):
    df = df.dropna(axis=0, subset=list_of_columns)
    print("na rows from these columns ,{}, have been removed.".format(list_of_columns))
    return df








# This function works.
# kcdf = kcdf.drop(axis=1, columns=['waterfront', 'yr_renovated'])
def drop_columns(df, list_of_columns):
    df.drop(axis=1, columns=list_of_columns, inplace = True)
    print("{} have been dropped".format(list_of_columns))

# This function works.
# df.duplicated().sum()
def check_duplicates(df):
    if df.duplicated().sum():
        print("there are duplicates")
    else:
        print("You're all clear")

            
    