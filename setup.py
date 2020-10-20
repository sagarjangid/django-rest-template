#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='service',
    version='1.0',
    description="",
    author="",
    author_email='',
    url='',
    packages=find_packages(),
    package_data={'service': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)
