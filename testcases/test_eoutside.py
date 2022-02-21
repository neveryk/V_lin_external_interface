from testcases.conftest import gen,outside_data,excel_path,sheet_name,excel_data
import pytest
import allure
#使用excel自动生成数据
class Test_Excel_Outside():
    # 每次必须调用apikey访问
    @allure.story('获取凭证接口')
    @allure.title('执行获取凭证接口用例')
    @allure.step('获取凭证')
    @pytest.mark.parametrize('userkey,secret,apitype,message,returnStatus',outside_data['test_getkey'])
    def test_getkey(self,userkey,secret,apitype,message,returnStatus):
        res=gen.get_key(userkey,secret,apitype)
        json_data=res.json()
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

    @allure.story('人员同步')
    @allure.title('执行人员同步用例')
    @allure.step('人员同步')
    @pytest.mark.parametrize("customerCode,peopleName,iDCard,phone,paymentAccountType,bankCode,bankName,createDate,signDate,protocolState,message,returnStatus",excel_data)
    def test_add_people(self,customerCode,peopleName,iDCard,phone,paymentAccountType,bankCode,bankName,createDate,signDate,protocolState,message,returnStatus):
        res = gen.add_people(apikey,customerCode,peopleName,iDCard,phone,paymentAccountType,bankCode,bankName,createDate,signDate,file_path,protocolState)
        json_data = res.json()
        assert res.status_code == 200
        assert json_data["message"] == "success"
        assert json_data["returnStatus"] == 1
        return res
