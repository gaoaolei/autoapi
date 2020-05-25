import json
import os
print(os.getcwd()) # 获取当前路径
with open('./a.json') as fp:
    json_data = json.load(fp)
print(json_data)
print(type(json_data))