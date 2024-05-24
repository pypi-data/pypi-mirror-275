# Author: Kenta Nakamura <c60evaporator@gmail.com>
# Copyright (c) 2020-2021 Kenta Nakamura
# License: BSD 3 clause

from setuptools import setup, find_packages
import echo_assigner

DESCRIPTION = "EchoAssiger: Automatically composes accompaniment to a melody midi consisting of a single note"
NAME = 'echo_assigner'
AUTHOR = 'Ryosuke Saiki'
AUTHOR_EMAIL = 'ryosuke3191@gmail.com'
URL = 'https://github.com/pdmuds4/EchoAssigner.git'
LICENSE = 'Creative Commons Legal Code'
VERSION = echo_assigner.__version__
PYTHON_REQUIRES = ">=3.10"

INSTALL_REQUIRES = [
    'midi2audio',
    'mido',
    'music21',
    'numpy',
    'pandas',
    'scipy',
    'keras',
    'keras-metrics',
    'tensorflow',
    'tqdm',
    'samplings'
]

PACKAGES = find_packages()

setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    packages=PACKAGES,
    package_data={
        'echo_assigner': 
            [
            'database/*.sqlite',
            'database/sample/*.mid'
            ]
    },
)
