#!/usr/bin/env python

import setuptools


setuptools.setup(
    name='netstatd-engine',
    version='0.1',
    description='netstatd engine',
    author='NetstatD',
    author_email='netstatd@gmail.com',
    packages=['netstatd_engine',
              'netstatd_engine.api',
              'netstatd_engine.common'],
    entry_points={
        'console_scripts': [
            'netstatd-engine=netstatd_engine.netstatd_engine_server:main'
        ]
    }
)
