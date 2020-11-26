# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

'''
<a href="/html/gndy/rihan/index.html">日韩电影</a>
<a href="/html/gndy/oumei/index.html">欧美电影</a>
<a href="/html/gndy/china/index.html">国内电影</a>
<a href="/html/gndy/jddy/index.html">综合电影</a>
'''


class DianYingTianTangSpider(scrapy.Spider):
    name = 'DianYingTianTangSpider'

    prefix_url = 'https://www.dytt8.net/html/gndy/dyzz/'

    allowed_domains = ['https://www.dytt8.net']

    start_urls = ['{}index.html'.format(prefix_url)]

    def parse(self, response):
        # xpath /html/body/div[1]/div/div[3]/div[3]/div[2]/div[2]/div[2]/ul/table[1]
        # content_list = response.xpath("/html/body/div[1]/div/div[3]/div[3]/div[2]/div[2]/div[2]/ul/td/table").extract()
        # for item in content_list:
        #     movie_url = Selector(text=item).xpath("//tr[2]/td[2]/b/a/@href").extract_first()
        #     movie_name = Selector(text=item).xpath("//tr[2]/td[2]/b/a/text()").extract_first()
        #     movie_time = Selector(text=item).xpath("//tr[3]/td[2]/font/text()").extract_first()
        #     movie_desc = Selector(text=item).xpath("//tr[4]/td/text()").extract_first()

        next_page_url = response.xpath(
            "/html/body/div[1]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div/td/a[text()='下一页']/@href").extract_first()
        if next_page_url is not None:
            next_page_url = self.prefix_url + next_page_url
            print(next_page_url)
            yield scrapy.Request(next_page_url, callback=self.parse, dont_filter=True)
