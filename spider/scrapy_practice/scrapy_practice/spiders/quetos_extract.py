# -*- coding: utf-8 -*-
import scrapy
'''以JSON格式导出爬取内容'''


class QuetosExtractSpider(scrapy.Spider):
    name = 'quetos_extract'

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        """
        上面代码的含义是，将html中<div class="quote">内包含的
        <text><author><tags>都保存到items中

        并且在外加命令 scrapy crawl quotes -o quotes.json 后
        保存到名为quotes.json的文件中
        """
