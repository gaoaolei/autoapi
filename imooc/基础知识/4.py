# 1.post（url，data）
# post请求的两种数据形式，表单（直接用dict传递）和json（将dict处理为json后传递）
import json
content = {'key1': 'value1', 'key2': 'value2'}
print(type(content))
# 将dict转为string类型的json格式
str_content = json.dumps(content)
print(type(str_content))
# 将json转回原来的格式
dict_content = json.loads(str_content)
print(type(dict_content))

# 2.post（url，json）  可不用1 的方法，直接传递json


# 实例
import requests
url = "http://localhost:7777/api/mgr/loginReq"
data = {
    "username": "auto2",
    "password": "sdfsdfsdf"
}
res = requests.post(url=url, data=data)
result = [res, res.text, res.json(), res.status_code]
print(result)
