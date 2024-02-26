import os
import sys
import pandas as pd
import numpy as np
from numpy import load

from insurancePP.logging import logger

from insurancePP.constants import *
from insurancePP.utils.common import read_yaml, create_directories, save_object, load_object, evaluate_models
from insurancePP.entity import ModelTrainingConfig

from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor


class ModelTraining:
    def __init__(self, config : ModelTrainingConfig):
        self.config = config
    

    def initiate_model_trainer(self):
        try:
            logger.info("loading the training and testing data")
            train_arr = load(self.config.prepared_train_data)
            test_arr = load(self.config.prepared_test_data)

            logger.info("spliting the training and testing data")
            X_train, y_train, X_test, y_test = (
                train_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, :-1],
                test_arr[:, -1],
            )

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            params={
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                },
                "Random Forest":{
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Gradient Boosting":{
                    # 'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "XGBRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "CatBoosting Regressor":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    'n_estimators': [8,16,32,64,128,256]
                }
            }

            
            model_report : dict = evaluate_models(X_train, y_train, X_test, y_test, models, params)
         
            performance_df = pd.DataFrame(list(zip(model_report.keys(), model_report.values())), columns=['Model Name', 'R2_Score']).sort_values(by=["R2_Score"],ascending=False)
            logger.info(f'Model Report: \n {performance_df}')

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            # if best_model_score < 0.6:
            #     raise e
            # logging.info(f"Best model found on both training and testing dataset")
    
            save_object(
                file_path = Path(self.config.model_path),
                obj = best_model
            )

            predict = best_model.predict(X_test)
            r2 = r2_score(y_test, predict)
            

        except Exception as e:
            raise e