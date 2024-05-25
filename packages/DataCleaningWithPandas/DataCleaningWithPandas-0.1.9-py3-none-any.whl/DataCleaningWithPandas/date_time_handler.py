
import pandas as pd

class DateTimeHandler:
    def __init__(self, df):
        self.df = df
        
    def extract_date_features(self, df, column):
        df[column] = pd.to_datetime(df[column])
        df[f'{column}_year'] = df[column].dt.year
        df[f'{column}_month'] = df[column].dt.month
        df[f'{column}_day'] = df[column].dt.day
        df[f'{column}_weekday'] = df[column].dt.weekday
        return df

    def convert_to_datetime(self, df, columns):
        for column in columns:
            df[column] = pd.to_datetime(df[column], errors='coerce')
        return df
