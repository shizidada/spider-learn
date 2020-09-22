# coding:utf-8
import re
import scrapy
from scrapy import Selector

from MooseSpider.items import ShiCiItem


class ShiCiMingJuSpider(scrapy.Spider):
    name = "ShiCiMingJuSpider"

    allowed_domains = ['www.shicimingju.com']

    start_urls = ['https://www.shicimingju.com/chaxun/zuozhe/1.html']

    def parse(self, response):

        shici_item = ShiCiItem()

        shici_item["type"] = 'poetry'

        poetry_author = response.xpath(
            "//div[@id='main_right']/div[@class='card about_zuozhe']/div[2]/div/h4/a/text()").extract_first()
        shici_item['poetry_author'] = poetry_author

        shici_content_list = response.xpath("//div[@id='main_left']/div[@class='card shici_card']/div").extract()
        for content_item in shici_content_list:
            list_num_info = Selector(text=content_item).xpath(
                "//div/div[@class='list_num_info']/text()").extract_first()
            if list_num_info is not None:
                list_num_info = str.strip(list_num_info)
                shici_item["poetry_num"] = list_num_info

            poetry_name = Selector(text=content_item).xpath(
                "//div/div[@class='shici_list_main']/h3/a/text()").extract_first()
            if poetry_name is not None:
                shici_item["poetry_name"] = poetry_name

            shici_content_more = Selector(text=content_item).xpath("//div/div[@class='shici_list_main']/div").extract()
            for item in shici_content_more:
                html = Selector(text=item).xpath("//div[@class='shici_content']").extract_first()
                if html is not None:
                    pattern = re.compile(r'<[^>]+>', re.S)
                    poetry_content = pattern.sub("", html).replace("展开全文", "").replace("收起", "").replace(" ", "")
                    shici_item['poetry_content'] = poetry_content
                    yield shici_item

        next_url = response.xpath(
            "//div[@id='main_left']/div[@id='list_nav']/div[@id='list_nav_part']/a[text()='下一页']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(str.format("https://www.shicimingju.com{}", next_url), callback=self.parse,
                                 dont_filter=True)
