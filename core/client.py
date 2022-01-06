import requests
import allure
import os
import json
import urllib3
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class Client:
    def __init__(self, host, **kwargs):
        self.host = host
        self.session = requests.session()
        self.header={"Content-Type":"application/json;charset=UTF-8"}

    def get(self, url, params=None, **kwargs):
        urllib3.disable_warnings()
        res = self.session.get(self.host + url, params=params, verify=False,**kwargs)
        # allure.attach(json.dumps(dict(self.session.headers.items())), 'request-headers', allure.attachment_type.TEXT)
        allure.attach(res.text, 'response-data', allure.attachment_type.TEXT)
        return res

    def post(self, url, jsondata=None,**kwargs):
        urllib3.disable_warnings()
        res = self.session.post(self.host + url,data=jsondata,verify=False,headers=self.header,**kwargs)
        # allure.attach(json.dumps(dict(self.session.headers.items())), 'request-headers', allure.attachment_type.TEXT)
        allure.attach(res.text, 'response-data', allure.attachment_type.TEXT)
        return res

