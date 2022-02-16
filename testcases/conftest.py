from api.tenapi import Tenapi
import os
from common.read_data import data_yaml
from api.tenapi import Tenapi
from api.genapi import Genapi
from common.operation_excel import excel

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, 'config', 'setting.ini')

def get_data(yaml_file_name):
    data_file_path = os.path.join(BASE_PATH, 'data', yaml_file_name)
    yaml_data = data_yaml.load_yaml(data_file_path)
    return yaml_data

def get_excel_data(excel_file_name):
    data_file_path = os.path.join(BASE_PATH, 'data', excel_file_name)
    excel_data = excel.read_xlsx(data_file_path)
    return excel_data

base_data = get_data('login_data.yml')
outside_data = get_data('outside_data.yml')

excel_path = os.path.join(BASE_PATH, 'data', "data.xls")
sheet_name="Sheet1"
excel_data= get_excel_data('data.xls')



HOST=data_yaml.load_ini(data_file_path)["host"]["BASEURL"]

ten=Tenapi(HOST)
gen=Genapi(HOST)
