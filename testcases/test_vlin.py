from testcases.conftest import ten,base_data
import pytest
import allure

class TestVlin():
    # 上海麦朵接口用
    @allure.step('新增银行卡')
    @pytest.mark.parametrize('payTaxesCode,keyStr,bankName,bankCode,idCrad',base_data['test_addbank_code'])
    def test_addbank_code(self,payTaxesCode,keyStr,bankName,bankCode,idCrad):
        res=ten.insert_bankcode(payTaxesCode,keyStr,bankName,bankCode,idCrad)
        respons = res.json()
        success = respons["returnStatus"]
        assert success == 1
        return res

    @allure.step('编辑银行卡')
    @pytest.mark.parametrize("payTaxesCode,keyStr,OldbankName,OldbankCode,bankName,bankCode,idCrad",base_data["test_updatebank_code"])
    def test_updatebank_code(self,payTaxesCode,keyStr,OldbankName,OldbankCode,bankName,bankCode,idCrad):
        res=ten.update_bankcode(payTaxesCode,keyStr,OldbankName,OldbankCode,bankName,bankCode,idCrad)
        respons = res.json()
        success = respons["returnStatus"]
        assert success == 1
        return res
    #
    @allure.step('新增人员')
    @pytest.mark.parametrize("payTaxesCode,keyStr,peopleName,iDCard,phone,bankName,bankCode,email",base_data["test_insert_people"])
    def test_insert_people(self, payTaxesCode,keyStr,peopleName,iDCard,phone,bankName,bankCode,email):
        res = ten.insert_people(payTaxesCode,keyStr,peopleName,iDCard,phone,bankName,bankCode,email)
        respons=res.json()
        success=respons["returnStatus"]
        assert success==1
        return res
    #
    @allure.step('创建订单')
    @pytest.mark.parametrize("data",base_data["test_add_order"])
    def test_add_order(self,data):
        res = ten.add_order(data)
        respons = res.json()
        success = respons["returnStatus"]
        assert success == 1
        return res