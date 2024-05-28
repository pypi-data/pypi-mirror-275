#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

with open('./readme.md', "r", encoding='utf8') as fh:
    long_description = fh.read()

setup(
    name='single-ins',
    version="0.0.1",
    author="lcy",
    author_email="lichunyang_1@outlook.com",
    description="Single Instance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lichunown/single-ins",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    packages=find_packages(),
    data_files=[],
    install_requires=[
    ],

    zip_safe=False
)
