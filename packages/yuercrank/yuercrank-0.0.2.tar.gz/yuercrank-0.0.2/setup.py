from setuptools import setup, find_packages
from os import path
working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='yuercrank',
    version='0.0.2',
    author='The Urban Penguin',
    author_email='crank3729@gmail.com',
    description='Simple package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=["telebot"],
)