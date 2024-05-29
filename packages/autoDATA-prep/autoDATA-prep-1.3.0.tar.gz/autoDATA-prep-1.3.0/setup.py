from setuptools import setup, find_packages
import os

# Read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='autoDATA-prep',
    version='1.3.0',
    description='Data pre-processing library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Emmanuel Ezenwere',
    author_email='emmaezenwere@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['assets/data-preprocessing-cover.png'],
    },
    zip_safe=False
)
