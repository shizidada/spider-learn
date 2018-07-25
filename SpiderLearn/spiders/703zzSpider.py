# -*- coding: utf-8 -*-

import scrapy


class Seven03zzSpider(scrapy.Spider):
    name = 'Seven03zzSpider'

    # start_urls = ["https://www.703zz.com/htm/index.htm"]
    # start_urls = ["https://www.703zz.com/htm/sp.htm"]
    # /htm/movielist1/
    # /htm/movielist2/
    # /htm/movielist3/
    # start_urls = ["https://www.703zz.com/htm/novellist1"]

    # def __init__(self):
    #     self.base_url = 'https://www.703zz.com'
    #
    # def parse(self, response):
    #     # print(response.body.decode())
    #     # print(help(response))
    #     print(response.text)
