import pandas as pd

class DataTypeConverter:
    def __init__(self):
        pass

    def to_numeric(self, df, columns):
        try:
            for col in columns:
                unique_types = df[col].apply(type).unique()
                if len(unique_types) == 1 or (len(unique_types) == 2 and pd.NA in unique_types):
                    converted_values = pd.to_numeric(df[col], errors='coerce')
                    if not pd.isnull(converted_values).all():
                        df[col] = converted_values
                    else:
                        print(f"Column '{col}' cannot be converted to numeric as all values are NaN.")
                else:
                    print(f"Column '{col}' contains mixed data types and cannot be converted to numeric.")
        except Exception as e:
            print("An error occurred during numeric conversion:", e)
        return df

    def to_categorical(self, df, columns):
        try:
            for col in columns:
                unique_types = df[col].apply(type).unique()
                if len(unique_types) == 1 or (len(unique_types) == 2 and pd.NA in unique_types):
                    converted_values = df[col].astype('category')
                    df[col] = converted_values
                else:
                    print(f"Column '{col}' contains mixed data types and cannot be converted to categorical.")
        except Exception as e:
            print("An error occurred during categorical conversion:", e)
        return df