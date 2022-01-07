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

    def update_bankcode(self,payTaxesCode,keyStr,OldbankName,OldbankCode,bankName,bankCode,idCrad):
        data={
            "payTaxesCode":payTaxesCode,
            "keyStr":keyStr,
            "OldbankName":OldbankName,
            "OldbankCode":OldbankCode,
            "bankName":bankName,
            "bankCode":bankCode,
            "idCrad":idCrad
        }
        return self.post('/api/External/Ext_EditBankCard',jsondata=data)

    def insert_people(self,payTaxesCode,keyStr,peopleName,iDCard,phone,bankName,bankCode,email):
        data={
            "payTaxesCode":payTaxesCode,
            "keyStr":keyStr,
            "peopleName":peopleName,
            "iDCard":iDCard,
            "phone":phone,
            "bankName":bankName,
            "bankCode":bankCode,
            "email":email
        }
        return self.post('/api/External/Ext_AddPeople',jsondata=data)

    def add_order(self,data):

        return self.post('/api/External/Ext_AddOrder',jsondata=data)


