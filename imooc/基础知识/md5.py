import hashlib

str = '869654023368628'

hl = hashlib.md5()

hl.update(str.encode(encoding='utf-8'))

print('MD5加密前为 ：' + str)
print('MD5加密后为 ：' + hl.hexdigest())