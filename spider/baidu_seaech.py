import requests
"""
直接使用requests进行搜索

baidu为/s?wd
google为/search?biw
"""
kv = {'wd': 'Python'}
r = requests.get("http://www.baidu.com/s", params=kv)
print(r.status_code)
print(r.request.url)
print(len(r.text))
# print(r.text)
