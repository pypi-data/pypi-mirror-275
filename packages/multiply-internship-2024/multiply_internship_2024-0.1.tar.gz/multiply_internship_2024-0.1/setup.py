from setuptools import setup, find_packages
from os import path

# Directory containing this file
HERE = path.abspath(path.dirname(__file__))

# The text of the README file
with open(path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="multiply_internship_2024",
    version="0.1",
    description="Description of your package",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Abdallah Abdelsameia",
    author_email="aabdelsameia1@gmail.com",
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        # List your project's dependencies here.
        # Example: 'requests>=2.20.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)