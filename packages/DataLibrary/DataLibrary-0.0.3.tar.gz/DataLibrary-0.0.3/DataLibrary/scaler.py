from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd

class Scaler:
    def min_max_scaling(self, data):
        scaler = MinMaxScaler()
        return pd.DataFrame(scaler.fit_transform(data), columns=data.columns, index=data.index)

    def standard_scaling(self, data):
        scaler = StandardScaler()
        return pd.DataFrame(scaler.fit_transform(data), columns=data.columns, index=data.index)