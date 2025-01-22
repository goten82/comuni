
from setuptools import setup, find_packages

setup(
    name="comuni",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "pandas>=1.2.0",
        "numpy>=1.19.0",
        "beautifulsoup4>=4.9.3",
        "lxml>=4.6.0",
        "setuptools>=70.0.0"
    ],
    author="Giuseppe Ninniri",
    author_email="goten.ninniri@gmail.com",
    description="A package for working with Italian municipality data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sourcegraph/comuni",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
