import os
from setuptools import setup, find_packages

def readme():
    with open('README_en.md', encoding='utf-8') as f:
        return f.read()

def get_req():
    if "PYODIDE" in os.environ:
        return ['mdutils', "numpy", "matplotlib",]
    else:
        return ['mdutils', "numpy", "matplotlib",]

setup(
    name='mapieng',
    version='0.1.9',
    packages=find_packages(),
    include_package_data=True,
    description='mapi engineers',
    long_description=readme(),
    long_description_content_type='text/markdown',
    license='MIT',
    author='bschoi',
    url='https://github.com/MIDASIT-Co-Ltd/engineers-api-python',
    install_requires=['mdutils', "numpy", "matplotlib",],
    )