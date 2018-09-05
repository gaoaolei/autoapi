import json
# fp = open("../dataconfig/login.json")
# data = json.load(fp)
# print(data['login'])
# fp.close()
class OperateJson:
    def __init__(self, file_name, key):
        self.file_name = file_name
        self.key = key
        self.data = self.get_data()
    def get_data(self):
        with open(self.file_name, 'r') as fp:
            return json.load(fp)
    def get_value(self):
        return self.data[self.key]

if __name__ == '__main__':
    oper = OperateJson("../dataconfig/login.json", 'login')
    a = oper.get_value()
    print(a)