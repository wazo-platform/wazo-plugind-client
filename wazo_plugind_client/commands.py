# -*- coding: utf-8 -*-
# Copyright 2017-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client import RESTCommand


class MarketCommand(RESTCommand):

    resource = 'market'

    def get(self, namespace, name):
        headers = self._get_headers()
        url = '{}/{}/{}'.format(self.base_url, namespace, name)
        r = self.session.get(url, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def list(self, *args, **kwargs):
        params = dict(kwargs)
        if args:
            params['search'] = args[0]

        headers = self._get_headers()
        r = self.session.get(self.base_url, params=params, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()


class PluginCommand(RESTCommand):

    resource = 'plugins'

    def get(self, namespace, name):
        headers = self._get_headers()
        url = '{}/{}/{}'.format(self.base_url, namespace, name)
        r = self.session.get(url, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def install(self, url=None, method=None, options=None, **kwargs):
        data = {'method': method,
                'options': options or {}}

        query_string = {}
        if kwargs.get('reinstall'):
            query_string['reinstall'] = True

        if url:
            data['options']['url'] = url

        headers = self._get_headers()
        r = self.session.post(
            self.base_url,
            headers=headers,
            params=query_string,
            json=data,
        )

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def list(self):
        headers = self._get_headers()
        r = self.session.get(self.base_url, headers=headers)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def uninstall(self, namespace, name):
        headers = self._get_headers()
        url = '{base_url}/{namespace}/{name}'.format(
            base_url=self.base_url,
            namespace=namespace,
            name=name,
        )
        r = self.session.delete(url, headers=headers)

        if r.status_code != 204:
            self.raise_from_response(r)

        return r.json()


class ConfigCommand(RESTCommand):

    resource = 'config'

    def get(self):
        headers = self._get_headers()
        r = self.session.get(self.base_url, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
