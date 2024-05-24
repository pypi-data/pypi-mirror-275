
import pandas as pd

class OutlierHandler:

    def __init__(self, method="iqr", threshold=1.5):
        self.method = method
        self.threshold = threshold
        self.lower_bound = None
        self.upper_bound = None

    def fit(self, X):
        if self.method == "iqr":
            numeric_cols = X.select_dtypes(include=['number'])
            Q1 = numeric_cols.quantile(0.25)
            Q3 = numeric_cols.quantile(0.75)
            IQR = Q3 - Q1
            self.lower_bound = Q1 - self.threshold * IQR
            self.upper_bound = Q3 + self.threshold * IQR
        else:
            raise ValueError("Invalid method: choose 'iqr'")
        return self

    def transform(self, X):
        if self.lower_bound is not None and self.upper_bound is not None:
            X.loc[:, self.lower_bound.index] = X[self.lower_bound.index].clip(lower=self.lower_bound, upper=self.upper_bound, axis=1)
        return X

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)
