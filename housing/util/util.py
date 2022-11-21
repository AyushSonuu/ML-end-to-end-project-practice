import yaml
from housing.exception import HousingException
from housing.constant import *
import sys,os


def read_yaml_file(file_path:str)-> dict:
    """reads a yaml file and returns thecontent as dictionary
    file_path: str"""

    try:
        with open (file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e