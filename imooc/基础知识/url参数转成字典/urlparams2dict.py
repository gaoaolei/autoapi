# 将name=xiaoming&pwd=111转成字典
import urllib.parse
url = 'http://www.xx.com?'
urlparams = 'name=xiaoming&pwd=111'

new_url = url + urlparams
data = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
print(data)