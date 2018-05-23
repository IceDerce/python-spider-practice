import requests

r = requests.get("https://www.baidu.com")


print(r.status_code)
# 查询header的编码方式，默认为ISO-8859-1
print(r.encoding)
# 查询body内容的编码方式
print(r.apparent_encoding)

# 打印出ISO-8859-1的编码内容
# print(r.text)

# 改变编码的方式到
r.encoding = 'utf-8'

# print(r.text)
