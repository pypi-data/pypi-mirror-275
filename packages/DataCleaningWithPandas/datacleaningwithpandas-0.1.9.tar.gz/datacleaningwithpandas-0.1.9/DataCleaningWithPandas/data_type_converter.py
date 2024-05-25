import pandas as pd

class DataTypeConverter:
    def __init__(self, df):
        self.df = df
        
    def convert_to_numeric(self, df, columns):
        for column in columns:
            df[column] = pd.to_numeric(df[column], errors='coerce')
        return df

    def convert_to_categorical(self, df, columns):
        for column in columns:
            df[column] = df[column].astype('category')
        return df
