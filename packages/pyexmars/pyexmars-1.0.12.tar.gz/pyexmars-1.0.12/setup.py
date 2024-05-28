from setuptools import setup, find_packages

setup(
    name='pyexmars',
    version='1.0.12',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'pyexmars': ['*.pyc'],
    },
    zip_safe=False,
)
