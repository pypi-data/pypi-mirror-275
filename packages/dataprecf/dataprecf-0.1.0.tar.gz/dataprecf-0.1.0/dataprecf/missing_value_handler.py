import pandas as pd
import numpy as np

class missing_value_handler:
    def __init__(self):
        pass
    
    def impute_mean(self, df, column):
        df[column].fillna(df[column].mean(), inplace=True)
        return df
    
    def impute_median(self, df, column):
        df[column].fillna(df[column].median(), inplace=True)
        return df
    
    def impute_constant(self, df, column, value):
        df[column].fillna(value, inplace=True)
        return df
    
    def delete_missing(self, df, column):
        df.dropna(subset=[column], inplace=True)
        return df
