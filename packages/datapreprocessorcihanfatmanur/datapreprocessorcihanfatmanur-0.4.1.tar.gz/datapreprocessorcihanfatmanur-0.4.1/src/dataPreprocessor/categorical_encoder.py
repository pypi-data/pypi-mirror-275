import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

class categorical_encoder:
    def __init__(self):
        self.one_hot_encoder = OneHotEncoder(sparse=False)
        self.label_encoder = LabelEncoder()
    
    def one_hot_encode(self, df, column):
        encoded = self.one_hot_encoder.fit_transform(df[[column]])
        encoded_df = pd.DataFrame(encoded, columns=self.one_hot_encoder.get_feature_names_out([column]))
        return pd.concat([df.reset_index(drop=True), encoded_df], axis=1).drop(column, axis=1)
    
    def label_encode(self, df, column):
        df[column] = self.label_encoder.fit_transform(df[column])
        return df
