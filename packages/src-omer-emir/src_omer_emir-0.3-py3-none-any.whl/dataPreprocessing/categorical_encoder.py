from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pandas as pd


class CategoricalEncoder:
    def oneHotEncode(self, df, column):
        encoder = OneHotEncoder(sparse=False)
        encoded = encoder.fit_transform(df[[column]])
        df = df.join(pd.DataFrame(encoded, columns=encoder.get_feature_names_out([column])))
        return df.drop(columns=[column])

    def labelEncode(self, df, column):
        encoder = LabelEncoder()
        df[column] = encoder.fit_transform(df[column])
        return df