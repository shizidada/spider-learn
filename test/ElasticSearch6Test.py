# coding:utf-8
import json

from elasticsearch6 import Elasticsearch

ES_URL = [
    '127.0.0.1:9200'
]

es = Elasticsearch(ES_URL)


class Article:
    name = ""
    author = ""


def test_ping():
    pong = es.ping()
    print(pong)


def test_create_index():
    is_create = es.create(index="shicimingju", doc_type="shici", id=1, body={})
    print(is_create)


def test_index():
    article = Article()
    article.name = "《今日你吃饭了吗》"
    article.author = '江景'
    is_create = es.index(index="shicimingju", doc_type="shici_spider", body=json.dumps(article.__dict__))
    print(is_create)


test_index()
