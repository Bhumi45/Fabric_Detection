import os
import sys
import yaml
import json
import joblib
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
from box import ConfigBox
from exception import CustomException
from logger import logging
import shutil


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns the content as a ConfigBox object.
    The ConfigBox is a special type of dictionary that allows you to use the keys as attributes.
    :param path_to_yaml: Path to the yaml file
    :return: ConfigBox object
    :raises CustomException: If the yaml file is not readable or if the content is not a dict
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file) # This will be loaded as a dict
            logging.info(f"yaml file: {path_to_yaml} loaded successfully as {type(content)}")
            return ConfigBox(content) # converting the dict to ConfigBox to use the keys as attributes
    except CustomException as e:
        raise CustomException(e, sys) 
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates a list of directories at the given paths.
    :param path_to_directories: List of paths to create the directories
    :param verbose: Whether to log the creation of directories
    :return: None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a given dictionary to a json file at the given path.
    :param path: Path to the json file
    :param data: Dictionary to be saved
    :return: None
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a json file and returns the content as a ConfigBox object.
    :param path: Path to the json file
    :return: ConfigBox object
    """
    with open(path) as f:
        content = json.load(f)  # This will be loaded as a dict
    
    logging.info(f"json file loaded successfully")
    return ConfigBox(content) # converting the dict to ConfigBox to use the keys as attributes

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves a given object to a binary file at the given path.
    :param data: Any object to be saved
    :param path: Path to the binary file
    :return: None
    """
    joblib.dump(value=data, filename=path)
    logging.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads a binary file and returns the content as an object.
    :param path: Path to the binary file
    :return: Loaded object
    """
    data = joblib.load(path)
    logging.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of the file in GB.
    :param path: Path to the file
    :return: Size of the file in GB as a string
    """
    size_in_gb = round(os.path.getsize(path)/(1024 ** 3), 2)
    return f"{size_in_gb} GB"


import os

def delete_artifacts_folder():
    folder_path = 'artifacts_deployment'

    try:
        # Check if the folder exists
        if os.path.exists(folder_path):
            # Remove the folder and all its contents
            shutil.rmtree(folder_path)
            print(f"Deleted the folder: {folder_path}")
        else:
            print(f"Folder not found: {folder_path}")
    except Exception as e:
        raise CustomException(e,sys)