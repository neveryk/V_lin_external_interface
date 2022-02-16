import os

import pandas as pd
import xlwt


class ReadExcelData():
    def read_xlsx(self,file_path):
        df = pd.read_excel(file_path)
        cols=df.shape[1]
        df = pd.read_excel(file_path, usecols=range(0, cols), names=None)
        df_li = df.values.tolist()
        return df_li

    def write_excel_xls(self,xls_name, sheet_name, value):
        index=len(value)
        wook=xlwt.Workbook()
        sheet=wook.add_sheet(sheet_name) #创建表单sheet
        for i in range(0,index):
            for j in range(0,len(value[i])):
                sheet.write(i,j,value[i][j])
        wook.save(xls_name)

excel=ReadExcelData()
