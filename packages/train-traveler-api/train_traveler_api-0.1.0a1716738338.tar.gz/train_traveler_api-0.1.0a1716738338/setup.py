from setuptools import setup, find_packages
from datetime import datetime

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="train-traveler-api",
    version=f"0.1.0-alpha.{int(round(datetime.timestamp(datetime.now())))}",
    author="Matthieu DURINDEL",
    description="Train traveler is a backend for SNCF API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/Matthyeux/train-traveler-api",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'train-traveler=sncf.train_traveler:main',
        ],
    }
)