# import requests
# import json
# class RunMethod:
#     def post_main(self, url, data, header=None):
#         res = None
#         if header != None:
#             res = requests.post(url=url, data=data, headers=header)
#         else:
#             res = requests.post(url=url, data=data)
#         return res.json()
#
#     def get_main(self, url, data=None, header=None):
#         res = None
#         if header != None:
#             res = requests.get(url=url, data=data, headers=header)
#         else:
#             res = requests.get(url=url, data=data)
#         return res.json()
#
#     def run_main(self, method, url, data=None, header=None):
#         res = None
#         if method == 'Post':
#             res = self.post_main(url, data, header)
#         else:
#             res = self.get_main(url, data, header)
#         return json.dumps(res, indent=4)

import requests
import json
class RunMethod:
    def post_main(self, url, data, header=None):
        return requests.post(url=url, data=data, headers=header)

    def get_main(self, url, data=None, header=None):
        return requests.get(url=url, data=data, headers=header)

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res.json(), indent=4)


