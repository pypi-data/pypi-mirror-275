# -*- coding: utf-8 -*-

from sys import version_info

from setuptools import setup, find_packages

__version__ = '0.1.0'  # 版本号
requirements = open('requirements.txt').readlines()  # 依赖文件

if version_info < (3, 8, 0):
    raise SystemExit('Sorry! dqlib requires python 3.8.0 or later.')

setup(
    name='dqlib',
    description='',
    long_description='',
    license='',
    version=__version__,
    author='zbz',
    url='',
    packages=find_packages(exclude=["test"]),
    python_requires='>= 3.8.0',
    install_requires=requirements
)
