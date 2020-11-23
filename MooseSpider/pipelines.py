# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# import requests
from pymongo import MongoClient


# class MooseSpiderPipeline(object):
#     def open_spider(self, spider):
#         pass
#
#     def close_spider(self, spider):
#         pass
#
#     def process_item(self, item, spider):
#         self.download_video(item, spider)
#         return item
#
#     def download_video(self, item, spider):
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"}
#         video_url = item['video_url']
#         video_title = item['video_title']
#         r = requests.get(video_url, headers=headers)
#         save_path = 'E:\\Code\\python-workspace\\spider-learn\\MooseSpider\\mp4\\{}.{}'.format(video_title, "mp4")
#         save_path = save_path.strip()
#         with open(save_path, 'wb') as f:
#             f.write(r.content)

# class MooseSpiderPipeline(object):
#     # 云音乐飙升榜
#     collection_name = 'music_soaring_list_comments'
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(mongo_uri=crawler.settings.get('MONGO_URI'),
#                    mongo_db=crawler.settings.get('MONGO_DATABASE',
#                                                  'netease_cloud_musics'))
#
#     def __init__(self, mongo_uri, mongo_db):
#         self.client = MongoClient(mongo_uri)
#         self.db = self.client[mongo_db]
#         self.es_client = Elasticsearch([
#             '127.0.0.1:9200'
#         ])
#
#     def open_spider(self, spider):
#         pass
#
#     def close_spider(self, spider):
#         self.client.close()
#
#     def process_item(self, item, spider):
#         if item["type"] == "music_soaring_list_comments":
#             self.db[self.collection_name].insert_one(dict(item))
#         elif item["type"] == 'poetry':
#             self.process_shici_item(item, spider)
#         return item
#
#     def process_shici_item(self, item, spider):
#         # print(dict(item))
#         self.es_client.index(index="shi_ci_ming_ju", doc_type="poetry", body=dict(item))

class MooseSpiderPipeline(object):
    collection_name = 'shici_item'

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'),
                   mongo_db=crawler.settings.get('MONGO_DATABASE', 'shicimingju'))

    def __init__(self, mongo_uri, mongo_db):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[mongo_db]

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.process_video_item(item, spider)
        return item

    def process_video_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
