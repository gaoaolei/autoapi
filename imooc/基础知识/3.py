import requests
def send_get(url, data):
    res = requests.get(url, data).json()
    return res
def send_post(url, data):
    res = requests.post(url, data).json()
    return res
url = "http://update.km.com/index.php"
data={
"appkey":"a36df9deb74d498a12284e14477c4304",
"authkey":"dsflgjdlkgjdlgdndfjgdgjldjgldkfjg",
"channel":"qm-huawei_lf",
"old_md5":"11111111111111111111111111111111",
"sign":"BAJbCABbV1AEBgZWAFQAVAUAXVMADgwLUgZTBwcDUVs=",
"type":"update",
"user_version":"1.0",
"version":"10000",
"":"081718f730219e20856fced4d60c58a7"
}

a = send_post(url, data)
print(a)

