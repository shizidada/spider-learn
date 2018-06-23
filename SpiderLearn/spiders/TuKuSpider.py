import scrapy
from scrapy.selector import Selector
from scrapy.http import Request


class TuKuSpider(scrapy.Spider):
    name = 'TuKuSpider'

    start_urls = ['https://www.zhainanfulishe.com/tuku']

    def parse(self, response):
        selector = Selector(response=response)
        # articles = selector.xpath('//div[@class="bloglist-container clr"]')
        hrefs = selector.xpath(
            '//div[@class="bloglist-container clr"]/article[@class="home-blog-entry col span_1 clr"]/a/@href')
        for href in hrefs:
            # 网页中 url 标签
            url = href.extract()
            yield Request(url=url, callback=self.parse_tuku)

    def parse_tuku(self, response):
        every_selecetor = Selector(response)

        img_url = every_selecetor.xpath('//div[@class="single-text"]/p/a/img/@src').extract()
        print(img_url)

        # print(response.css('title::text'))
