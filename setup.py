#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name="17MonIP",
    version="0.1.0",
    description="IP search based on 17mon.cn, the best IP database for China.",
    author="Lx Yu",
    author_email="github@lxyu.net",
    packages=["IP", ],
    package_data={'IP': ['17monipdb.dat'], },
    entry_points={"console_scripts": ["ip = ip.cmd:ip", ]},
    url="http://lxyu.github.io/17monip/",
    license="MIT",
    long_description=open("README.rst").read(),
)
