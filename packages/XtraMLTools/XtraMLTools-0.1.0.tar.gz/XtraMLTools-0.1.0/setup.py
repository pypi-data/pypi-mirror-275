# -*- coding: utf-8 -*-
"""
Created on Sat May  4 18:12:55 2024

@author: atdou
"""

from setuptools import setup, find_packages

setup(
      author ="Andrew Douglas",
      description = "Additional Tools for MAchine Learning",
      name = "XtraMLTools",
      version = "0.1.0",
      packages = find_packages(include = ["XtraMLTools", "XtraMLTools.*"]))

