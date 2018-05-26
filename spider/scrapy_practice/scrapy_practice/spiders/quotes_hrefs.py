# -*- coding: utf-8 -*-
import scrapy
'''顺链接爬取和回调机制'''


class AuthorSpider(scrapy.Spider):
    name = 'quetos_hrefs'

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # 爬取作者链接
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse_author)

        # 爬取分页链接
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            """
            一个辅助函数，用于从CSS查询中提取和清理数据并生成带有作者数据的Python字典
            这个蜘蛛演示的另一个有趣的事情是，即使有来自同一作者的许多引用，我们也不必担心多次
            访问相同的作者页面。默认情况下，Scrapy会将重复的请求过滤到已访问的URL中，避免因
            编程错误而导致服务器过多的问题。
            :param query:
            :return:
            """
            return response.css(query).extract_first().strip()

        # 注意看这里的extract方式，和前面的方式有所区别
        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }
