#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name='ChatTTS',
    version='0.0.2',
    description='next level TTS for Chat',
    # long_description='',
    author='2_NOISE',
    # author_email='lichenghai99@gmail.com',
    license='Apache License 2.0',
    #url='https://github.com/',
    #download_url='https://github.com/',
    packages=find_packages(),
    install_requires=['torch>=2.0.0']
)