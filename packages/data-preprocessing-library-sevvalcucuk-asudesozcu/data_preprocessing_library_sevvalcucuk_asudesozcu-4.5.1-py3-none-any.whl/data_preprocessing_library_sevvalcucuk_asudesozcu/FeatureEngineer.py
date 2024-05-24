import pandas as pd


class FeatureEngineer:
    def __init__(self):
        pass

    def sort_df_alphabetically(self, df, column, ascending=True):
        sorted_df = df.sort_values(by=column, ascending=ascending)
        return sorted_df

    def sort_df_by_date(self, df, column, ascending=True, date_format='%d/%m/%Y'):
        df[column] = pd.to_datetime(df[column], format=date_format)
        sorted_df = df.sort_values(by=column, ascending=ascending)
        sorted_df[column] = sorted_df[column].dt.strftime(date_format)
        return sorted_df

    def filter_df_by_key(self, df, column, key, exists=True):
        original_type = df[column].dtype

        try:
            df[column] = df[column].astype(type(key))
        except ValueError as e:
            raise ValueError(f"Could not convert column '{column}' to type {type(key)}: {e}")

        if exists:
            filtered_df = df[df[column] == key]
        else:
            filtered_df = df[df[column] != key]

        df[column] = df[column].astype(original_type)

        return filtered_df

    def sort_df_by_key(self, df, column, key, exist=True):
        original_df = df.copy()
        original_type = df[column].dtype
        if isinstance(key, str):
            try:
                key = pd.to_datetime(key, dayfirst=True, errors='coerce')
                df[column] = pd.to_datetime(df[column], dayfirst=True, errors='coerce')
                if df[column].isna().any():
                    raise ValueError(f"Column '{column}' contains invalid dates that couldn't be parsed.")
            except ValueError as e:
                raise ValueError(f"Could not convert column '{column}' to datetime: {e}")
        else:
            try:
                df[column] = df[column].astype(type(key))
            except ValueError as e:
                raise ValueError(f"Could not convert column '{column}' to type {type(key)}: {e}")

        if exist:
            sorted_df = df[df[column] >= key]
        else:
            sorted_df = df[df[column] < key]

        df[column] = original_df[column]

        return original_df.iloc[sorted_df.index]
