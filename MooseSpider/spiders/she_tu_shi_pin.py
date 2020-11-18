# coding:utf-8
import scrapy
from scrapy import Selector

from MooseSpider.items import VideoItem


class ShiCiPaiMing(scrapy.Spider):
    name = "SheTuShiPin"

    prefix_url = 'https://699pic.com'

    allowed_domains = ['699pic.com']

    # https://699pic.com/video/338.html
    start_urls = ['https://699pic.com/video/18.html']

    def parse(self, response):
        # print(response.body)
        video_list = response.xpath(
            "//div[@class='search-video-wrap']/div[@class='video-list clearfix add-quick-recommend']/ul/li").extract()
        video_item = VideoItem()
        for item in video_list:
            video_url = Selector(text=item).xpath("//a/div[@class='video-box']/video/@data-original").extract_first()
            video_url = video_url.replace("_10s", "")
            video_item['video_url'] = 'https:' + video_url

            video_title = Selector(text=item).xpath("//a[@class='video-name fl']/h3/text()").extract_first()
            video_item['video_title'] = video_title

            video_time = Selector(text=item).xpath(
                "//a[@class='video-name fl']/span[@class='video-time']/text()").extract_first()
            video_item['video_time'] = video_time
            yield video_item
        # # 下一页 url
        # next_url = response.xpath("//div[@class='pagelist']/a[@class='downPage']/@href").extract_first()
        # if next_url is not None:
        #     print(self.prefix_url + next_url)
        #     yield scrapy.Request(self.prefix_url + next_url, callback=self.parse, dont_filter=True)
