# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['python123.io']
    start_urls = ['http://python123.io/ws/demo.html']

    def parse(self, response):
        """
        parse()用于处理响应，解析内容形成字典，发现新的URL爬取请求

        被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。
        该方法负责解析返回的数据(response data)，
        提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象。

        :param response: 从网络中返回内容所存储的对象
        :return:
        """
        # 这个函数从response.url中提取倒数第一个斜杠之后的部分
        # 比如http://www.abc.com/ 123.zip，得到文件名123.zip
        fname = response.url.split('/')[-1]
        # 打开这个文件读取内容，并且将它返回，作为response.body输出
        with open(fname, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s.' % fname)
