from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Creating dividers (divs) for CLI or output files'
with open("README.md", "r") as fh:
    long_description = fh.read()

# Setting up
setup(
    name="Dividers",
    version=VERSION,
    author="Burritoless Codec",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'dividers', 'cli', 'output'],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
