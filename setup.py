#!/usr/bin/env python3
# coding=utf-8

from distutils.core import setup

version = '0.2'

setup(
    name='jefferson',
    version=version,
    description='',
    author='Stefan Viehböck',
    url='https://github.com/figbux/jefferson-py3',
    license='MIT',

    requires=['cstruct'],
    packages=['jefferson'],
    package_dir={'jefferson': 'src/jefferson'},
    scripts=['src/scripts/jefferson'],
)
