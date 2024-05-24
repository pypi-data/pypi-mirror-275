class OutlierHandler:
    def iqrOutlierDetection(self, df, column, threshold=1.5):
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (IQR * threshold)
        upper_bound = Q3 + (IQR * threshold)
        return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]