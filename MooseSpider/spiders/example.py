# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request

from scrapy import signals

from MooseSpider.items import MoosespiderItem

class ExampleSpider(scrapy.Spider):
    name = 'example'

    allowed_domains = ['www.wanshifu.com']

    start_urls = ['https://www.wanshifu.com/']

    def parse(self, response):
        selector = Selector(response)
        category_list = selector.xpath("//div[@class='service-content-inner']/section[@class='service-two-container']/ul[@class='category-list']/li").extract()

        for category in category_list:
            moose_item = MoosespiderItem()
            name = Selector(text=category).xpath("//p/span/text()").extract_first()
            if (name):
                yield MoosespiderItem(name=name)
    