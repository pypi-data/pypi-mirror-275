import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

class MissingValueHandler:
    def _init_(self):
        self.imputer = SimpleImputer()

    def impute_mean(self, data):
        self.imputer = SimpleImputer(strategy='mean')
        return pd.DataFrame(self.imputer.fit_transform(data), columns=data.columns, index=data.index)

    def impute_median(self, data):
        self.imputer = SimpleImputer(strategy='median')
        return pd.DataFrame(self.imputer.fit_transform(data), columns=data.columns, index=data.index)

    def impute_constant(self, data, constant):
        self.imputer = SimpleImputer(strategy='constant', fill_value=constant)
        return pd.DataFrame(self.imputer.fit_transform(data), columns=data.columns, index=data.index)

    def delete_missing(self, data):
        return data.dropna()