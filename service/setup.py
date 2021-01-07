#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages


setup(
    author="Jason Guiditta",
    author_email='jguiditt@redhat.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    description=("RTLS, or Real Time Locator System, is an abstraction layer "
                 "for tracking changes to code through their lifecycle"),
    entry_points={},
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_restful',
        'gunicorn',
    ],
    license="MIT license",
    name='rtls',
    packages=find_packages(include=['rtls']),
    tests_require=[
        'pytest'
    ],
    url='https://github.com/release-depot/rtls',
    version='0.0.1',
    zip_safe=False,
)
