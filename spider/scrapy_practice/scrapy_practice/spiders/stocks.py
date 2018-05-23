# -*- coding: utf-8 -*-
import scrapy
import re


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    start_urls = ['http://quoto.eastmoney.com/stocklist.html']
    user_agent_list = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36']

    def parse(self, response):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'user_agent_list'
        }  # 构造请求头

        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r'[s][hz]\d{6}', href)[0]
                url = 'https://gupiao.baidu.com/stock/' + stock + ".html"
                yield scrapy.Request(url, callback=self.parse_stock, headers=headers)
            except:
                continue

    def parse_stock(self, response):

        infodic = {}
        stockinfo = response.css('.stock-bets')
        name = stockinfo.css('.bets-name').extract()[0]
        keylist = stockinfo.css('dt').extract()
        valuelist = stockinfo.css('dd').extract()

        for i in range(len(keylist)):
            key = re.findall(r'>.*</dt>', keylist[i])[0][1:-5]
            try:
                val = re.findall(r'\d+\.?.*</dd>', valuelist[i][0][0:-5])
            except:
                val = '--'
            infodic[key] = val

        infodic.update(
            {'股票名称': re.findall('\s.*\(', name)[0].split()[0] + re.findall('\>.*\<', name)[0][1:-1]}
        )
        yield infodic

