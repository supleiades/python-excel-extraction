import re
import json
import shutil
from datetime import datetime, date, timedelta

import openpyxl

# Excelファイル読み込み
wb = openpyxl.load_workbook('{file_path}')
sheet = wb.sheetnames[sheetlist[1]]
print(type(sheet))
print(sheet.title)


# 取得した値をjsonに格納
json_name = {
    "variable01"  : sheet["A1"].value,
}


# 変数の中身を確認
print(f"""
json.dumps(json_name, indent=2)
"""
)
      

# テンプレートファイル読み込み
with open(before_filename, encoding='utf-8') as f:
    data_lines = f.read()

    
# 文字列置換
for i in json_name.keys():
    bedore_replaceword = {keyword}
    data_lines = data_lines.replace(bedore_replaceword, str(json_name[i])


# 別名保存
with open(after_filename, mode='w', encoding='utf-8') as f:
    f.write(date_lines)
