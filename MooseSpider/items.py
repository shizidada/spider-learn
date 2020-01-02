# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MoosespiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class NeteaseMusicItem(scrapy.Item):
    # define the fields for your item here like:
    hot_num = scrapy.Field()
    hot_rk = scrapy.Field()
    song_pic = scrapy.Field()
    song_name = scrapy.Field()
    song_time = scrapy.Field()
    singer_name = scrapy.Field()
    pass