#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup for the Graphite Eagle.

Source:: https://github.com/ampledata/graphiteeagle
"""

import os
import sys
import setuptools

__title__ = 'graphiteeagle'
__version__ = '0.0.1b2'
__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Apache License, Version 2.0'


def publish():
    """Function for publishing package to pypi."""
    if sys.argv[-1] == 'publish':
        os.system('python setup.py sdist')
        os.system('twine upload dist/*')
        sys.exit()


publish()


setuptools.setup(
    name=__title__,
    version=__version__,
    description='Graphite Eagle.',
    author='Greg Albrecht',
    author_email='oss@undef.net',
    packages=['graphiteeagle'],
    package_data={'': ['LICENSE']},
    package_dir={'graphiteeagle': 'graphiteeagle'},
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
    url='https://github.com/ampledata/graphiteeagle',
    zip_safe=False,
    include_package_data=True,
    entry_points={'console_scripts': ['graphiteeagle = graphiteeagle.cmd:cli']}
)
