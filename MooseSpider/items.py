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
    type = scrapy.Field()
    hot_num = scrapy.Field()
    hot_rk = scrapy.Field()
    song_pic = scrapy.Field()
    song_name = scrapy.Field()
    song_id = scrapy.Field()
    song_time = scrapy.Field()
    singer_name = scrapy.Field()
    pass


class NeteaseMusicCommentItem(scrapy.Item):
    # define the fields for your item here like:
    type = scrapy.Field()
    avatar = scrapy.Field()
    user_id = scrapy.Field()
    user_name = scrapy.Field()
    comment_content = scrapy.Field()
    pass


class ShiCiItem(scrapy.Item):
    type = scrapy.Field()
    # 作者
    poetry_author = scrapy.Field()
    # 诗词名
    poetry_name = scrapy.Field()
    # 诗词内容
    poetry_content = scrapy.Field()
    # 诗词序号
    poetry_num = scrapy.Field()
