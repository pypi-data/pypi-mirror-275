import pandas as pd

class feature_engineer:
    def __init__(self):
        pass
    
    def create_feature(self, df, new_column, func, *args, **kwargs):
        df[new_column] = func(df, *args, **kwargs)
        return df

    
    def add_columns(df, column1, column2, operation=lambda x, y: x + y):
        return operation(df[column1], df[column2])
