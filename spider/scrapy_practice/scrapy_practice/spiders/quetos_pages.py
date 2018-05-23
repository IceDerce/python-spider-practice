# -*- coding: utf-8 -*-
import scrapy
'''顺页面顺序爬取'''


class QuetosPagesSpider(scrapy.Spider):
    name = 'quetos_pages'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        """
        下面部分的内容为，scrapy的翻页爬取

        使用scrapy crawl quetos_pages -o queto_pages.json 命令输出结果
        """

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

        """
        也可以使用<response.follow>来取代<response.urljoin>和<scrapy.Request>
          注意：下述写法
        """
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        """
        上述为列表形式赋予<response.follow>,而下面的形式是用selector赋予
        注意：用下属的写法更简单
        """
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, callback=self.parse)
