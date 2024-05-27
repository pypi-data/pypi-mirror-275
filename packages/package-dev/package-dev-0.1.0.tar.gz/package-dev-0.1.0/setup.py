
from setuptools import setup, find_packages

setup(
    name='package-dev',
    version='0.1.0',
    author='sravs',
    author_email='sravanthi23.2001@gmail.com',
    description='A simple package with basic functions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sravanthi69/package-dev',  # Replace with your GitHub repository URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
