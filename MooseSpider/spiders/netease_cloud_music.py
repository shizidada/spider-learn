# coding:utf-8

import scrapy
from scrapy.selector import Selector
from MooseSpider.items import NeteaseMusicItem
import os


class NeteaseCloudMusicSpider(scrapy.Spider):

    name = "NeteaseCloudMusicSpider"

    allowed_domains = ['music.163.com']

    start_urls = ['https://music.163.com/#/discover/toplist?id=19723756']

    def parse(self, response):
        html_list = response.xpath(
            "//div[@id='toplist']/div[@class='g-mn3']/div[@class='g-mn3c']/div[@class='g-wrap12']/div[@id='song-list-pre-cache']/div/div[@class='j-flag']/table/tbody/tr"
        ).extract()

        for item in html_list:
            music_item = NeteaseMusicItem()

            hot_num = Selector(
                text=item).xpath("//tr/td[1]/div[@class='hd']/span/text()"
                                 ).extract_first() or ''

            hot_rk = Selector(text=item).xpath(
                "//tr/td[1]/div[@class='hd']/div/span[@class='ico u-icn u-icn-73 s-fc9']/text()"
            ).extract_first() or ''

            song_pic = Selector(text=item).xpath(
                "//tr/td[2]/div[@class='f-cb']/div[@class='tt']/a/img/@src"
            ).extract_first() or ''

            song_name = Selector(text=item).xpath(
                "//tr/td[2]/div[@class='f-cb']/div[@class='tt']/div[@class='ttc']/span/a/b/@title"
            ).extract_first() or ''

            song_href = Selector(text=item).xpath(
                "//tr/td[2]/div[@class='f-cb']/div[@class='tt']/div[@class='ttc']/span/a/@href"
            ).extract_first()
            song_id = ''
            if song_href:
                song_id = song_href.split('=')[-1]

            song_time = Selector(text=item).xpath(
                "//tr/td[3]/span/text()").extract_first() or ''

            singer_name = Selector(text=item).xpath(
                "//tr/td[4]/div[@class='text']/@title").extract_first() or ''

            music_item['hot_num'] = hot_num
            music_item['hot_rk'] = hot_rk
            music_item['song_pic'] = song_pic
            music_item['song_name'] = song_name
            music_item['song_id'] = song_id
            music_item['song_time'] = song_time
            music_item['singer_name'] = singer_name
            yield music_item
