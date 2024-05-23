from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

class Scaler:
    def __init__(self, method='standard'):
        if method == 'standard':
            self.scaler = StandardScaler()
        elif method == 'minmax':
            self.scaler = MinMaxScaler()
        else:
            raise ValueError(f"Unknown method: {method}")
    
    def fit(self, X):
        self.scaler.fit(X)
        return self
    
    def transform(self, X):
        return pd.DataFrame(self.scaler.transform(X), columns=X.columns)
    
    def fit_transform(self, X):
        return self.fit(X).transform(X)
