from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pandas as pd

class CategoricalEncoder:
    def one_hot_encode(self, data, column):
        encoder = OneHotEncoder(sparse=False)
        encoded = encoder.fit_transform(data[[column]])
        encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out([column]))
        return pd.concat([data.reset_index(drop=True), encoded_df.reset_index(drop=True)], axis=1).drop(column, axis=1)

    def label_encode(self, data, column):
        encoder = LabelEncoder()
        data[column] = encoder.fit_transform(data[column])
        return data