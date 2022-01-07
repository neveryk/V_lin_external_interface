from testcases.conftest import gen,outside_data
import pytest
import allure

class TestOutside():
    # V零工对外接口
    # 每次必须调用apikey访问
    @allure.step('获取凭证接口')
    @pytest.mark.parametrize('userkey,secret,apitype',outside_data['test_getkey'])
    def test_getkey(self,userkey,secret,apitype):
        res=gen.get_key(userkey,secret,apitype)
        json_data=res.json()
        global apikey
        apikey=json_data["data"]["apikey"]
        assert json_data["message"]=="success"
        return res
    #
    # @allure.step('上传附件')
    # def test_upload(self):
    #     res=gen.upload_file(apikey)
    #     return res
    #
    # @allure.step('任务同步接口V1')
    # @pytest.mark.parametrize("orderNo,orderName,customerCode,address,peopleName,iDCard,bankCode,amt,exAmt",outside_data["test_add_order_v1"])
    # def test_add_order_v1(self,orderNo,orderName,customerCode,address,peopleName,iDCard,bankCode,amt,exAmt):
    #     res=gen.add_order_v1(apikey,orderNo,orderName,customerCode,address,peopleName,iDCard,bankCode,amt,exAmt)
    #     return res
    #
    # @allure.step('任务同步接口V2')
    # @pytest.mark.parametrize("data",outside_data["test_add_order_v2"])
    # def test_add_order_v2(self,data):
    #     data["apikey"]=apikey
    #     res = gen.many_add_order_v2(data)
    #     return res
    #
    # @allure.step('任务同步接口V1-多人')
    # @pytest.mark.parametrize("data", outside_data["test_add_order_v1_many"])
    # def test_add_order_v1_many(self, data):
    #     data["apikey"] = apikey
    #     res = gen.many_add_order_v1(data)
    #     return res

    @allure.step('人员同步')
    @pytest.mark.parametrize("customerCode,peopleName,iDCard,phone,paymentAccountType,bankCode,bankName,createDate,signDate,signFile,protocolState", outside_data["add_people"])
    def test_add_order_v1_many(self,customerCode,peopleName,iDCard,phone,paymentAccountType,bankCode,bankName,createDate,signDate,signFile,protocolState):
        res = gen.add_people(apikey,customerCode,peopleName,iDCard,phone,paymentAccountType,bankCode,bankName,createDate,signDate,signFile,protocolState)
        return res


