#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from setuptools import setup
from setuptools import find_packages

setup(
    name='wazo_plugind_client',
    version='0.1',

    description='a simple client library for the wazo-plugind HTTP interface',

    author='Wazo Authors',
    author_email='dev@wazo.community',

    url='http://wazo.community',

    packages=find_packages(),

    entry_points={
        'plugind_client.commands': [
            'plugins = wazo_plugind_client.commands:PluginCommand',
        ],
    }
)
