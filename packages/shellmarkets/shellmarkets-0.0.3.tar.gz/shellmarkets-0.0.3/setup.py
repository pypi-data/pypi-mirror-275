from os import path
from setuptools import setup, find_packages


VERSION= '0.0.3'
AUTHOR='Croketillo'
AUTHOR_EMAIL='croketillo@gmail.com'
CURR_PATH = "{}{}".format(path.abspath(path.dirname(__file__)), '/')
NAME='shellmarkets'
DESCRIPTION="A CLI tool for retrieving stock market information."
URL='https://github.com/croketillo/SHELLMARKETS'

from setuptools import setup, find_packages

setup(
    name="shellmarkets",
    version=VERSION,
    packages=find_packages(include=['modules', 'modules.*']),
    py_modules=['shmkt'],
    include_package_data=True,
    install_requires=[
        "click",
        "yfinance",
        "colorama",
    ],
    entry_points={
        "console_scripts": [
            "shmkt=shmkt:main",
        ],
    },
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url=URL,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Financial and Insurance Industry",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
)
