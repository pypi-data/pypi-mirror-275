import pandas as pd
from datetime import datetime
from dateutil import parser


class DateTimeHandler:
    def __init__(self):
        pass

    def filter_dates(self, df, columns, criteria, **kwargs):
        for column in columns:
            if criteria == 'min_max':
                min_date = pd.to_datetime(kwargs.get('min_date'), format='%Y-%m-%d')
                max_date = pd.to_datetime(kwargs.get('max_date'), format='%Y-%m-%d')
                df[column] = pd.to_datetime(df[column], errors='coerce', format='%d/%m/%Y')
                df = df[(df[column] >= min_date) & (df[column] <= max_date)]
            elif criteria == 'min':
                min_date = pd.to_datetime(kwargs.get('min_date'), format='%Y-%m-%d')
                df[column] = pd.to_datetime(df[column], errors='coerce', format='%d/%m/%Y')
                df = df[df[column] >= min_date]
            elif criteria == 'max':
                max_date = pd.to_datetime(kwargs.get('max_date'), format='%Y-%m-%d')
                df[column] = pd.to_datetime(df[column], errors='coerce', format='%d/%m/%Y')
                df = df[df[column] <= max_date]
        return df

    def filter_time(self, df, columns, criteria, **kwargs):
        for column in columns:
            try:
                df[column] = pd.to_datetime(df[column], format='%I:%M %p').dt.time
                if criteria == 'min_max':
                    min_time = pd.to_datetime(kwargs.get('min_time')).time()
                    max_time = pd.to_datetime(kwargs.get('max_time')).time()
                    df = df[(df[column] >= min_time) & (df[column] <= max_time)]
                elif criteria == 'min':
                    min_time = pd.to_datetime(kwargs.get('min_time')).time()
                    df = df[df[column] >= min_time]
                elif criteria == 'max':
                    max_time = pd.to_datetime(kwargs.get('max_time')).time()
                    df = df[df[column] <= max_time]
            except Exception as e:
                print(f"Error processing column '{column}': {str(e)}")
        return df

    def extract_date_parts(self, df, columns):
        for col in columns:
            if col not in df.columns:
                print(f"Column '{col}' not found in DataFrame.")
                continue
            try:
                df[col] = df[col].apply(lambda x: self.parse_date(x) if not isinstance(x, pd.Timestamp) else x)
                df[f"{col}_year"] = df[col].apply(lambda x: x.year if x is not None else None)
                df[f"{col}_month"] = df[col].apply(lambda x: x.month if x is not None else None)
                df[f"{col}_day"] = df[col].apply(lambda x: x.day if x is not None else None)
            except Exception as e:
                print(f"Error processing column '{col}': {str(e)}")
                continue
        return df

    def parse_date(self, value):
        try:
            if isinstance(value, pd.Timestamp):
                return value
            parsed_date = parser.parse(str(value)).date()
            return parsed_date
        except Exception as e:
            print(f"Error parsing date '{value}': {str(e)}")
            return None

    def extract_time_parts(self, df, columns):
        for col in columns:
            if col not in df.columns:
                print(f"Column '{col}' not found in DataFrame.")
                continue

            try:
                df[col] = df[col].apply(lambda x: self.parse_time(x) if not isinstance(x, pd.Timestamp) else x)
                df[f"{col}_hour"] = df[col].apply(lambda x: x.hour if x is not None else None)
                df[f"{col}_minute"] = df[col].apply(lambda x: x.minute if x is not None else None)
                df[f"{col}_second"] = df[col].apply(lambda x: x.second if x is not None else None)
            except Exception as e:
                print(f"Error processing column '{col}': {str(e)}")
                continue

        return df

    def parse_time(self, value):
        try:
            if isinstance(value, pd.Timestamp):
                return value
            parsed_time = parser.parse(str(value)).time()
            return parsed_time
        except Exception as e:
            print(f"Error parsing time '{value}': {str(e)}")
            return None

    def replace_date(self, df, columns, old_date, new_date):
        for col in columns:
            if col not in df.columns:
                print(f"Column '{col}' not found in DataFrame.")
                continue

            try:
                old_date = pd.to_datetime(old_date)
                new_date = pd.to_datetime(new_date)
                df[col] = df[col].apply(lambda x: new_date if x == old_date else x)
            except Exception as e:
                print(f"Error processing column '{col}': {str(e)}")
                continue

        return df

    def replace_time(self, df, columns, old_time, new_time):
        for col in columns:
            if col not in df.columns:
                print(f"Column '{col}' not found in DataFrame.")
                continue

            try:
                old_time = pd.to_datetime(old_time).time()
                new_time = pd.to_datetime(new_time).time()
                df[col] = df[col].apply(lambda x: new_time if x == old_time else x)
            except Exception as e:
                print(f"Error processing column '{col}': {str(e)}")
                continue

        return df