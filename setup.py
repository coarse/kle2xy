#!/usr/bin/env python
# Special thanks to Hynek Schlawack for providing excellent documentation:
#
# https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
import os
from setuptools import setup, find_packages, Command


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(
    name='kle2xy',
    version='0.0.1',
    description='Library for turning keyboard-layout-editor.com raw code into X/Y coordinates',
    long_description='\n\n'.join((read('README.md'), read('AUTHORS.md'))),
    url='https://github.com/skullydazed/kb_builder',
    license='all_rights_reserved',
    author='skullY',
    author_email='skullydazed@gmail.com',
    install_requires=['hjson'],
    py_modules=['kle2xy'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: Restrictive',
        'Topic :: System :: Systems Administration',
    ],
)
