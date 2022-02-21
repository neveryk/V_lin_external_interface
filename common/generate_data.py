import random
import datetime
from faker import Faker
import time
f=Faker(locale='zh-CN')
class Generate_Data():
    def addpeople_data(self,num):
        cols=["customerCode","姓名","身份证","手机号码","paymentAccountType","银行账号","bankName","createDate","signDate","protocolState","message","returnStatus"]
        datalist=[]
        for i in range(num):
            customerCode="44562131211500231QA"
            people_name=f.name()
            sfz = f.ssn()
            phone_num = f.phone_number()
            paymentAccountType=1
            bank_code = int(random.randint(6200000000000000, 6299999999999999))
            bankName="建行"
            createDate=time.strftime("%Y-%m-%d %H:%M:%S")
            signDate=createDate
            protocolState=0
            message="success"
            returnStatus=1
            data=[customerCode,people_name,str(sfz),phone_num,paymentAccountType,bank_code,bankName,createDate,signDate,protocolState,message,returnStatus]
            datalist.append(data)
        datalist.insert(0,cols)
        return datalist

    def timelife(self):
        now=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        today=datetime.date.today()
        last_day_of_last_month=datetime.date(today.year,today.month,1)-datetime.timedelta(1)
        first_day_of_last_month=datetime.date(last_day_of_last_month.year,last_day_of_last_month.month,1)
        return {"last_day_of_last_month":str(last_day_of_last_month),"first_day_of_last_month":str(first_day_of_last_month),"now":str(now)}


data_test=Generate_Data()
