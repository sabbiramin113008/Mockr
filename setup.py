# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 15 Oct 2019
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

from setuptools import setup

setup(
    name='mockr',
    author='S.M. Sabbir Amin',
    author_email='<sabbiramin.cse11ruet@gmail.com>,<sabbir@rokomari.com',
    version='0.8.0',
    description='A RESTful Mock Server Generator',
    packages=["mockr"],
    entry_points={"console_scripts": ["mockr = mockr.__main__:main"]},
    license='GNU GPL v3 or later',
    install_requires=[
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
