import pandas as pd

class MissingValueHandler:
    def __init__(self, df):
        self.df = df
        
    def impute_mean(self, df, columns):
        for column in columns:
            df[column].fillna(df[column].mean(), inplace=True)
        return df

    def impute_median(self, df, columns):
        for column in columns:
            df[column].fillna(df[column].median(), inplace=True)
        return df

    def impute_constant(self, df, columns, constant):
        for column in columns:
            df[column].fillna(constant, inplace=True)
        return df

    def drop_missing(self, df, threshold):
        return df.dropna(thresh=threshold)