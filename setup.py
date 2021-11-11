#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="socpy",
    version="0.0.5",
    author="Daniel Molitor",
    author_email="molitdj97@gmail.com",
    description="Query the SOCcer API",
    long_description=long_description,
    url="https://github.com/dmolitor/socpy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "pandas",
        "requests",
        "setuptools"
    ],
    include_package_data=True,
    package_data={"": ["data/*.csv"]},
    python_requires=">=3.6",
)