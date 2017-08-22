# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_webhookd_client.command import WebhookdCommand


class SubscriptionsCommand(WebhookdCommand):

    resource = 'subscriptions'
    _ro_headers = {'Accept': 'application/json'}
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def create(self, subscription):
        r = self.session.post(self.base_url, json=subscription, headers=self._rw_headers)
        self.raise_from_response(r)
        return r.json()

    def list(self):
        r = self.session.get(self.base_url, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def get(self, subscription_uuid):
        r = self.session.get('{base}/{id}'.format(base=self.base_url, id=subscription_uuid), headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def edit(self, subscription_uuid, subscription):
        r = self.session.put('{base}/{id}'.format(base=self.base_url, id=subscription_uuid), json=subscription, headers=self._rw_headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, subscription_uuid):
        r = self.session.delete('{base}/{id}'.format(base=self.base_url, id=subscription_uuid), headers=self._ro_headers)
        self.raise_from_response(r)

    def list_services(self):
        r = self.session.get('{base}/services'.format(base=self.base_url), headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()
