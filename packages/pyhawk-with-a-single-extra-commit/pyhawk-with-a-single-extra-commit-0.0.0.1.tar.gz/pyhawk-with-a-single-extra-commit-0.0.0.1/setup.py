from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='pyhawk-with-a-single-extra-commit',
    version='0.0.0.1',
    packages=['pyhawk-with-a-single-extra-commit'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
    