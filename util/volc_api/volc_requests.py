import json
import logging

import requests

from util.volc_api.volc_client_model import VolcClientConfig
from util.volc_api.volc_constant import VOLC_CONSTANT
from util import lib

class VolcRequests:
    def __init__(self, client):
        if client is None:
            self.client = VolcClientConfig()
        else:
            self.client = client

    @staticmethod
    def form_params(action=None, params=None):
        if params is None:
            params = {}
        params_merged = {"Action": action}
        logging.info(params)
        logging.info(params_merged)
        params_merged.update(params)
        return params_merged

    @staticmethod
    def implement(client, url, action, params, data, method):
        if params is None:
            params = {}
        if action is not None:
            params = VolcRequests.form_params(action=action, params=params)
        if method == VOLC_CONSTANT.GET:
            resp = VolcRequests(client=client).get(url, params=params)
        elif method == VOLC_CONSTANT.POST:
            resp = VolcRequests(client=client).post(url, params=params, data=data)
        else:
            raise Exception("Request method invalid, please check!")
        logging.info("请求Volc GTM OpenApi, URL: %s" % resp.url)
        # logging.info(resp.text)
        # logging.info(resp)
        assert "ResponseMetadata" in resp.text, resp.text
        return resp.status_code, lib.bytes2json(resp.content)

    def post(self, url, params, data):
        # return requests.post(
        #     url=url,
        #     headers=self.client.headers,
        #     params=params,
        #     data=json.dumps(data),
        #     auth=self.client.auth,
        # )
        resp = requests.post(
            url=url,
            headers=self.client.headers,
            params=params,
            data=json.dumps(data),
            auth=self.client.auth,
        )
        return resp

    def get(self, url, params):
        return requests.get(
            url=url,
            headers=self.client.headers,
            params=params,
            auth=self.client.auth,
        )
