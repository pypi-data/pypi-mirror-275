import pandas as pd

class MissingValueHandler:
    def __init__(self, df):
        self.df = df

    def impute_mean(self, column):
        if pd.api.types.is_numeric_dtype(self.df[column]):
            self.df[column].fillna(self.df[column].mean(), inplace=True)
        else:
            raise TypeError(f"Column {column} is not numeric and cannot be imputed with mean.")
        return self.df

    def impute_median(self, column):
        if pd.api.types.is_numeric_dtype(self.df[column]):
            self.df[column].fillna(self.df[column].median(), inplace=True)
        else:
            raise TypeError(f"Column {column} is not numeric and cannot be imputed with median.")
        return self.df

    def impute_constant(self, column, value):
        self.df[column].fillna(value, inplace=True)
        return self.df

    def drop_missing(self):
        self.df.dropna(inplace=True)
        return self.df
