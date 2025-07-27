import os
from box.exceptions import BoxValueError
import yaml
from CNN_classifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
    
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates list of directories
    
    Args:
        path_to_dirs (list): List of paths of directories
        ignore_log (bool, optional): Ignore if multiple dirs is to be created. Defaults to false
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")

@ensure_annotations
def save_json(path:Path, data: dict):
    """
    Saves JSON Data
    
    Args:
        path (Path): Path to save the JSON file.
        data (dict): Data to be saved in JSON format.
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"JSON file saved at {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads JSON Data
    
    Args:
        path (Path): Path to the JSON file.
    
    Returns:
        ConfigBox: data as class atrtibute insteda of dict
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded from {path}")
    return content

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())


