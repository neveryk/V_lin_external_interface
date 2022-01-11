from testcases.conftest import ten,base_data
import pytest
import allure

class TestVlin():
    # 上海麦朵接口用
    # @allure.step('新增银行卡')
    # @pytest.mark.parametrize('payTaxesCode,keyStr,bankName,bankCode,idCrad',base_data['test_addbank_code'])
    # def test_addbank_code(self,payTaxesCode,keyStr,bankName,bankCode,idCrad):
    #     res=ten.insert_bankcode(payTaxesCode,keyStr,bankName,bankCode,idCrad)
    #     respons = res.json()
    #     success = respons["returnStatus"]
    #     message = respons["message"]
    #     assert success == 1 and message == "null"


    #
    # @allure.step('编辑银行卡')
    # @pytest.mark.parametrize("payTaxesCode,keyStr,OldbankName,OldbankCode,bankName,bankCode,idCrad",base_data["test_updatebank_code"])
    # def test_updatebank_code(self,payTaxesCode,keyStr,OldbankName,OldbankCode,bankName,bankCode,idCrad):
    #     res=ten.update_bankcode(payTaxesCode,keyStr,OldbankName,OldbankCode,bankName,bankCode,idCrad)
    #     respons = res.json()
    #     success = respons["returnStatus"]
    #     assert success == 1
    #     return res
    # #
    @allure.step('新增人员')
    @pytest.mark.parametrize("payTaxesCode,keyStr,peopleName,iDCard,phone,bankName,bankCode,email,message,returnStatus",base_data["test_insert_people"])
    def test_insert_people(self, payTaxesCode,keyStr,peopleName,iDCard,phone,bankName,bankCode,email,message,returnStatus):
        res = ten.insert_people(payTaxesCode,keyStr,peopleName,iDCard,phone,bankName,bankCode,email)
        try:
            if res.status_code==200:
                respons=res.json()
                status=respons["returnStatus"]
                mess=respons["message"]
                assert status==returnStatus
                assert mess==message
        except Exception as e:
            return e

    # #
    # @allure.step('创建订单')
    # @pytest.mark.parametrize("data",base_data["test_add_order"])
    # def test_add_order(self,data):
    #     res = ten.add_order(data)
    #     respons = res.json()
    #     success = respons["returnStatus"]
    #     assert success == 1
    #     return res