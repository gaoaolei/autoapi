"""不用类的写法，就是这么简单"""
import xlrd
import json
from base.runmethod import RunMethod

data = xlrd.open_workbook('dataconfig/interface.xlsx')
tables = data.sheets()[0]

for i in range(1, tables.nrows):
    url = tables.cell_value(i, 2)
    is_run = tables.cell_value(i, 3)
    method = tables.cell_value(i, 4)
    with open("dataconfig/login.json") as fp:
        data = json.load(fp)[tables.cell_value(i, 9)]
    if is_run == "yes":
        print(RunMethod().run_main(method, url, data))
