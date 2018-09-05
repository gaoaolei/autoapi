from data.get_data import GetData
from base.runmethod import RunMethod
from util.common_util import CommonUtil
from data.dependent_data import DenpendentData
class RunTest:
    def __init__(self):
        self.data = GetData()
        self.run_method = RunMethod()

    # 程序执行的主入口
    def go_on_run(self):
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            """第一步判断case是否运行"""
            is_run = self.data.get_is_run(i)
            # print("run method:%s" % is_run)
            if is_run:
                url = self.data.get_url(i)
                # print(url)
                method = self.data.get_request_method(i)
                # print(method)
                data = self.data.get_data_for_json(i)
                print(data)
                header = self.data.is_header(i)
                expect = self.data.get_expect_data(i)
                # print(header)
                """第二步判断是否有依赖"""
                depend_source_key = GetData().get_depend_source_key(i)
                if depend_source_key:
                    depend_value = DenpendentData().get_depend_value_from_depend_reponse_data_by_depend_key(i)
                    data[depend_source_key] = depend_value
                    print(data)

                response = self.run_method.run_main(method, url, data, header)
                print(response)
                flag = CommonUtil().contain(expect, response)
                if flag:
                    self.data.write_result(i, "测试通过")
                else:
                    self.data.write_result(i, "测试失败")

if __name__ == "__main__":
    run = RunTest()
    run.go_on_run()