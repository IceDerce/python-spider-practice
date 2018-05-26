import requests
from bs4 import BeautifulSoup

def geturl(url):

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        "Accept-Language": "en-GB,en;q=0.5",
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
    }
    try:
        r = requests.get(url, headers=headers, timeout=300)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""


def searchurl(ilt, html):
    soup = BeautifulSoup(html, 'html.parser')

    pricelist = []
    namelist = []
    try:
        priceinfo = soup.find_all('div', attrs={'class': 'p-price'})
        # print(priceinfo)

        nameinfo = soup.find_all('div', attrs={'p-name p-name-type-2'})
        # print(nameinfo)

        for x in range(len(priceinfo)):
            pricelist.append(priceinfo[x].find('i').text)

        for x in range(len(nameinfo)):
            namelist.append(nameinfo[x].find('em').text)

        for i in range(len(pricelist)):
            price = pricelist[i]
            title = namelist[i]
            ilt.append([price, title])

        return ilt
    except:
        print('失败')



def printlist(ilt):
    tplt = "{:2}\t{:3}\t{:10}"
    print(tplt.format("序号", "商品价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    url = 'https://search.jd.com/search?keyword=SSD' \
          '&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=SSD&ev=1948_82060%5E539_826%' \
          '5E&wtype=1&0.35864972351771063#J_main'

    ilt = []
    html = geturl(url)
    searchurl(ilt, html)
    printlist(ilt)


main()
