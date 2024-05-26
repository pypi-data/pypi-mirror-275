
import os, glob
from setuptools import setup, find_packages
from pypi_project.config import PACKAGE_NAME, COMMAND_NAME, PACKAGE_VERSION

def recursive(directory):
    file_patterns = os.path.join(directory, '**', '*')
    return [file for file in glob.glob(file_patterns, recursive=True)]

setup (
    name = PACKAGE_NAME, 
    version = PACKAGE_VERSION, 
    description = 'description', 
    long_description = open('README.md').read(), 
    long_description_content_type = 'text/markdown', 
    author = 'wukunhuan', 
    author_email = 'wukunhuan1208@163.com', 
    url = 'https://github.com/WuKunhuan163/PyPI-Project', 
    entry_points = {
        'console_scripts': [
            f'{COMMAND_NAME} = pypi_project.main:main'
        ]
    }, 
    project_urls = {
        "Source": "https://github.com/WuKunhuan163/PyPI-Project", 
    }, 
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires=">=3", 
    install_requires = [
        "argparse", 
    ], 
    package_data={
        
    }, 

)
