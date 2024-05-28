from setuptools import setup, find_packages

setup(
    name='pyexmars',
    version='1.0.11',
    packages=find_packages(),
    package_data={'': ['*.pyc']},
    include_package_data=True,
    # 추가 메타데이터 및 의존성 정보 작성
)