import pymssql
import json
#import pandas as pd
#from testcases.conftest import gen,outside_data
import pytest


class sqlnumber():

    def conn(self):
        connect = pymssql.connect('192.168.8.168', 'sa', 'qwe123!@#', 'master') #服务器名,账户,密码,数据库名
        # if connect:
        #     print("连接成功!")
        return connect

    #@pytest.mark.parametrize("customerCode", outside_data["get_Client_freeamount"])
    #, customerCode
    def getCfreeamount(self,clientid):
        connect=self.conn()
        cursor = connect.cursor() #创建游标
        sql="SELECT cast(balance-lockFunds as varchar) from  [V_OddJob].[dbo].[W_EnterpriseWallet]  where account in(SELECT walletAccount  from [V_OddJob].[dbo].[P_Client] p where payTaxesCode='{clientid}')".format(clientid=clientid)
        cursor.execute(sql)
        freeamount=cursor.fetchall()
        #print(freeamount)
        connect.commit()
        cursor.close()
        connect.close()
        return freeamount


s=sqlnumber()
#s.conn()
#s.getCfreeamount()

