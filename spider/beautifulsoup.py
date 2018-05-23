"""
介绍HTML处理的一种工具 BeautifulSoup

可以将HTML处理的更有格式化，便于计算机识别处理
"""
import requests
from bs4 import BeautifulSoup

url = 'http://python123.io/ws/demo.html'
r = requests.get(url)
# print(r.text)

demo = r.text

soup = BeautifulSoup(demo, "html.parser")

# 打印出soup过后的页面内容
# print(soup.prettify())

# 打印soup的title部分的内容
print(soup.title)
# 打印title中的文字那种
print(soup.title.string)

# 打印body内的全部内容
# print(soup.body)
# 打印 body内含的 <content> 内容
print(soup.body.content)

# 提取出soup中的<a>类  第一个
tag = soup.a
print(tag)
