import random
import datetime
from faker import Faker
import time
f=Faker(locale='zh-CN')
class Generate_Data():
    def addpeople_data(self,num):
        cols=["姓名","银行卡号","手机号码","身份证","时间"]
        datalist=[]
        for i in range(num):
            people_name=f.name()
            bank_code = random.randint(6200000000000000, 6299999999999999)
            phone_num=f.phone_number()
            sfz = f.ssn()
            date=time.strftime("%Y-%m-%d %H:%M:%S")
            data=[people_name,str(bank_code),phone_num,sfz,date]
            datalist.append(data)
        datalist.insert(0,cols)
        return datalist

    def timelife(self):
        now=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        today=datetime.date.today()
        last_day_of_last_month=datetime.date(today.year,today.month,1)-datetime.timedelta(1)
        first_day_of_last_month=datetime.date(last_day_of_last_month.year,last_day_of_last_month.month,1)
        return {"last_day_of_last_month":str(last_day_of_last_month),"first_day_of_last_month":str(first_day_of_last_month),"now":str(now)}


gen=Generate_Data()
