import xlrd

excel = xlrd.open_workbook('./workbook.xlsx')
# table = excel.sheets()[0]
table = excel .sheet_by_name('gaoaolei')
print(table.nrows)
value = table.cell_value(2,3)
print(value)