from setuptools import setup, find_packages

setup(
    name='pyexmars',
    version='1.0.14',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.pyc'],
    },
    zip_safe=False,
)
