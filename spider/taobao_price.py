import requests
import re


def geturl(url):
    try:
        r = requests.get(url, timeout=300)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def searchurl(ilit, html):
    try:
        pricelist = re.findall(r'"view_price":"[\d.]*"', html)
        namelist = re.findall(r'"raw_title":".*?"', html)
        for i in range(len(pricelist)):
            price = eval(pricelist[i].split(':')[1])
            title = eval(namelist[i].split(':')[1])
            ilit.append([price, title])
    except:
        print("")


def printlist(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "商品价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = '蚊帐'
    depth = 5
    start_url = 'https://s.taobao.com/search?q=' + goods
    infolist = []
    for i in range(depth):
        try:
            url = start_url + '&s=' +str(44*i)
            html = geturl(url)
            searchurl(infolist, html)
        except:
            continue
    printlist(infolist)


main()
