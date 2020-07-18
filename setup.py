#!/usr/bin/env python
from setuptools import setup
import sys
import os

version = '1.0.0'

long_description = open('README.md').read()

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='darbird',
    version=version,
    packages=['darbird'],
    description='Official Darbird Python SDK',
    data_files=[('', ['README.md'])],
    license='MIT',
    author='Darbird',
    install_requires=[
        'requests>=v2.18.4',
        'schema>=0.6.7'
    ],
    python_requires=">=2.7.10",
    author_email='developers@darbird.com',
    url='https://github.com/AfricasTalkingLtd/africastalking-python',
    download_url='https://codeload.github.com/AfricasTalkingLtd/africastalking-python/tar.gz/' + version,
    keywords='ussd voice sms mpesa card bank b2b b2c sender_id payments airtime darbird',
    classifiers=[],
    long_description=long_description,
    long_description_content_type='text/markdown'
)