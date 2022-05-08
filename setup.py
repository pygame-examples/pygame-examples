"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

from setuptools import find_packages, setup

# py -m build
# twine upload dist/*
VERSION = "0.0.1"
DESCRIPTION = "A collection of pygame examples"
LONG_DESCRIPTION = """
A collection of pygame examples that support WASM, 
and can be run on desktop/browser and viewed on the browser.
"""

# Setup
setup(
    name="pgex",
    version=VERSION,
    author="Matiiss",
    email="-",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["pygame", "click"],
    python_requires=">=3.7",
    keywords=["cli", "examples"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Games/Entertainment",
        "Intended Audience :: Developers",
    ],
    entry_points={"console_scripts": ["pgex=pgex:main"]},
)
