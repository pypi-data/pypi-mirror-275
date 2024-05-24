import pandas as pd
import numpy as np


class OutlierHandling:
    def _init_(self, file_path):
        self.file_path = file_path
        try:
            self.data = pd.read_csv(file_path)
        except Exception as e:
            print(f" error occurred!")

    def round_outlier(self, column, threshold=1.5):
        Q1 = self.data[column].quantile(0.25)
        Q3 = self.data[column].quantile(0.75)
        IQR = Q3 - Q1

        if IQR == 0:
            return

        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR

        if self.data[column].dtype == 'int64':
            self.data[column] = np.clip(self.data[column], lower_bound, upper_bound).astype(int)
        else:
            self.data[column] = np.clip(self.data[column], lower_bound, upper_bound)

    def round_all_outliers(self, threshold=1.5):
        columns = self.data.select_dtypes(include=['int64', 'float64']).columns
        for column in columns:
            self.round_outlier(column, threshold)

    def remove_outliers(self, column, threshold=1.5):
        Q1 = self.data[column].quantile(0.25)
        Q3 = self.data[column].quantile(0.75)
        IQR = Q3 - Q1

        if IQR == 0:
            return

        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR

        if self.data[column].dtype == 'int64':
            self.data = self.data[(self.data[column] >= lower_bound) & (self.data[column] <= upper_bound)]
            self.data[column] = self.data[column].astype(int)
        else:
            self.data = self.data[(self.data[column] >= lower_bound) & (self.data[column] <= upper_bound)]

    def remove_all_outliers(self, threshold=1.5):
        columns = self.data.select_dtypes(include=['int64', 'float64']).columns
        for column in columns:
            self.remove_outliers(column, threshold)

    def save_rounded_data(self, output_file):
        self.data.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")