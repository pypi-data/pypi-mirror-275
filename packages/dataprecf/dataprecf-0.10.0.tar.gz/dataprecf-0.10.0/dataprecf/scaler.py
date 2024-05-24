import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class scaler:
    def __init__(self):
        self.min_max_scaler = MinMaxScaler()
        self.standard_scaler = StandardScaler()

    def min_max_scale(self, df, column):
        df[column] = self.min_max_scaler.fit_transform(df[[column]])
        return df
    
    def standard_scale(self, df, column):
        df[column] = self.standard_scaler.fit_transform(df[[column]])
        return df
