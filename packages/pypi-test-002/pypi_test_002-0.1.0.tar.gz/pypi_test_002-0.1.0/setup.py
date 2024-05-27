
import os, glob
from setuptools import setup, find_packages
from pypi_test_002.config import pypi_PACKAGE_NAME, pypi_PACKAGE_VERSION, pypi_DATA_PATH, pypi_COMMAND_NAME
from pypi_test_002.config import pypi_PACKAGE_AUTHOR_NAME, pypi_PACKAGE_AUTHOR_EMAIL, pypi_PACKAGE_WEBSITE

# Retrieval of current directory and sub directories
def recursive(directory):
    file_patterns = os.path.join(directory, '**', '*')
    return [file for file in glob.glob(file_patterns, recursive=True)]

# Create the data folder of the package
os.makedirs(pypi_DATA_PATH, exist_ok=True)

setup (
    name = pypi_PACKAGE_NAME, 
    version = pypi_PACKAGE_VERSION, 
    description = f'Description of the {pypi_PACKAGE_NAME} package. ', 
    long_description = open('README.md').read(), 
    long_description_content_type = 'text/markdown', 
    author = pypi_PACKAGE_AUTHOR_NAME, 
    author_email = pypi_PACKAGE_AUTHOR_EMAIL, 
    entry_points = {
        'console_scripts': [
            f'{pypi_COMMAND_NAME} = {pypi_PACKAGE_NAME}.main:main'
        ]
    }, 
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires=">=3.8", 
    install_requires = [
        "argparse", 
    ], 
    package_data={
        pypi_PACKAGE_NAME: recursive(pypi_DATA_PATH)
    }, 

)

