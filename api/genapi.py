import json
import logging
import requests
from core.client import Client

import allure

class Genapi(Client):
    def __init__(self, host, **kwargs):
        super(Genapi, self).__init__(host, **kwargs)
    #V零工对外接口
    def get_key(self,userkey,secret,apitype):
        data={
            "userkey":userkey,
            "secret":secret,
            "apitype":apitype
        }
        return self.post_key('/api/External/GetKey',jsondata=data)

    def upload_file(self,apikey):
        files = [
            ('files', ('files', open("C:\\Users\\Administrator\\Desktop\\数据\\员工管理导入模板.xlsx", 'rb'), 'application/vnd.ms-excel'))
        ]
        data={
            "apikey":apikey
        }
        return self.post_file('/api/External/UpLoadFile',jsondata=data,file=files)

    def add_order_v1(self,apikey,orderNo,orderName,customerCode,address,peopleName,iDCard,bankCode,amt,exAmt):
        data={
            "apikey":apikey,
            "orderNo":orderNo,
            "orderName":orderName,
            "customerCode":customerCode,
            "address":address,
            "peopleName":peopleName,
            "iDCard":iDCard,
            "bankCode":bankCode,
            "amt":amt,
            "exAmt":exAmt
        }
        return self.post('/api/External/AddOrder',data)

    def many_add_order_v1(self,data):
        return self.post('/api/External/AddOrderPeoples',data)

    def many_add_order_v2(self,data):
        return self.post('/api/External/AddOrderV2',data)

    def add_people(self,apikey,customerCode,peopleName,iDCard,phone,paymentAccountType,bankCode,bankName,createDate,signDate,signFile,protocolState):
        data={
            "apikey":apikey,
            "customerCode":customerCode,
            "peopleName":peopleName,
            "iDCard":iDCard,
            "phone":phone,
            "paymentAccountType":paymentAccountType,
            "bankCode":bankCode,
            "bankName":bankName,
            "createDate":createDate,
            "signDate":signDate,
            "signFile":signFile,
            "protocolState":protocolState
        }
        return self.post('/api/External/AddPeople',data)