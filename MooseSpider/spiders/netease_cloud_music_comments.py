# coding:utf-8

import scrapy
from scrapy.selector import Selector
from MooseSpider.items import NeteaseMusicCommentItem
import os


class NeteaseCloudMusicSpider(scrapy.Spider):

    name = "NeteaseCloudMusicCommentSpider"

    allowed_domains = ['music.163.com']

    start_urls = ['https://music.163.com/#/discover/toplist?id=19723756']

    def parse(self, response):
        # comments_count = response.xpath(
        #     "//div[@id='toplist']/div[@class='g-mn3']/div[@class='g-mn3c']/div[@class='g-wrap']/div[@class='m-info m-info-rank f-cb']/div[@class='cnt']/div[@class='cntc m-info']/div[@class='btns f-cb']/a[@class='u-btni u-btni-cmmt j-cmt']/i/span/text()"
        # ).extract_first()

        comments_list = response.xpath(
            "//div[@id='toplist']/div[@class='g-mn3']/div[@class='g-mn3c']/div[@class='g-wrap12']/div[@class='n-cmt']/div/div[@class='m-cmmt']/div[@class='cmmts j-flag']/div[@class='itm']"
        ).extract()

        for comment_item in comments_list:

            avator = Selector(text=comment_item).xpath(
                "//div[@class='itm']/div[@class='head']/a/img/@src"
            ).extract_first()

            user_id = Selector(text=comment_item).xpath(
                "//div[@class='itm']/div[@class='cntwrap']/div/div[@class='cnt f-brk']/a/@href"
            ).extract_first().split('=')[-1]

            user_name = Selector(text=comment_item).xpath(
                "//div[@class='itm']/div[@class='cntwrap']/div/div[@class='cnt f-brk']/a/text()"
            ).extract_first()

            comment_content = Selector(text=comment_item).xpath(
                "//div[@class='itm']/div[@class='cntwrap']/div/div[@class='cnt f-brk']/text()"
            ).extract_first().split('：')[-1]

            yield NeteaseMusicCommentItem(avator=avator,
                                          user_id=user_id,
                                          user_name=user_name,
                                          comment_content=comment_content)

            # TODO: 分页
