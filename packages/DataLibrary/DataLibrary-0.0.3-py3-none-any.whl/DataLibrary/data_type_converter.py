import pandas as pd

class DataTypeConverter:
    def convert_to_numeric(self, data, columns):
        """
        Convert specified columns in the DataFrame to numeric, handling errors by coercion.
        """
        for column in columns:
            data[column] = pd.to_numeric(data[column], errors='coerce')
        return data

    def convert_to_categorical(self, data, columns):
        """
        Convert specified columns in the DataFrame to categorical.
        """
        for column in columns:
            data[column] = data[column].astype('category')
        return data