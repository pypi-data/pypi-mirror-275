from setuptools import setup, find_packages

setup(
    name='pyexmars',
    version='0.0.1',
    packages=['pyexmars'],
    package_data={'pyexmars': ['*.py']},
    include_package_data=True,
    # 추가 메타데이터 및 의존성 정보 작성
)