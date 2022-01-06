from testcases.conftest import ten,base_data
import pytest
import allure

class TestVlin():
    #上海麦朵接口用
    @allure.step('新增银行卡')
    @pytest.mark.parametrize('payTaxesCode,keyStr,bankName,bankCode,idCrad',base_data['test_addbank_code'])
    def test_addbank_code(self,payTaxesCode,keyStr,bankName,bankCode,idCrad):
        res=ten.insert_bankcode(payTaxesCode,keyStr,bankName,bankCode,idCrad)
        return res

