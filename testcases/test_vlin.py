from testcases.conftest import ten,base_data
import pytest
import allure

class TestVlin():
    pass
    # 上海麦朵接口用
    @allure.story('新增银行卡接口')
    @allure.title('执行新增银行卡接口用例')
    @allure.step('新增银行卡测试数据')
    @pytest.mark.parametrize('payTaxesCode,keyStr,bankName,bankCode,idCrad',base_data['test_addbank_code'])
    def test_addbank_code(self,payTaxesCode,keyStr,bankName,bankCode,idCrad):
        res=ten.insert_bankcode(payTaxesCode,keyStr,bankName,bankCode,idCrad)
        respons = res.json()
        success = respons["returnStatus"]
        message = respons["message"]
        assert success == 1 and message == "null"


    @allure.story('编辑银行卡接口')
    @allure.title('执行编辑银行卡接口用例')
    @allure.step('编辑银行卡')
    @pytest.mark.parametrize("payTaxesCode,keyStr,OldbankName,OldbankCode,bankName,bankCode,idCrad",base_data["test_updatebank_code"])
    def test_updatebank_code(self,payTaxesCode,keyStr,OldbankName,OldbankCode,bankName,bankCode,idCrad):
        res=ten.update_bankcode(payTaxesCode,keyStr,OldbankName,OldbankCode,bankName,bankCode,idCrad)
        respons = res.json()
        success = respons["returnStatus"]
        assert success == 1
        return res
    # #
    @allure.story('新增人员接口')
    @allure.title('执行新增人员接口用例')
    @allure.step('新增人员测试数据')
    @pytest.mark.parametrize("payTaxesCode,keyStr,peopleName,iDCard,phone,bankName,bankCode,email,message,returnStatus",base_data["test_insert_people"])
    def test_insert_people(self, payTaxesCode,keyStr,peopleName,iDCard,phone,bankName,bankCode,email,message,returnStatus):
        res = ten.insert_people(payTaxesCode,keyStr,peopleName,iDCard,phone,bankName,bankCode,email)
        respons=res.json()
        status=respons["returnStatus"]
        mess=respons["message"]
        assert status==returnStatus
        assert mess==message


    # #
    @allure.story('新增订单接口')
    @allure.title('执行新增订单接口用例')
    @allure.step('创建订单')
    @pytest.mark.parametrize("data",base_data["test_add_order"])
    def test_add_order(self,data):
        res = ten.add_order(data)
        respons = res.json()
        success = respons["returnStatus"]
        assert success == 1
        return res