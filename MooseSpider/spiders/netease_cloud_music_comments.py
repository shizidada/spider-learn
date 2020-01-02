# coding:utf-8

import scrapy
from scrapy.selector import Selector
import os


class NeteaseCloudMusicSpider(scrapy.Spider):

    name = "NeteaseCloudMusicSpider"

    allowed_domains = ['music.163.com']

    start_urls = ['https://music.163.com/#/discover/toplist?id=19723756']

    def parse(self, response):
        html_list = response.xpath("//div[@id='toplist']/div[@class='g-mn3']/div[@class='g-mn3c']/div[@class='g-wrap12']/div[@id='song-list-pre-cache']/div/div[@class='j-flag']/table/tbody/tr").extract()
        for item in html_list:
          num = Selector(text=item).xpath("//tr/td[1]/div[@class='hd']/span/text()").extract()
          rk = Selector(text=item).xpath("//tr/td[1]/div[@class='hd']/div/span[@class='ico u-icn u-icn-73 s-fc9']/text()").extract()

          # num = Selector(text=item).xpath("//tr/td[2]/div[@class='hd']/span/text()").extract()
          # num = Selector(text=item).xpath("//tr/td[3]/div[@class='hd']/span/text()").extract()
          # num = Selector(text=item).xpath("//tr/td[4]/div[@class='hd']/span/text()").extract()
          print(num, rk)
        pass
