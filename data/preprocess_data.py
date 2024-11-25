import numpy as np
import pandas as pd
import pickle
from typing import Literal, Union
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split


class PreprocessingPipeline:
    def __init__(self):
        self.label_encoder = LabelEncoder()
        self.scaler = MinMaxScaler()
    
    def fit(self, X: pd.DataFrame, y: pd.DataFrame) -> None:
        self.scaler.fit(X)
        self.label_encoder.fit(y=y)

    def transform(self, X: pd.DataFrame, y: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        X_transformed = self.scaler.transform(X)
        y_transformed = self.label_encoder.transform(y)
        return X_transformed, y_transformed
    
    def inverse_transform(self, X: pd.DataFrame, y: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        return self.scaler.inverse_transform(X), self.label_encoder.inverse_transform(y)


def get_raw_data():
    data, labels = pd.read_parquet('./data/data.parquet'), pd.read_parquet('./data/labels.parquet')
    data, labels = data.drop(columns = 'Unnamed: 0'), labels.drop(columns = 'Unnamed: 0')
    # splits data to train 60%, val 20%, test 20%
    X_train, X_temp, y_train, y_temp = train_test_split(data, labels, test_size=0.4, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
    return [X_train, y_train, X_val, y_val, X_test, y_test]


class RawData:
    def __init__(self):
        self.name = 'Raw Data'
        col = get_raw_data()

        self.X_train = col[0]
        self.y_train = col[1]
        self.X_val = col[2]
        self.y_val = col[3]
        self.X_test = col[4]
        self.y_test = col[5]

    def get_data(self):
        return [self.X_train, self.y_train, self.X_val, self.y_val, self.X_test, self.y_test]

# TODO make different type of preprocessor classes

class MinMaxScaledData(RawData):
    def __init__(self):
        pass


class StandardScaledData(RawData):
    def __init__(self):
        pass


class ShapleyReducedData(RawData):
    def __init__(self, k):
        pass


class FeatureImportanceReducedData(RawData):
    def __init__(self, k):
            pass


class PCAedData(RawData):
    def __init__(self, n_components):
        pass


# remove all zero columns from training dataset
# column_sums = X_train.sum()
# filtered_columns = column_sums[column_sums == 0]
# X_train = X_train.drop(columns = filtered_columns.index)

#standardize features with StandardScalar to normalize values, ensuring each feature has a mean of 0 and 
#   a standard deviation of 1
#https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.StandardScaler.html
# scaler = StandardScaler() # NOTE
# #fit and transform the training data
# X_train_scaled = scaler.fit_transform(X_train)
# #transform the testing data using the same scaler
# X_test_scaled = scaler.transform(X_test)

# dan's way
# preprocessor = PreprocessingPipeline()

# X_train_proced, y_train_proced = preprocessor.transform(X=X_train, y=y_train)
# X_val_proced, y_val_proced = preprocessor.transform(X=X_val, y=y_val)
# X_test_proced, y_test_proced = preprocessor.transform(X=X_test, y=y_test)


