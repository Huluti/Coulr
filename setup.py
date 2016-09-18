#!/usr/bin/env python

from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name="Coulr",
      version="0.1",
      description="Coulr is a color box to help developers and designers.",
      author="Hugo Posnic",
      url="https://github.com/Huluti/Coulr",
      packages=["coulr"],
      install_requires=requirements,
     )
