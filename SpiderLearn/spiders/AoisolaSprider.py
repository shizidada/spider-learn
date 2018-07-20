# -*- coding: utf-8 -*-

import scrapy


class AoisolaSprider(scrapy.Spider):
    name = 'AoisolaSprider'

    # start_urls = ['http://www.haoa19.com']
    # http://se.haoa19.com/

    # start_urls = ['http://se.haoa19.com/']
    # start_urls = ['http://dy.haoa19.com/']
    start_urls = ["http://se.haoa19.com/listhtml/12.html"]

    def __init__(self):
        self.base_url = 'http://se.haoa19.com'
        self.count = 0

    def parse(self, response):
        # print(response.body)
        # print(help(response))
        # print(response.text)
        list = response.xpath("//div[@class='list']/ul/li/a/@href")
        for item in list:
            # 获取媒体类容
            # print(url)
            url = self.base_url + item.extract()
            yield scrapy.Request(url=url, callback=self.process_content)
            # print(response.css("title::text")[0].extract())
            # print(response.xpath("//title/text()")[0].extract())

    def process_content(self, response):
        # print(response.text)
        self.count += 1

        with open(str(self.count) + ".txt", mode='a+', encoding='utf-8') as article:
            content = response.xpath("//div[@class='center margintop border clear main']/p")[0].extract()
            article.write(content)
