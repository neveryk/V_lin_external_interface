import json
import logging
import requests
from core.client import Client
import allure
import os
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
            ('files', ('files', open(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+"\data\员工管理导入模板.xlsx", 'rb'), 'application/vnd.ms-excel'))
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

    def update_people_message(self,apikey,customerCode,peopleName,iDCard,signDate,signFile):
        data={
            "apikey":apikey,
            "customerCode":customerCode,
            "peopleName":peopleName,
            "iDCard":iDCard,
            "signDate":signDate,
            "signFile":signFile
        }
        return self.post("/api/External/Protocol",data)

    def update_bank_code(self,apikey,peopleName,iDCard,paymentAccountType,bankCode,bankName):
        data={
            "apikey":apikey,
            "peopleName":peopleName,
            "iDCard":iDCard,
            "paymentAccountType":paymentAccountType,
            "bankCode":bankCode,
            "bankName":bankName
        }
        return self.post("/api/External/UpBankCard",data)

    def get_order_state(self,apikey,orderNo):
        data={
            "apikey":apikey,
            "orderNo":orderNo
        }
        return self.post("/api/External/GetGenerateByOrderNo",data)

    def get_people_state(self,apikey,generateCode):
        data={
            "apikey":apikey,
            "generateCode":generateCode
        }
        return  self.post("/api/External/GetPeoplesByGenerateCode",data)

    def get_Client_freeamount(self,apikey,customerCode):
        data={
            "apikey":apikey,
            "customercode":customerCode
        }
        return self.post("/api/External/GetClient",data)
