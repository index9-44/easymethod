#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: yizhang
# Mail: 944057541@qq.com
# Created Time:  2021-1-13 21:17:34
#############################################


from setuptools import setup, find_packages

setup(
    name = "easymethod",
    version = "0.1.1",
    keywords = ("pip", "pathtool","timetool", "magetool", "mage"),
    description = "easy to use method",
    long_description = "easy!!!",
    license = "MIT Licence",

    url = "https://github.com/index9-44/easymethod.git",
    author = "yizhang",
    author_email = "944057541@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)