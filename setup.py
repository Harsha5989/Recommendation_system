from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from the given file path.
    It removes any '-e .' entry and strips whitespace from each line.
    """    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements


setup(
    name="my_package",
    version="0.1",
    author="Harsha",
    author_email="harshagowda5989@gmail.com",
    packages=find_packages(),
    install_requires=[get_requirements('requirement.txt')]
    )