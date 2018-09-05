import requests

# 返回时json的情况
res = requests.get(url="http://update.km.com")
print(res.text)
print(res)
print(res.status_code)
print(res.json())
print(res.json)
print(type(res))
print(type(res.text))
print(type(res.json()))

print("-----------------------")

# 返回不是json的情况，没有json格式，所以res.json()会报错
res = requests.get("http://www.baidu.com")
print(res.text)
print(res)
print(res.json)
# print(res.json())




