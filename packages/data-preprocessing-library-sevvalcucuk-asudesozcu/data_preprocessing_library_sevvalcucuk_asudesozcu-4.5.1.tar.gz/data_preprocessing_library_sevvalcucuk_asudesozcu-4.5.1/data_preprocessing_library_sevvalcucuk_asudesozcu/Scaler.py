import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


class Scaler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.normalized_data = None
        self.standardized_data = None

    def change_budget(self, df, column_name="Budget in USD"):
        if column_name in df.columns:
            df[column_name] = df[column_name].round().astype(float)

    def min_max_normalize(self, column_name):
        self.change_budget(self.data)
        try:
            if self.data[column_name.strip()].dtype in ['float64', 'int64']:
                min_max_scaler = MinMaxScaler()
                normalized_data = min_max_scaler.fit_transform(self.data[[column_name]])

                self.normalized_data = self.data.copy()
                self.normalized_data[column_name] = normalized_data

                return self.normalized_data
            else:
                print(f"Error: {column_name} is not a numeric column")
        except Exception as e:
            print(f"Error occurred: {e}")

    def standardize(self, column_name):
        try:
            if self.data[column_name.strip()].dtype in ['float64', 'int64']:
                standard_scaler = StandardScaler()
                standardized_data = standard_scaler.fit_transform(self.data[[column_name]])

                self.standardized_data = self.data.copy()
                self.standardized_data[column_name] = standardized_data

                return self.standardized_data
            else:
                print(f"Error: {column_name} is not a numeric column")
        except Exception as e:
            print(f"Error occurred: {e}")
