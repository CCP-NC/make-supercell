#!/usr/bin/env python
"""
make-supercell - A quick helper script to make supercells of structure files
with ASE
"""

# Python 2-to-3 compatibility code
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
# The next line is removed because it causes issues in interpreting
# the package_data line, unfortunately
# from __future__ import unicode_literals

from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(name='make-supercell',
          version='0.5',
          description='A quick helper script to make supercells of structure'
          ' files with ASE',
          url='https://github.com/CCP-NC/make-supercell',
          author='Simone Sturniolo',
          author_email='simone.sturniolo@stfc.ac.uk',
          license='MIT',
          classifiers=[
              # How mature is this project? Common values are
              #   3 - Alpha
              #   4 - Beta
              #   5 - Production/Stable
              'Development Status :: 4 - Beta',

              # Indicate who your project is intended for
              'Intended Audience :: Science/Research',
              'Topic :: Scientific/Engineering :: Chemistry',
              'Topic :: Scientific/Engineering :: Physics',

              # Pick your license as you wish (should match "license" above)
              'License :: OSI Approved :: MIT License',

              # Specify the Python versions you support here. In particular, ensure
              # that you indicate whether you support Python 2, Python 3 or
              # both.
              'Programming Language :: Python :: 2',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3',
          ],
          keywords='crystallography ccpnc computational chemistry',
          # For scripts - just put the paths
          scripts=['make-supercell.py'],
          # Requirements
          install_requires=[
              'numpy',
              'scipy',
              'ase'
          ],
          python_requires='>=2.7'
          )
