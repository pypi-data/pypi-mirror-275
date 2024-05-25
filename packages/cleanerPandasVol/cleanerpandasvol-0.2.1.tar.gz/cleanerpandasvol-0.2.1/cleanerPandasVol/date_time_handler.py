import pandas as pd
from datetime import datetime, timedelta



class DateTimeHandler:
    @staticmethod
    def convert_to_datetime(df, column, format=None):
        df[column] = pd.to_datetime(df[column], format=format)
        return df

    @staticmethod
    def extract_date_component(df, column, component):
        if component == 'year':
            df[f'{column}_year'] = df[column].dt.year
        elif component == 'month':
            df[f'{column}_month'] = df[column].dt.month
        elif component == 'day':
            df[f'{column}_day'] = df[column].dt.day
        return df
    