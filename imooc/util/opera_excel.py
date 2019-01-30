# daf
import xlrd
from xlutils.copy import copy
class OperateExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/interface.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()

    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        return self.data.nrows

    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    def write_data(self, row, col, value):
        """
        往excel中写入数据,必须得将表格copy一份再进行写操作
        执行的时候一定要关闭excel表，切记！！！，巨坑啊！！！
        """
        source_table = xlrd.open_workbook(self.file_name)
        backup_table = copy(source_table)
        enable_write_data_sheet = backup_table.get_sheet(0)   # 与读的时候区分
        enable_write_data_sheet.write(row, col, value)
        backup_table.save(self.file_name)

    """----------------依赖case相关的方法---------------------"""
    def get_col0_data(self):
        """获取case_id列内容"""
        return self.data.col_values(0)

    def get_row_num(self, case_id):
        """根据case_id找到行号"""
        row = 0
        cols_data = self.get_col0_data()
        for col_data in cols_data:
            if case_id == col_data:
                return row
            row = row + 1
    def get_row_data(self, row):  #  为什么此处在不直接调用前面的函数,因为这样可以减少依赖，减少耦合，可单独使用
        """通过行号获取整行内容"""
        return self.data.row_values(row)

    def get_row_value(self, case_id):
        """根据case_id获取依赖用例的整行数据，逻辑是get_col_data----->get_row----->get_row_data----->get_row_value"""
        return self.get_row_data(self.get_row_num(case_id))
    """---------------------------------------------------------"""


if __name__ == "__main__":
    # '-------------操作excel的用法---------------'
    # '获取文件'
    # data = xlrd.open_workbook('../dataconfig/interface.xlsx')
    # '获取表'
    # tables = data.sheets()[0]  # catch the first sheet
    # '获取表的总行数'
    # print(tables.nrows)  # print row_number of sheet
    # '获取单元格，横纵index从0开始'
    # print(tables.cell_value(2, 3))
    # '根据行号拿到整行的内容'
    # print(tables.row_values(3))
    print(OperateExcel().get_row_value("Imooc-005"))
