#!/usr/bin/env python

from os.path import exists, join
from setuptools import setup, find_packages
import os
import platform

from sphinx.setup_command import BuildDoc
cmdclass = {'build_sphinx': BuildDoc}

SCRIPTS =[]

setup(
    name='tantan-examination',
    version=open('VERSION').read().strip(),
    author='David Koo',
    author_email='nuanguang.gu@intel.com',
    packages=find_packages(),
    cmdclass=cmdclass,
    command_options={
        'build_sphinx': {
            'project': ('setup.py', 'tantan-examination'),
            'version': ('setup.py', open('VERSION').read().strip()),
            'release': ('setup.py', open('VERSION').read().strip()),
            'source_dir': ('setup.py', 'docs/source'),
            'build_dir': ('setup.py', 'docs/build'),
        }
    },
    scripts=SCRIPTS,
    url='https://github.com/nuangua/tantan-examination',
    license='David Koo Reserved',
    description='tantan-examination',
    long_description=open('README.rst').read() if exists("README.rst") else "",
    include_package_data=True,
    # Any requirements here
    install_requires=[
        'setuptools',
        'Sphinx',
        'sphinx_rtd_theme'
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
)