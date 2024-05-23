import pandas as pd
import numpy as np

class MissingValueHandler:
    def __init__(self, strategy='mean', fill_value=None):
        self.strategy = strategy
        self.fill_value = fill_value
    
    def fit(self, X):
        if self.strategy == 'mean':
            self.fill_value = X.mean()
        elif self.strategy == 'median':
            self.fill_value = X.median()
        elif self.strategy == 'constant':
            if self.fill_value is None:
                raise ValueError("fill_value must be specified for constant strategy")
        elif self.strategy == 'delete':
            self.fill_value = None
        else:
            raise ValueError(f"Unknown strategy: {self.strategy}")
        return self
    
    def transform(self, X):
        if self.strategy == 'delete':
            return X.dropna()
        else:
            return X.fillna(self.fill_value)

    def fit_transform(self, X):
        return self.fit(X).transform(X)
