import pandas as pd


class DataTypeConverter:
    def toNumeric(self, df, column):
        df[column] = pd.to_numeric(df[column], errors='coerce')

    def toCategorical(self, df, column):
        df[column] = df[column].astype('category')