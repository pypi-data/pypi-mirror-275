from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='super-ec2',
    version='0.0.0.1',
    packages=['super-ec2'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
    