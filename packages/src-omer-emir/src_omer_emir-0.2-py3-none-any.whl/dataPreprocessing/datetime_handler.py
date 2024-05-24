import pandas as pd

class DateTimeHandler:
    def convertToDatetime(self, df, column):
        df[column] = pd.to_datetime(df[column], errors='coerce')

    def extractDateParts(self, df, column, part):
        if part == 'year':
            df[f'{column}_year'] = df[column].dt.year
        elif part == 'month':
            df[f'{column}_month'] = df[column].dt.month
        elif part == 'day':
            df[f'{column}_day'] = df[column].dt.day
        elif part == 'weekday':
            df[f'{column}_weekday'] = df[column].dt.weekday
        return df