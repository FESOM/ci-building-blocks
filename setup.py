"""Example setup.py File

This assumes that your code is in a src folder, and you have a README.md file
in the root directory of your project. The find_packages function will
automatically discover packages in the src directory, and the package_dir
argument tells setuptools to look for packages starting in the src directory.

You can also include any data files in your package by setting
``include_package_data=True``. This will include all files that match the
patterns specified in MANIFEST.in.

The install_requires argument reads the list of requirements from a
``requirements.txt`` file in the root directory of your project, and installs
them automatically when your package is installed.

The if not line.startswith('#') condition is used to ignore any comments in the
``requirements.txt`` file.

"""
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my_package",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Short description of your package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        line.strip() for line in open("requirements.txt") if not line.startswith("#")
    ],
)
