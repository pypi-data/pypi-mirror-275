import pandas as pd
def filter_numeric_columns(df):
    columns=df.columns
    new_df=pd.DataFrame()
    for column_name in columns:
        column=df[column_name]
        try:
            pd.to_numeric(column)
            new_df[column_name]=column
            print(column_name)
        except ValueError:
            None
            print(f"{column_name} can't be converted to numeric")
    return new_df

