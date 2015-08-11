# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

import codecs
import os
import versioneer

from setuptools import setup

def read(*parts):
    """
    Build an absolute path from C{parts} and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *parts), 'r', 'utf-8') as f:
        return f.read()

if __name__ == "__main__":
    setup(
        classifiers=[
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
        description="Symbolic constants in Python",
        long_description=read('README.rst'),
        keywords="constants,enum,twisted",
        license="MIT",
        name="constantly",
        packages=["constantly"],
        url="https://github.com/twisted/constantly",
        maintainer='Twisted Matrix Labs Developers',
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
    )
