import os
import urllib.request as request
import zipfile
from insurancePP.logging import logger
from insurancePP.utils.common import get_size, save_object
from datasets import load_from_disk
from insurancePP.logging import logger

import numpy as np
from numpy import save
import pandas as pd
import sys
from pathlib import Path

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from insurancePP.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config


    def get_data_transformer_object(self):
        try:
            categorical_columns = ['sex', 'smoker', 'region']
            numerical_columns = ['age', 'bmi', 'children']
            logger.info("Numerical and Categorical features has been extracted from dataset")

            logger.info("creating categorical pipeline")
            categorical_pipeline = Pipeline([
                ('imputer', SimpleImputer(strategy='most_frequent', fill_value='missing')),
                ('onehot', OneHotEncoder()),
                ('scaler', StandardScaler(with_mean=False))
            ])

            logger.info("creating numerical pipelines")
            numerical_pipeline = Pipeline([
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])

            logger.info("creating column transformer object")
            preprocessor = ColumnTransformer([
                ('numerical_pipeline', numerical_pipeline, numerical_columns),
                ('categorical_pipeline', categorical_pipeline, categorical_columns)
            ])

            return preprocessor
        
        except Exception as e:
            raise e


    def initiate_data_transformation(self):
        try:
            train_df = pd.read_csv(self.config.train_data_path)
            test_df = pd.read_csv(self.config.test_data_path)

            logger.info('obtaining preprocessing object')
            preprocessor_obj = self.get_data_transformer_object()

            target_column_name = 'expenses'
            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = train_df[target_column_name]


            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name]

            logger.info('Applying preprocessing object on training and testing dataframe')

            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save(self.config.prepared_train_data, train_arr)
            save(self.config.prepared_test_data, test_arr)

            save_object(
                file_path = Path(self.config.preprocessor_obj_file_path),
                obj = preprocessor_obj
            )


        except Exception as e:
            raise e

    