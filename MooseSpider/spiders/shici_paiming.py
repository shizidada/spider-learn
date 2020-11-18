# coding:utf-8
import scrapy


class ShiCiPaiMing(scrapy.Spider):
    name = "ShiCiPaiMing"

    allowed_domains = ['www.shicimingju.com']

    start_urls = ['https://www.shicimingju.com/paiming']

    def parse(self, response):
        print(response.body)
        pass
