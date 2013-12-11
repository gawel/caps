# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages

version = '0.1.dev0'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name='caps',
    version=version,
    description="caps package",
    long_description=read('README.rst'),
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='',
    author='Gael Pasgrimaud',
    author_email='gael@gawel.org',
    url='https://github.com/gawel/caps/',
    license='MIT',
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    extras_require={
        'test': [
            'nose', 'webtest', 'coverage', 'coveralls',
        ],
    },
    entry_points="""
    [console_scripts]
    caps = caps.scripts:main
    """,
)
