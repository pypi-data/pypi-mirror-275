import pandas as pd
import numpy as np


class MissingValueHandler:


    def __init__(self, strategy="mean", fill_value=None):
        self.strategy = strategy
        self.fill_value = fill_value

    @staticmethod
    def drop_missing(df, column):
        df = df.dropna(subset=[column])
        return df

    def transform(self, X):
        return X.fillna(self.fill_value)

    def fit_transform(self, X):
        return self.fit(X).transform(X)

    @staticmethod
    def fill_with_mean(df, column):
        df[column] = df[column].fillna(df[column].mean()).astype(df[column].dtype)
        return df

    def fit(self, X):
        if self.strategy == "mean":
            self.fill_value = X.mean()
        elif self.strategy == "median":
            self.fill_value = X.median()
        elif self.strategy == "constant":
            if self.fill_value is None:
                raise ValueError("fill_value must be provided for constant strategy")
        else:
            raise ValueError("Invalid strategy: choose from 'mean', 'median', 'constant'")
        return self


    @staticmethod
    def fill_with_mode(df, column):
        df[column] = df[column].fillna(df[column].mode()[0]).astype(df[column].dtype)
        return df

    @staticmethod
    def fill_with_median(df, column):
        df[column] = df[column].fillna(df[column].median()).astype(df[column].dtype)
        return df

