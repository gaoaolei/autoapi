import requests
import json

class RunMethod:
    def __int__(self, url, data, method):
        res = self.send_request(url, data, method)
        return res
    def send_get(self, url, data):
        res = requests.get(url, data).json()
        return json.dumps(res, indent=4, sort_keys=True)
    def send_post(self, url, data):
        res = requests.post(url, data).json()
        return json.dumps(res, indent=4, sort_keys=True)
    def send_request(self, url, data, method):
        res = None
        if method == "GET":
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res

if __name__ == "__main__":
    url = "http://localhost:7777/api/mgr/sq_mgr/"
    data = {
        "action": "list_course",
        "pagenum": "1",
        "pagesize": "20"
    }
    a=RunMethod(url, data, "GET")
    print(a)