from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent

setup(
    long_description=this_directory.joinpath('README.md').read_text(),
    licensetext=this_directory.joinpath('LICENSE').read_text(),
)
