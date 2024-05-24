#!/usr/bin/env python3
from setuptools import setup, find_packages
from subprocess import run, PIPE
from sys import version_info, stderr
from setuptools import setup
from pkg_resources import require
from sys import argv

NAME: str = "tharos-pytools"
AUTHOR: str = "Tharos",
AUTHOR_EMAIL: str = "dubois.siegfried@gmail.com",
LICENCE: str = "LICENCE"
DESCRIPTION: str = "Collection of quality-of-life functions"
REQUIRED_PYTHON: tuple = (3, 10)
OVERRIDE_VN: bool = True
VN: str = "0.0.32"
URL: str = "https://github.com/Tharos-ux/tharos-pytools"
REQUIREMENTS: list[str] = [
    'mycolorpy>=1.5.1',
    'matplotlib>=3.9.0',
    'rich>=13.7.1'
]


if argv[1] in ('install', 'sdist', 'bdist_wheel'):
    # Checking if Python version is correct
    if version_info[:2] < REQUIRED_PYTHON:
        stderr.write(
            f"{NAME} requires Python {'.'.join(REQUIRED_PYTHON)} or higher and your current version is {version_info[:2]}.")
        exit(1)

    # Computing version number
    if OVERRIDE_VN:
        _iv: str = VN
    else:
        try:
            _iv: list = [int(x) for x in require(NAME)[0].version.split('.')]
            _iv[-1] += 1
        except:
            _iv: list = [int(x) for x in VN.split('.')]
        finally:
            _iv: str = '.'.join([str(x) for x in _iv])

    _sb, _eb = "{", "}"
    with open('pyproject.toml', 'w', encoding='utf-8') as tomlwriter:
        tomlwriter.write(
            f"""[build-system]
    requires = ["setuptools>=61.0"]
    build-backend = "setuptools.build_meta"

    [project]
    name = "{NAME}"
    version = "{_iv}"
    authors = [
    {_sb} name="{AUTHOR[0]}", email="{AUTHOR_EMAIL[0]}" {_eb},
    ]
    description = "{DESCRIPTION}"
    readme = "README.md"
    requires-python = ">={'.'.join([str(x) for x in REQUIRED_PYTHON])}"
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

    [project.urls]
    "Homepage" = "{URL}"
    "Bug Tracker" = "{URL}/issues"
    """
        )
else:
    _iv: str = VN if OVERRIDE_VN else require(NAME)[0].version

# Install procedure
setup(
    name=NAME,
    version=_iv,
    description=DESCRIPTION,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    zip_safe=False,
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type='text/markdown',
)
