# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='tonton-bot',
    version='0.2',
    description='Small irc bot using Twisted',
    long_description=readme,
    author='Tonton duPirox',
    author_email='onclebobs@gmail.com',
    url='https://github.com/tontonDuPirox/tonton-bot',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

