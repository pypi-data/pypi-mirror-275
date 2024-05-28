from setuptools import setup, find_packages
import os

# Read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='org-ds-cdk',
    version='0.1.11',
    description='DS Organization CDK Constructs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(include=['cdk_main.*']),  # This line is changed
    package_dir={'': '.'},  # This line is changed
    include_package_data=True,  # This line is added
    install_requires=[
        'aws-cdk-lib==2.143.0',
        'constructs>=10.0.0'
    ],
)