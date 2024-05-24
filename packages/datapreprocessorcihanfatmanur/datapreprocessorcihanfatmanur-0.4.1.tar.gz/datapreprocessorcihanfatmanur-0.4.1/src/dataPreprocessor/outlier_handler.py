import pandas as pd
import numpy as np

class outlier_handler:
    def __init__(self):
        pass
    
    def iqr_outliers(self, df, column, threshold=1.5):
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR
        return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
