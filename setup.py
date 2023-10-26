# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

import codecs
import os
import versioneer

from setuptools import find_packages, setup

def read(*parts):
    """
    Build an absolute path from C{parts} and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *parts), 'r', 'utf-8') as f:
        return f.read()

with open("README.rst") as f:
    long_description = f.read()

if __name__ == "__main__":
    setup(
        classifiers=[
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3 :: Only',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
        description="Symbolic constants in Python",
        long_description=long_description,
        keywords="constants,enum,twisted",
        license="MIT",
        name="constantly",
        packages=find_packages(),
        url="https://github.com/twisted/constantly",
        maintainer='Twisted Matrix Labs Developers',
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        python_requires=">= 3.8",
    )
