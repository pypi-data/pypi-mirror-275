import pandas as pd

class datetime_handler:
    def __init__(self):
        pass
    
    def extract_date_parts(self, df, column):
        df[column] = pd.to_datetime(df[column])
        df[f'{column}_year'] = df[column].dt.year
        df[f'{column}_month'] = df[column].dt.month
        df[f'{column}_day'] = df[column].dt.day
        df[f'{column}_weekday'] = df[column].dt.weekday
        return df
