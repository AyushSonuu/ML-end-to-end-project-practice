from setuptools import setup, find_packages
from typing import List  


PROJECT_NAME= "housing-predictor"
VERSION ='0.0.1'
AUTHOR = "ayush"
DESCRIPTION = "THIS IS MY FIRST END TO END PROJECT"
REQUIREMENT_FILE_NAME ="requirements.txt"
# PACKAGES = ["housing"]


def get_requirements_list()->List[str]:
    '''description : this is going to return list of requirements
    mentioned in requiremnts.txt fie
    
    return this function is going to return list oof the name of iberaries mantioned in requirements.txt
    '''
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        a = requirement_file.readlines()
        a.pop(-1)
        return a

setup(
    name =PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description= DESCRIPTION,
    packages= find_packages(),
    install_requires = get_requirements_list()
)