import pandas as pd
import numpy as np

class MissingValueHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_file(file_path)

    def change_budget(self, df, column_name):
        if column_name in df.columns:
            df[column_name] = df[column_name].round().astype(float)

    def validate_data_types(self, data):
        for column in data.columns:
            if data[column].dtype == 'int64' or data[column].dtype == 'float64':
                data[column] = pd.to_numeric(data[column], errors='coerce')
            elif data[column].dtype == 'object':
                data[column] = data[column].astype(str)
        return data

    def read_file(self, file_path):
        garbage_values = ["n/a", "na", "--", "—", ",", ".", "*"]
        data = pd.read_csv(file_path, na_values=garbage_values)
        data = self.validate_data_types(data)
        self.change_budget(data, 'Budget in USD')
        return data

    def print_modified_rows(self, original_df, modified_df):
        modified_rows = original_df.ne(modified_df).any(axis=1)
        if modified_rows.any():
            print(modified_df[modified_rows])
        else:
            print("No modified rows found.")

    def impute_mean(self, df):
        df_imputed = df.copy()
        for column in df_imputed.columns:
            if df_imputed[column].dtype in ['float64', 'int64']:
                df_imputed[column].fillna(df_imputed[column].mean(), inplace=True)
        self.change_budget(df_imputed, 'Budget in USD')
        return df_imputed

    def impute_median(self, df):
        df_imputed = df.copy()
        for column in df_imputed.columns:
            if df_imputed[column].dtype in ['float64', 'int64']:
                df_imputed[column].fillna(df_imputed[column].median(), inplace=True)
        self.change_budget(df_imputed, 'Budget in USD')
        return df_imputed

    def impute_mode(self, df):
        df_imputed = df.copy()
        for column in df_imputed.columns:
            if df_imputed[column].dtype in ['float64', 'int64']:
                df_imputed[column].fillna(df_imputed[column].mode()[0], inplace=True)
        self.change_budget(df_imputed, 'Budget in USD')
        return df_imputed

    def impute_constant(self, df, value):
        df_imputed = df.copy()
        df_imputed.fillna(value, inplace=True)
        self.change_budget(df_imputed, 'Budget in USD')
        return df_imputed

    def impute_ffill(self, df):
        df_ffill = df.ffill()
        self.change_budget(df_ffill, 'Budget in USD')
        return df_ffill

    def impute_bfill(self, df):
        df_bfill = df.bfill()
        self.change_budget(df_bfill, 'Budget in USD')
        return df_bfill

    def drop_missing_rows(self, df):
        return df.dropna()

    def drop_missing_columns(self, df):
        return df.dropna(axis=1)

