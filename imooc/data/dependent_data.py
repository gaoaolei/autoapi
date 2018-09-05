from util.opera_excel import OperateExcel
from data.get_data import GetData
from base.runmethod import RunMethod
from jsonpath_rw import jsonpath, parse
import json
class DenpendentData:

    def get_row_line_data(self, row):   # 压根没用上
        """通过依赖case_id获取依赖cese的整行数据"""
        case_id = GetData().get_depend_case_id(row)       # 考虑下怎么用global
        return OperateExcel().get_row_value(case_id)

    def run_depend_case(self, row):
        case_id = GetData().get_depend_case_id(row)
        row_num_of_depend_case = OperateExcel().get_row_num(case_id)
        url = GetData().get_url(row_num_of_depend_case)
        method = GetData().get_request_method(row_num_of_depend_case)
        header = GetData().is_header(row_num_of_depend_case)
        data = GetData().get_data_for_json(row_num_of_depend_case)
        print("-----------------依赖的请求数据--------------")
        print(data)
        print("-------------------------------------------")
        depend_response_data = RunMethod().run_main(method, url, data, header)
        return json.loads(depend_response_data)


    def get_depend_value_from_depend_reponse_data_by_depend_key(self, row):
        """根据依赖数据key找到depend_response_data中对应的value"""
        depend_key = GetData().get_depend_key(row)
        depend_response_data = self.run_depend_case(row)    # 学习下此处
        print("-----------------依赖的响应数据--------------")
        print(depend_response_data)
        print("-------------------------------------------")
        json_exe = parse(depend_key)
        madle = json_exe.find(depend_response_data)
        depend_value = [math.value for math in madle][0]  # 必须这么写
        return depend_value





