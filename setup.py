#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mindstorms_tools",
    description="Python LEGO Mindstorms tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brean/mindstorms_tools",
    version="0.0.1",
    license="Apache2",
    author="Andreas Bresser",
    packages=find_packages(),
    tests_require=["serial"],
    include_package_data=True,
    install_requires=[],
)
