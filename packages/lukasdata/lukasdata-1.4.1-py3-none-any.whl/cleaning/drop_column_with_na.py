import pandas as pd
from datahandling.change_directory import chdir_data

def drop_nan_columns(df : pd.DataFrame,min_na_percentage: float=1):
    #should I copy here?
    bool_df=df.notna()
    print(bool_df.columns)
    print(df.columns)
    for column_name in df.columns:
        if bool_df[column_name].sum()/len(bool_df) < min_na_percentage:
            df=df.drop(columns=column_name,axis=1)
            print(f"dropped {column_name}")
    return df
