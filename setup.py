#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

with open('README.md') as readme:
    long_description = readme.read()

with open('requirements.txt') as requirements:
    lines = requirements.readlines()
    libraries = [lib for lib in lines if not lib.startswith('-')]
    dependency_links = [link.split()[1] for link in lines if
                        link.startswith('-f')]

setup(
    name='pyromarc-template',
    version='1.0.0',
    author='morganbohn',
    author_email='morgan.bohn@unistra.fr',
    maintainer='morganbohn',
    maintainer_email='morgan.bohn@unistra.fr',
    url='https://github.com/morganbohn/pyromarc-template',
    license='PSF',
    description='Templating system for pyromarc',
    long_description=long_description,
    packages=find_packages(),
    download_url='https://github.com/morganbohn/pyromarc-template',
    install_requires=libraries,
    dependency_links=dependency_links,
    keywords=['pyromarc', 'mir', 'yaml', 'template'],
    entry_points={},
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3'
    )
)
