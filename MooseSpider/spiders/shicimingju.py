# coding:utf-8
import logging
import re

import scrapy
from scrapy import Selector

from MooseSpider.items import ShiCiItem


class ShiCiMingJuSpider(scrapy.Spider):
    name = "ShiCiMingJuSpider"  # 爬虫名称

    allowed_domains = ['www.shicimingju.com']  # 允许爬取域名

    start_urls = ['https://www.shicimingju.com/chaxun/zuozhe/1.html']  # 开始爬取地址

    def parse(self, response):

        shici_item = ShiCiItem()  # 封装Item对象

        shici_item["type"] = 'poetry'  # Item 类型

        # xpath 解析作者
        poetry_author = response.xpath(
            "//div[@id='main_right']/div[@class='card about_zuozhe']/div[2]/div/h4/a/text()").extract_first()
        shici_item['poetry_author'] = poetry_author

        # 解析内容
        shici_content_list = response.xpath("//div[@id='main_left']/div[@class='card shici_card']/div").extract()
        for content_item in shici_content_list:
            list_num_info = Selector(text=content_item).xpath(
                "//div/div[@class='list_num_info']/text()").extract_first()
            if list_num_info is not None:
                list_num_info = str.strip(list_num_info)
                shici_item["poetry_num"] = list_num_info
            # 解析诗名
            poetry_name = Selector(text=content_item).xpath(
                "//div/div[@class='shici_list_main']/h3/a/text()").extract_first()
            if poetry_name is not None:
                shici_item["poetry_name"] = poetry_name

            # 解析诗内容
            shici_content_more = Selector(text=content_item).xpath("//div/div[@class='shici_list_main']/div").extract()
            for item in shici_content_more:
                html = Selector(text=item).xpath("//div[@class='shici_content']").extract_first()
                if html is not None:
                    pattern = re.compile(r'<[^>]+>', re.S)
                    poetry_content = pattern.sub("", html).replace("展开全文", "").replace("收起", "").replace("\n",
                                                                                                         "").replace(
                        " ", "")
                    shici_item['poetry_content'] = poetry_content

                    # 打印数据
                    logging.info(shici_item)

                    # 交给 Pipeline
                    yield shici_item

        # 获取下一页数据
        next_url = response.xpath(
            "//div[@id='main_left']/div[@id='list_nav']/div[@id='list_nav_part']/a[text()='下一页']/@href").extract_first()

        # 抓取下一页数据
        if next_url is not None:
            yield scrapy.Request(str.format("https://www.shicimingju.com{}", next_url), callback=self.parse,
                                 dont_filter=True)
