import pandas as pd
class DateTimeHandler:
    def __init__(self, df):
        self.df = df

    def to_datetime(self, column, dayfirst=True):
        self.df[column] = pd.to_datetime(self.df[column], errors='coerce', dayfirst=dayfirst)
        return self.df
    
    def extract_date_parts(self, column):
        self.df[f'{column}_year'] = self.df[column].dt.year
        self.df[f'{column}_month'] = self.df[column].dt.month
        self.df[f'{column}_day'] = self.df[column].dt.day
        return self.df
