# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

from MooseSpider.items import VideoItem


class InSiJiSpider(scrapy.Spider):
    name = 'InSiJiSpider'

    prefix_url = 'https://www.insiji.com'

    # https://www.insiji.com/index.php/vod/type/id/6.html
    allowed_domains = ['www.insiji.com']

    start_urls = ['https://www.insiji.com/index.php/vod/type/id/6.html']

    def parse(self, response):
        video_model = VideoItem()

        video_container = response.xpath(
            "//div[@class='fed-main-info fed-min-width']/div[@class='fed-part-case']/div[@class='fed-part-layout fed-back-whits']")
        video_item_list = video_container.xpath("//ul[@class='fed-list-info fed-part-rows']/li").extract()
        for video_item in video_item_list:
            video_detail_url = Selector(text=video_item).xpath(
                "//a[@class='fed-list-title fed-font-xiv fed-text-center fed-text-sm-left fed-visible fed-part-eone']/@href").extract_first()
            video_title = Selector(text=video_item).xpath(
                "//a[@class='fed-list-title fed-font-xiv fed-text-center fed-text-sm-left fed-visible fed-part-eone']/text()").extract_first()
            video_desc = Selector(text=video_item).xpath(
                "//span[@class='fed-list-desc fed-font-xii fed-visible fed-part-eone fed-text-muted fed-hide-xs fed-show-sm-block']/text()").extract_first()

            if video_detail_url is not None:
                video_model['video_url'] = self.prefix_url + video_detail_url

            if video_title is not None:
                video_model['video_title'] = video_title

            if video_desc is not None:
                video_model['video_desc'] = video_desc
            # yield video_model
            print(video_model)
        #
        # next_page_url = video_container.xpath(
        #     "//div[@class='fed-page-info fed-text-center']/a[text()='下页']/@href").extract_first()
        # if next_page_url is not None:
        #     next_page_url = self.prefix_url + next_page_url
        #     yield scrapy.Request(next_page_url, callback=self.parse, dont_filter=True)
