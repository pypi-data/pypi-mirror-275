# setup.py

from setuptools import setup, find_packages

setup(
    name='fraction_package',
    version='0.1',
    packages=find_packages(),
    description='A simple fraction data type',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Gokul',
    author_email='gokul1357@gmail.com',
    url='https://github.com/greetcat/Fractions',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
