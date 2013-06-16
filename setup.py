#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Python Package for Scientific Constants, Universals and Functions',
	'author': 'Anthony Nystrom',
	'url': 'https://github.com/AnthonyNystrom/PyNuGenSci',
	'download_url': 'https://github.com/AnthonyNystrom/PyNuGenSci',
	'author_email': 'nystrom.anthony@gmail.com',
	'verion': '0.1',
	'install_requires': ['nose'],
	'packages': ['PyNuGenSci'],
	'scripts': [],
	'name': 'PyNuGenSci'
}

setup(**config)
