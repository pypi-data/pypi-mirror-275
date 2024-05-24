import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import category_encoders as c

class CategoricalEncoder:

    def __init__(self):
        self.encoders = {}


    @staticmethod
    def one_hot_encode(df, column):
        ohe = OneHotEncoder(sparse_output=False)
        encoded = ohe.fit_transform(df[[column]])
        encoded_df = pd.DataFrame(encoded, columns=ohe.get_feature_names_out([column]))
        df = pd.concat([df.drop(column, axis=1), encoded_df], axis=1)
        return df, ohe

    @staticmethod
    def label_encode(df, column):
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        return df, le


