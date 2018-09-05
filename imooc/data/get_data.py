from util.opera_excel import OperateExcel
from util.opera_json import OperateJson
from data import data_config

class GetData:
    def get_case_lines(self):
        return OperateExcel().get_lines()
    def get_is_run(self, row):
        col = data_config.get_run()
        run_model = OperateExcel().get_cell_value(row, col)
        if run_model == 'yes':
            return True
        else:
            return False

    def get_url(self, row):
        col = data_config.get_url()
        return OperateExcel().get_cell_value(row, col)
    def is_header(self,row):
        col = data_config.get_header()
        return OperateExcel().get_cell_value(row, col)
    def get_request_method(self,row):
        col = data_config.get_request_way()
        return OperateExcel().get_cell_value(row, col)
    def get_request_data(self,row):
        col = data_config.get_data()
        data = OperateExcel().get_cell_value(row, col)
        if data == "":
            return None
        else:
            return data
    def get_data_for_json(self, row):
        file_name = '../dataconfig/login.json'
        key = self.get_request_data(row)
        return OperateJson(file_name, key).get_value()

    def get_expect_data(self, row):
        col = data_config.get_expect()
        expect = OperateExcel().get_cell_value(row, col)
        return expect
    def write_result(self, row, value):
        col = data_config.get_result()
        OperateExcel().write_data(row, col, value)

    def get_depend_case_id(self, row):
        """从当前运行case中返回依赖cese_id"""
        col = data_config.get_case_depend()
        return OperateExcel().get_cell_value(row, col)
    def get_depend_key(self, row):
        """返回依赖字段"""
        col = data_config.get_data_depend()
        depend_key = OperateExcel().get_cell_value(row, col)
        if depend_key == '':
            return None
        else:
            return depend_key
    def get_depend_source_key(self, row):
        col = data_config.get_field_depend()
        depend_source_key = OperateExcel().get_cell_value(row, col)
        return depend_source_key








