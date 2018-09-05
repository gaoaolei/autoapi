# get方法的两种方式
import requests
# ----1----
url = "http://localhost:7777/api/mgr/sq_mgr/"
data = {
    "action": "list_course",
    "pagenum": "1",
    "pagesize": "20"
    }
a = requests.get(url, data).json()
print(a)

# ----2----
url = "http://localhost:7777/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20"
b = requests.get(url=url).json()
print(b)
