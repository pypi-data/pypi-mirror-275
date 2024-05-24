import pandas as pd

class data_type_converter:
    def __init__(self):
        pass
    
    def to_numeric(self, df, column):
        df[column] = pd.to_numeric(df[column], errors='coerce')
        return df
    
    def to_categorical(self, df, column):
        df[column] = df[column].astype('category')
        return df
