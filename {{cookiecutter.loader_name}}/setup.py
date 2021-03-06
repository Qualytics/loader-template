#!/usr/bin/env python
from setuptools import setup

setup(
    name="{{cookiecutter.loader_name}}",
    version="0.1.0",
    description="Meltano loader for extracting data",
    author="{{cookiecutter.author_name}}",
    url="",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["{{cookiecutter.package_name}}"],
    install_requires=[
        "singer-python>=5.0.12",
        'jsonschema==2.6.0',
    ],
    entry_points="""
    [console_scripts]
    {{cookiecutter.loader_name}}={{cookiecutter.package_name}}:main
    """,
    packages=["{{cookiecutter.package_name}}"],
    package_data = {},
    include_package_data=True,
)
