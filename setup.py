# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

install_requires = [
    'docker-py==1.3.1',
    'nose==1.3.7'
]

tests_require = [
]

setup(
    name="twarm",
    version='0.0.1',
    description="Event-driven Postgres client library",
    author="Liam Costello",
    author_email="liam@lolletsoc.com",
    url="https://github.com/lolletsoc/twarm",
    install_requires=install_requires,
    packages=find_packages(),
    classifiers=[],
    zip_safe=False,
    entry_points={
        'nose.plugins': [
            'twarm = nosetwarm:Twarm'
        ]
    },
)
