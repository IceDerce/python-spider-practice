# -*- coding: utf-8 -*-
import scrapy
"""
<div class="quote">
    <span class="text">“The world as we have created it is a process of our
    thinking. It cannot be changed without changing our thinking.”</span>
    <span>
        by <small class="author">Albert Einstein</small>
        <a href="/author/Albert-Einstein">(about)</a>
    </span>
    <div class="tags">
        Tags:
        <a class="tag" href="/tag/change/page/1/">change</a>
        <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
        <a class="tag" href="/tag/thinking/page/1/">thinking</a>
        <a class="tag" href="/tag/world/page/1/">world</a>
    </div>
</div>
以上为quotes.toscrape.com的部分内容
下面将会描述 如何从中提取信息
"""


class QuotesSelectorSpider(scrapy.Spider):
    name = 'quotes_selector'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        """提取标签<div class="quote">的表述方式"""
        queto = response.css("div.quote")[0]
        """提取标签<span class="text">的内容的表述"""
        title = queto.css("span.text::text").extract()[0]
        """提取标签<small class="author">的内容的表述"""
        author = queto.css("small.author::text").extract()[0]
        """提取Tags的内容的表述，注意tags为多目录，并且为列表形式"""
        tags = queto.css("div.tags a.tag::text").extract()

        # 这里需要留意，如何才能提取href中的信息？
        """下面演示，如何提取标签属性，如href的信息"""
        links = queto.css("div.tags a.tag::attr(href)").extract()[0]

        """用迭代的方式，将上述所有的信息装进字典中"""
        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").extract_first()
            author = quote.css("small.author::text").extract_first()
            tags = quote.css("div.tags a.tag::text").extract()
            print(dict(text=text, author=author, tags=tags))
