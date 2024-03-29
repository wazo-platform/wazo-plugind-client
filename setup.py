#!/usr/bin/env python3
# Copyright 2017-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import find_packages, setup

setup(
    name='wazo_plugind_client',
    version='0.2',
    description='a simple client library for the wazo-plugind HTTP interface',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo.community',
    packages=find_packages(),
    entry_points={
        'wazo_plugind_client.commands': [
            'config = wazo_plugind_client.commands:ConfigCommand',
            'market = wazo_plugind_client.commands:MarketCommand',
            'plugins = wazo_plugind_client.commands:PluginCommand',
            'status = wazo_plugind_client.commands:StatusCheckerCommand',
        ],
    },
)
