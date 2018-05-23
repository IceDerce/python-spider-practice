"""
在BeautifulSoup中查找内容

这一部分为bs4库自带的内容
soup.find_all():
    默认是对标签名(name)进行搜索，
    但是也可以附加搜索属性(Attributes)
    也可以进行内容搜索(strings)
  HTML : <name  Attributes>strings</name>
  同样soup.find_all()可以简单的表达为soup()
"""
import requests
from bs4 import BeautifulSoup
import re

url = 'http://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")

# 查找soup中包含link的所有<a>标签，并且打印出其中的href链接
# for link in soup.find_all('a'):
#    print(link.get('href'))

# 查找soup中所有的<a>标签
# print(soup.find_all('a'))

# 查找soup中所有的a标签和b标签，并且将其储存在列表中
# print(soup.find_all(['a', 'b']))

# 列出soup中包含的所有标签，名字
# for tag in soup.find_all(True):
#    print(tag.name)

# 列出包含b字母的标签，比如b和body标签,名字
# 需要引入正则表达式库 import re
# for tag in soup.find_all(re.compile('b')):
#    print(tag.name)

"""
这一部分是查找标签name中属性的部分

可以使用准确属性词查找，也可使用正则表达式库，进行关键词查找
"""
# 查找p标签中包含course字符串
# print(soup.find_all('p', 'course'))

# 查找标签属性，包含id=link1的内容
# print(soup.find_all(id='link1'))
# 查找标签属性，包含id=link的内容
# print(soup.find_all(id='link'))

# 查找标签中包含link字符串的标签内容
# print(soup.find_all(id=re.compile('link')))

# 查找所有内容(strings)中包含Basic Python的内容
# print(soup.find_all(text='Basic Python'))
# 下面也可以 但是很慢
# print(soup.find_all(string = 'Basic Python'))

# 利用正则表达式库进行关键词查找
# print(soup.find_all(text=re.compile('python')))




