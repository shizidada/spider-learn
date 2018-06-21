# -*- coding: utf-8 -*-
import scrapy


class BaxxLearnSpider(scrapy.Spider):
    name = 'BaxxLearnSpider'
    allowed_domains = ['buaixuexi.club']
    start_urls = ['http://buaixuexi.club/']

    def parse(self, response):
        title = response.css("title::text").extract()[0]
        print title
        pass
