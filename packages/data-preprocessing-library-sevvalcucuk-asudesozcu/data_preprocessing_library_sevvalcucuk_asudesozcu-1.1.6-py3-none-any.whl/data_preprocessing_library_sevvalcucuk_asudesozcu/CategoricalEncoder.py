import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import numpy as np

class CategoricalEncoder:
    def __init__(self):
        self.label_encoders = {}
        self.one_hot_encoders = {}
        self.binary_encoders = {}
        self.frequency_encoders = {}

    def one_hot_encode(self, df, columns):
        for column in columns:
            encoder = OneHotEncoder(sparse_output=False)
            encoded_data = encoder.fit_transform(df[[column]])
            encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out([column]))
            df = df.drop(column, axis=1)
            df = pd.concat([df, encoded_df], axis=1)
            self.one_hot_encoders[column] = encoder
        return df

    def label_encode(self, df, columns):
        for column in columns:
            encoder = LabelEncoder()
            df[column] = encoder.fit_transform(df[column])
            self.label_encoders[column] = encoder
        return df

    def binary_encode(self, df, columns):
        for column in columns:
            unique_values = df[column].unique()
            max_bits = len(bin(len(unique_values) - 1)) - 2
            binary_encoded = df[column].apply(lambda x: list(map(int, bin(x)[2:].zfill(max_bits))))
            binary_encoded_df = pd.DataFrame(binary_encoded.tolist(), columns=[f'{column}_bin_{i}' for i in range(max_bits)])
            df = df.drop(column, axis=1)
            df = pd.concat([df, binary_encoded_df], axis=1)
            self.binary_encoders[column] = unique_values
        return df

    def frequency_encode(self, df, columns):
        for column in columns:
            frequency = df[column].value_counts()
            df[column] = df[column].map(frequency)
            self.frequency_encoders[column] = frequency
        return df

    def inverse_label_encode(self, df, columns):
        for column in columns:
            if column in self.label_encoders:
                encoder = self.label_encoders[column]
                df[column] = encoder.inverse_transform(df[column])
        return df

    def inverse_one_hot_encode(self, df, columns):
        for column in columns:
            if column in self.one_hot_encoders:
                encoder = self.one_hot_encoders[column]
                encoded_columns = encoder.get_feature_names_out([column])
                column_data = df[encoded_columns]
                original_data = encoder.inverse_transform(column_data)
                original_series = pd.Series(original_data.flatten(), name=column)
                df = df.drop(encoded_columns, axis=1)
                df = pd.concat([df.iloc[:, :1], original_series, df.iloc[:, 1:]], axis=1)
        return df
