import requests
import json
url = "http://localhost:7777/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20"
b = requests.get(url=url)
print(b.json())
print(type(b.json()))
# dict转为json（格式化）

c = json.dumps(b.json(), indent=8, sort_keys=True)
print(c)
print(type(c))


