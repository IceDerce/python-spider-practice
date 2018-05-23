import re
"""
REGEX 正则表达式

即关键字符串，通过re工具匹配待搜索的内容
具体写法，自行参考网络
"""


"""
在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
re.research(pattern,string,flags=0)
     pattern:字符串或原生字符串
     string:待匹配的字符串
     flags:控制标记
"""
match = re.search(r'[1-9]\d{5}', 'mit 456132')
if match:
    print(match.group(0))


"""
re.match(patterns,string,flags=0)
从一个字符串的开始位置匹配正则表达式，返回match对象
"""
# 下面的语句无法查找到，会报错
# match = re.match(r'[1-9]\d{5}', 'mit 456132')
match = re.search(r'[1-9]\d{5}', '456132 mit')
if match:
    print(match.group(0))


"""
re.findall(patterns,string,flags=0)
搜索字符串，以列表的类型返回全部能匹配的字符串
"""
match = re.findall(r'[1-9]\d{5}', '456132 mit 554468')
print(match)

"""
re.split(patterns,string,maxsplit=0,flags=0)
将一个字符串按照正则表达式的匹配结果进行分割，返回列表类型
"""
ls = re.split(r'[1-9]\d{5}', 'ccc456132 mit 554468')
print(ls)


"""
re.finditer(patterns,string,flags=0)
搜索字符串，返回一个匹配结果的迭代类型，每个迭代的元素是match对象
"""
for m in re.finditer(r'[1-9]\d{5}', 'mit458995 ssa894164'):
    if m:
        print(m.group(0))

"""
re.sub(pattern,repl,string,count=0,flags=0)
在一个字符串中替换所有的匹配正则表达式的子串，返回替换后的字符串
repl：替换匹配的字符串的字符串
count：匹配的最大替换次数
"""
lss = re.sub(r'[1-9]\d{5}', ':zipcode', 'mit458995 ssa894164')
print(lss)
