#!/usr/bin/env python3
"""
Euroscope Sweatbox Scenario Maker

Copyright (C) 2019  Pedro Rodrigues <prodrigues1990@gmail.com>
                    Tiago Vicente <tmavicente@gmail.com>

This file is part of Euroscope Sweatbox Scenario Maker.

Euroscope Sweatbox Scenario Maker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

Euroscope Sweatbox Scenario Maker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Euroscope Sweatbox Scenario Maker. If not, see <http://www.gnu.org/licenses/>.
"""
from setuptools import setup, find_packages

setup(
  name='es-scenario-maker',
  version='0.1',
  py_modules=['esmake'],
  packages=find_packages(),
  install_requires=['Click'],
  entry_points='''
    [console_scripts]
    esmake=esmake:main
  '''
)
