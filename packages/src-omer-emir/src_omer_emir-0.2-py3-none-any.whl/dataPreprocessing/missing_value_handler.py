import pandas as pd


class MissingValueHandler:
    def imputeByMean(self, df, column):
        mean_value = df[column].mean()
        df[column].fillna(mean_value, inplace=True)

    def imputeByMedian(self, df, column):
        median_value = df[column].median()
        df[column].fillna(median_value, inplace=True)

    def imputeByConstant(self, df, column, constant):
        df[column].fillna(constant, inplace=True)

    def deleteByMissing(self, df, column):
        df.dropna(subset=[column], inplace=True)