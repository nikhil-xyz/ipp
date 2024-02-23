import os
from box.exceptions import BoxValueError
import yaml
from insurancePP.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


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