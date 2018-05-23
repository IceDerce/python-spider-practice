import requests
from bs4 import BeautifulSoup
import bs4


def gethtmltext(url):
    try:
        r = requests.get(url, timeout=300)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def filllist(ulist, html):
    """
    找到每一个tbody标签中的tr标签，并在tr标签中找到td标签
    将td标签内的内容添加到，ulist列表中
    """
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])
        #  这里如何实现，将所有的td标签全都写入到ulist中？


def printlist(ulist, num):
    tplit = "{:^10}\t{1:{3}^10}\t{:^10}"
    print(tplit.format("排名", "学校名称", "总分", chr(12288)))
    # 需要填充时，选用chr(12288)中文空格填充
    for i in range(num):
        u = ulist[i]
        print(tplit.format(u[0], u[1], u[3], chr(12288)))
        # 需要填充时，选用chr(12288)中文空格填充


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html'
    html = gethtmltext(url)
    filllist(uinfo, html)
    printlist(uinfo, 20)  # 打印前十的大学


main()
