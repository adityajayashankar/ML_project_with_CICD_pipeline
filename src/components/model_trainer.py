import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from numpy import e
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
) 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join("artifacts","model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            logging.info("Splitting training and Testing input data")
            x_train, y_train, x_test, y_test = (

                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
                ) 
            
            models = {
                "Linear Regression": LinearRegression(),
                "Decision Tree Regressor": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "Gradient Boosting Regressor": GradientBoostingRegressor(),
                "XGBoost Regressor": XGBRegressor(),
                "CatBoost Regressor": CatBoostRegressor(verbose=0),
                "AdaBoost Regressor": AdaBoostRegressor(),
                "K-Neighbors Regressor": KNeighborsRegressor()
            }
            params = {
                "Linear Regression": {},
                "Decision Tree Regressor": {"max_depth": [3, 5, 7, 10]},
                "Random Forest Regressor": {"n_estimators": [50, 100, 200]},
                "Gradient Boosting Regressor": {"learning_rate": [0.01, 0.1, 0.2]},
                "XGBoost Regressor": {"n_estimators": [50, 100], "learning_rate": [0.01, 0.1]},
                "CatBoost Regressor": {"depth": [3, 5, 7], "learning_rate": [0.01, 0.1]},
                "AdaBoost Regressor": {"n_estimators": [50, 100]},
                "K-Neighbors Regressor": {"n_neighbors": [3, 5, 7]}
            }
            model_report: dict = evaluate_models(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,
                                                models=models,params=params)
            best_model_score = max([value[0] for value in model_report.values()])
            best_model_name = [key for key, value in model_report.items() if value[0] == best_model_score][0]

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found with sufficient accuracy")
            logging.info(f"Best model found: {best_model_name} with score: {best_model_score}")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(x_test)
            r2_square = r2_score(y_test, predicted)
            return r2_square
            
        except Exception as e:
            raise CustomException(e, sys)
          