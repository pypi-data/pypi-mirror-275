
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

class CategoricalEncoder:
    def __init__(self, df):
        self.df = df
    
    def one_hot_encode(self, df, columns):
        encoder = OneHotEncoder(sparse=False, drop='first')
        encoded_columns = encoder.fit_transform(df[columns])
        df = df.drop(columns, axis=1)
        df = pd.concat([df, pd.DataFrame(encoded_columns, columns=encoder.get_feature_names_out(columns))], axis=1)
        return df

    def label_encode(self, df, columns):
        encoder = LabelEncoder()
        for column in columns:
            df[column] = encoder.fit_transform(df[column])
        return df
