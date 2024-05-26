#! /usr/bin/env python3

import sys
import os

from setuptools import setup

setup(
    name='pyspimdbg',
    version='0.2',
    url='https://github.com/Gabrain24/pyspimdbg',
    author='Gabrain24', # (forked from pyspim by Jason Yosinski)'
    py_modules=['pyspimdbg'],
    install_requires=[
        'pexpect',
    ],
    entry_points={
        'console_scripts': [
            'pyspimdbg=pyspimdbg:main',
        ],
    },
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)

print('Looking for dependency: spim...', end='')
sys.stdout.flush()
if os.system('which spim > /dev/null') == 0:
    print('found.')
else:
    print('not found.')
    print('\nERROR: spim is required before using pyspim. You can get it here:')
    print('    http://sourceforge.net/projects/spimsimulator/')

print('Checking for dependency: pexpect module...', end='')
sys.stdout.flush()
try:
    import pexpect
    print('found.')    
except ImportError:
    print('not found.')
    print('\nERROR: The pexpect module is required by pyspim. Install via')
    print('    sudo pip install pexpect')
    print('or by downloading it directly from http://sourceforge.net/projects/pexpect/')