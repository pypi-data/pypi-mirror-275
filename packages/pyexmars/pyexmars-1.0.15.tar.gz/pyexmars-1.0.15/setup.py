from setuptools import setup, find_packages

setup(
    name='pyexmars',
    version='1.0.15',
    author='Smartcubelabs',
    description='pyexmars library',
    packages=find_packages(),
    package_data={'pyexmars': ['*.pyc']},
)