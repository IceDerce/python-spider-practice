import requests

r = requests.get("https://www.amazon.cn/dp/B073LJR2JF")
print(r.status_code)
print(r.encoding)
print(r.request.headers)

# print(r.text)
