import os
# 获取当前文件所在路径
print(os.getcwd())
# 获取文件路径
print(os.path.realpath(__file__))
print(os.path.split(os.path.realpath(__file__)))
print(os.path.split(os.path.realpath(__file__))[0])



