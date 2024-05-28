# -*- coding: utf-8 -*-
"""
Created on Sat May  4 18:12:55 2024

@author: atdou
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
	read_me = fh.read()

setup(
      author ="Andrew Douglas",
      description = "Additional Tools for Machine Learning",
      long_description = read_me,
      long_description_content_type = "text/markdown",
      name = "XtraMLTools",
      version = "0.1.2",
      packages = find_packages(include = ["XtraMLTools", "XtraMLTools.*"]),
      install_requires = ["numpy", "pandas", "scipy", "scikit-learn", "xgboost", "matplotlib"],
  	  classifiers = ["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License"]
      )