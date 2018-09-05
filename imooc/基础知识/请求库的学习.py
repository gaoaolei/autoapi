import requests
import json
data = {"secrect": "b94fb01b388129b61c3b9714e1b17b43",
        "timestamp": "1527948687076",
        "token": "071fd0fc55a7fce4d151a5af1a649fb7",
        "uid": "6547325"
        }
a = requests.request('POST', 'http://www.imooc.com/api3/coursecategories')
print(a.status_code)
print(a, '\n----------------------------------')
print(a.text, '\n----------------------------------')
print(a.json, '\n----------------------------------')
print(a.json(), '\n----------------------------------')
print(json.dumps(a.json(), indent=4), '\n----------------------------------')




