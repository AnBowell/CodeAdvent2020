# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 18:28:25 2020

@author: Andrew
"""
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("DayTwoCython.pyx", annotate=True)
)