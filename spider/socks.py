import requests
from bs4 import BeautifulSoup
import traceback
import re


def geturl(url):
    try:
        r = requests.get(url, timeout=3000)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""


def getsockslist(list, stocksurl):
    """
    从股票编号网站爬取所有股票的编号

    :param list: 股票编号的列表
    :param stocksurl: 股票编号的网址
    :return:
    """
    html = geturl(stocksurl)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            list.append(re.findall(r'[s][hz]\d{6}', href)[0])
        except:
            continue


def getsocksinfo(list, stockurl, output_file):
    """
    得到股票编号，并到百度股票，查找这支股票的具体参数信息

    :param list: 股票编号列表
    :param stockurl: 股票查询网址
    :param output_file: 本地保存文件名
    :return:
    """
    count = 0
    for stock in list:
        url = stockurl + stock + ".html"
        html = geturl(url)
        try:
            if html == "":
                continue

            stocksinfodict = {}

            soup = BeautifulSoup(html, "html.parser")
            stockinfo = soup.find('div', attrs={'class': 'stock-bets'})

            name = stockinfo.find_all(attrs={'class': 'bets-name'})[0]
            stocksinfodict.update({'股票名称': name.text.split()[0]})

            keylist = stockinfo.find_all('dt')
            valuelist = stockinfo.find_all('dd')

            for i in range(len(keylist)):
                key = keylist[i].text
                val = valuelist[i].text
                stocksinfodict[key] = val

            with open(output_file, 'a', encoding='utf-8') as f:
                f.write(str(stocksinfodict) + '\n')
                count = count + 1
                print('\r当前进度:{:2f}%'.format(count*100/len(list)), end='')
        except:
            count = count + 1
            print('\r当前进度:{:2f}%'.format(count * 100 / len(list)), end='')
            traceback.print_exc()
            continue


def main():
    stock_list_url = 'http://quoto.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = '/home/zeaslity/Documents/stocks.txt'
    list = []
    getsockslist(list, stock_list_url)
    getsocksinfo(list, stock_info_url, output_file)


main()
