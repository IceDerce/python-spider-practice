import requests

url = "http://m.ip138.com/ip.asp?ip="
r = requests.get(url + '58.60.1.80')
print(r.status_code)

# 打印出网页返回内容的后500个字节
print(r.text[-500:])