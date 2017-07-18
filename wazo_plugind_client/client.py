# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client.client import BaseClient


class PlugindClient(BaseClient):

    namespace = 'plugind_client.commands'

    def __init__(self, host, port=9503, version='0.2', **kwargs):
        super(PlugindClient, self).__init__(host=host, port=port, version=version, **kwargs)
