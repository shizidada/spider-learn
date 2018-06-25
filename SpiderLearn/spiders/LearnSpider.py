# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
import sys

from SpiderLearn.items import AoisolasItem


class LearnSpider(scrapy.Spider):

    name = 'LearnSpider'
    allowed_domains = ['lab.scrapyd.cn']

    # Scrapy 为 Spider 的 start_urls 属性中的每个URL创建了 scrapy.Request 对象
    # 并将 parse 方法作为回调函数(callback)赋值给了 Request
    # Request 对象经过调度，执行生成 scrapy.http.Response 对象并送回给spider parse() 方法。
    start_urls = ['http://lab.scrapyd.cn/']

    page_num = 1

    def parse(self, response):
        # texts = response.css("span.text::text").extract()
        # print(texts)

        self.page_num += 1

        selector = Selector(response)
        # divs = selector.xpath("//div[@class='quote post']").extract()
        divs = selector.xpath("//div[@class='quote post']").extract()
        for item in divs:
            # print(item)
            learn_item = AoisolasItem()

            text = Selector(text=item).xpath("//span[@class='text']/text()").extract()[0]
            author = Selector(text=item).xpath("//span/small[@class='author']/text()").extract()[0]

            learn_item["text"] = text
            learn_item["author"] = author

            yield learn_item

        if len(divs):
            yield Request(url='http://lab.scrapyd.cn/page/%s/' % self.page_num, callback=self.parse)
