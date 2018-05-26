# -*- coding: utf-8 -*-
import scrapy
'''保存爬取页面为html'''


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        """
        多网页爬取的请求（静态多网页，需要提前输入）

        :return: scrapy.Request对象，并且调用与请求相关的回调方法（parse）
                ，将响应作为参数传递。
        """
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        """  
        上面代码的含义是将这两个网页保存下来，
        命名为，quetos-网址编号.html
        并且保存为文件
        """
