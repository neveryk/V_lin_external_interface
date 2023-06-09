from testcases.conftest import gen, outside_data
import pytest
import pytest_ordering
import allure

from common.operation_excel import excel
from common.connect_database import s



class TestOutside():
    #pass
    #V零工对外接口
    #每次必须调用apikey访问
    @allure.story('获取凭证接口')
    @allure.title('执行获取凭证接口用例')
    @allure.step('获取凭证')
    @pytest.mark.parametrize('userkey,secret,apitype,message,returnStatus',outside_data['test_getkey'])
    @pytest.mark.run(order=1)
    def test_getkey(self,userkey,secret,apitype,message,returnStatus):
        res=gen.get_key(userkey,secret,apitype)
        json_data=res.json()
        print(json_data)
        global apikey
        apikey=json_data["data"]["apikey"]
        assert res.status_code==200
        assert json_data["message"]==message
        assert json_data["returnStatus"]==returnStatus
        return res
    #
    @allure.story('获取上传文件接口')
    @allure.title('上传文件接口')
    @allure.step('上传附件')
    def test_upload(self):
        res=gen.upload_file(apikey)
        json_data = res.json()
        global file_path
        file_path=json_data["data"][0]["path"]
        assert res.status_code == 200
        assert json_data["message"] == "success"
        assert json_data["returnStatus"] == 1
        return res
    #
    # @allure.story('任务同步接口V1')
    # @allure.title('执行任务同步接口V1用例')
    # @allure.step('任务同步接口V1')
    # @pytest.mark.parametrize("orderNo,orderName,customerCode,address,peopleName,iDCard,bankCode,amt,exAmt,message,returnStatus",outside_data["test_add_order_v1"])
    # def test_add_order_v1(self,orderNo,orderName,customerCode,address,peopleName,iDCard,bankCode,amt,exAmt,message,returnStatus):
    #     res=gen.add_order_v1(apikey,orderNo,orderName,customerCode,address,peopleName,iDCard,bankCode,amt,exAmt)
    #     json_data = res.json()
    #     print(json_data)
    #     assert json_data["message"] == message
    #     assert json_data["returnStatus"] == returnStatus
    #     return res
    # #
    # @allure.story('任务同步接口V2')
    # @allure.title('执行任务同步接口V2用例')
    # @allure.step('任务同步接口V2')
    # @pytest.mark.parametrize("data",outside_data["test_add_order_v2"])
    # def test_add_order_v2(self,data):
    #     data["apikey"]=apikey
    #     res = gen.many_add_order_v2(data)
    #     return res
    #
    # @allure.story('任务同步接口V1-多人')
    # @allure.title('执行任务同步接口V1-多人用例')
    # @allure.step('任务同步接口V1-多人')
    # @pytest.mark.parametrize("data", outside_data["test_add_order_v1_many"])
    # def test_add_order_v1_many(self, data):
    #     data["apikey"] = apikey
    #     res = gen.many_add_order_v1(data)
    #     return res
    #
    @allure.story('人员同步')
    @allure.title('执行人员同步用例')
    @allure.step('人员同步')
    @pytest.mark.parametrize("customerCode,peopleName,iDCard,phone,paymentAccountType,bankCode,bankName,createDate,signDate,signFile,protocolState", outside_data["test_add_people"])
    def test_add_people(self,customerCode,peopleName,iDCard,phone,paymentAccountType,bankCode,bankName,createDate,signDate,signFile,protocolState):
        res = gen.add_people(apikey,customerCode,peopleName,iDCard,phone,paymentAccountType,bankCode,bankName,createDate,signDate,signFile,protocolState)
        json_data = res.json()
        assert res.status_code == 200
        assert json_data["message"] == message
        assert json_data["returnStatus"] == returnStatus
        return res
    #
    # @allure.story('更改人员签约信息')
    # @allure.title('执行更改人员签约信息用例')
    # @allure.step('更改人员签约信息')
    # @pytest.mark.parametrize("customerCode,peopleName,iDCard,signDate,signFile",outside_data["update_people_message"])
    # def test_up_people(self,customerCode,peopleName,iDCard,signDate,signFile):
    #     res = gen.update_people_message(apikey,customerCode,peopleName,iDCard,signDate,signFile)
    #     json_data = res.json()
    #     assert json_data["message"] == "success"
    #     return res
    #
    # @allure.story('银行卡修改')
    # @allure.title('执行银行卡修改用例')
    # @allure.step('银行卡修改')
    # @pytest.mark.parametrize("peopleName,iDCard,paymentAccountType,bankCode,bankName,phone,message,returnStatus",outside_data["update_bank_code"])
    # def test_up_bank_code(self,peopleName,iDCard,paymentAccountType,bankCode,bankName,phone,message,returnStatus):
    #     res = gen.update_bank_code(apikey,peopleName,iDCard,paymentAccountType,bankCode,bankName,phone)
    #     json_data = res.json()
    #     assert res.status_code == 200
    #     assert json_data["message"] == message
    #     assert json_data["returnStatus"] == returnStatus
    #     return res
    #
    # @allure.story('获取账单状态')
    # @allure.title('执行获取账单状态用例')
    # @allure.step('获取账单状态')
    # @pytest.mark.parametrize("orderNo", outside_data["get_order_state"])
    # def test_get_order_state(self,orderNo):
    #     res = gen.get_order_state(apikey,orderNo)
    #     return res
    #
    # @allure.story('获取人员发放状态')
    # @allure.title('执行获取人员发放状态用例')
    # @allure.step('获取人员发放状态')
    # @pytest.mark.parametrize("generateCode", outside_data["get_people_state"])
    # def test_get_people_state(self, generateCode):
    #     res = gen.get_people_state(apikey, generateCode)
    #     return res
    #
    # @allure.step('获取企业可用余额')
    # @pytest.mark.parametrize("customerCode,returnStatus", outside_data["get_Client_freeamount"])
    # @pytest.mark.run(order=3)
    # def test_get_Client_freeamount(self, customerCode,returnStatus):
    #     res = gen.get_Client_freeamount(apikey, customerCode)
    #     json_data = res.json()
    #     dfreeamount=s.getCfreeamount(customerCode)
    #     assert json_data["data"]["accountBalance"]==dfreeamount[0][0]
    #     assert json_data["message"]=="success"
    #     assert json_data["returnStatus"]==returnStatus
    #     return res
    #
    # @allure.step('人员发单状态查询')
    # @pytest.mark.parametrize("iDCard,peopleName,phone,bankCode,message,status",outside_data["get_people_orderstatus"])
    # @pytest.mark.run(order=2)
    # def test_get_people_orderstatus(self,iDCard,peopleName,phone,bankCode,message,status):
    #     res = gen.get_people_orderstatus(apikey, iDCard)
    #     json_data=res.json()
    #     print(json_data)
    #     # assert json_data["data"]["peopleInfo"]["peopleName"]==peopleName
    #     # assert json_data["data"]["peopleInfo"]["phone"]==phone
    #     # assert json_data["data"]["peopleInfo"]["bankCode"]==bankCode
    #     assert json_data["message"]==message
    #     assert json_data["data"]["status"]==status
    #     return res

    @allure.step('对账接口')
    @pytest.mark.parametrize("customerCode,startDate,endDate,message,returnStatus", outside_data["get_Statement"])
    @pytest.mark.run(order=2)
    def test_get_Statement(self, customerCode, startDate, endDate,message,returnStatus):
        res = gen.get_Statement(apikey, customerCode, startDate, endDate)
        json_data = res.json()
        print(json_data)
        assert json_data["message"]==message
        assert json_data["returnStatus"]==returnStatus
        return res
