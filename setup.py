from setuptools import setup
from typing import List  


PROJECT_NAME= "housing-predictor"
VERSION ='0.0.1'
AUTHOR = "ayush"
DESCRIPTION = "THIS IS MY FIRST END TO END PROJECT"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME ="requirements.txt"


def get_requirements_list()->List[str]:
    '''description : this is going to return list of requirements
    mentioned in requiremnts.txt fie
    
    return this function is going to return list oof the name of iberaries mantioned in requirements.txt
    '''
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name =PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description= DESCRIPTION,
    packages= PACKAGES,
    install_requires = get_requirements_list()
)