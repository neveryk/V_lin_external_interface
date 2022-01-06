import json
import logging
import requests
from core.client import Client

import allure

class Tenapi(Client):
    def __init__(self, host, **kwargs):
        super(Tenapi, self).__init__(host, **kwargs)
    #上海麦朵用接口
    def insert_bankcode(self,payTaxesCode,keyStr,bankName,bankCode,idCrad):
        data={
            "payTaxesCode":payTaxesCode,
             "keyStr":keyStr,
             "bankName":bankName,
             "bankCode":bankCode,
             "idCrad":idCrad
        }
        return self.post('/api/External/Ext_AddBankCard',jsondata=data)

    def update_bankcode(self,data):
        return self.post('/api/External/Ext_EditBankCard',jsondata=data)

    def insert_people(self,data):
        return self.post('/api/External/Ext_AddPeople',jsondata=data)

    def add_order(self,data):
        return self.post('/api/External/Ext_AddOrder',jsondata=data)


