
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class Scaler:
    def __init__(self, df):
        self.df = df
        
    def min_max_scale(self, df, columns):
        scaler = MinMaxScaler()
        df[columns] = scaler.fit_transform(df[columns])
        return df

    def standard_scale(self, df, columns):
        scaler = StandardScaler()
        df[columns] = scaler.fit_transform(df[columns])
        return df
