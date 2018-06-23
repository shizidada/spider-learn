import scrapy

from scrapy.http import Request


class TestSpider(scrapy.Spider):
    name = "TestSpider"

    start_urls = ["http://stackoverflow.com/questions?sort=votes"]

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield Request(full_url, callback=self.parse_info)  # 这个方法会直接产出
            # print(full_url)

    def parse_info(self, response):
        yield {
            'title': response.css('h1 a::text').extract()[0],
            'votes': response.css('.question .vote-count-post::text').extract()[0],
            'body': response.css('.question .post-text').extract()[0],
            'tags': response.css('.question .post-tag::text').extract(),
            'link': response.url,
        }
