import os
from box.exceptions import BoxValueError
import yaml
from insurancePP.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import pickle

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read yaml file and returns
    Args: 
        path_to_yaml (Path): path to the yaml file
    Raises:
        ValueError : if yaml file is empty
        e : empty file

    Returns : 
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories : list, verbose=True):
    """create directories
    Args: 
        path_to_directories (list): list of paths to directories
        verbose (bool): if True, print the directory creation
    """

    for directory in path_to_directories:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logger.info(f"directory {directory} created")

@ensure_annotations
def get_size(path: Path) -> str:
    """get size of a file
    Args: 
        path (Path): path to the file
    Returns : 
        str: size of the file
    """
    return f"~ {round(os.path.getsize(path)/1024)} KB"


@ensure_annotations
def save_object(file_path, obj):
    try:
    
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
      
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
        logger.info('Binary Object is stored')

    except Exception as e:
        raise e

@ensure_annotations
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise e


def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}
  
        for i in range(len(list(models))):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]
          
            gs = GridSearchCV(model, param, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score
        return report

    except Exception as e:
        raise e