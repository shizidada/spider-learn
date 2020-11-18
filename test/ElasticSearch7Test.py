# coding:utf-8
import json

from elasticsearch7 import Elasticsearch

# /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/
from MooseSpider.items import ShiCiItem

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


def test_delete(index):
    if not es.indices.exists(index):
        return False
    else:
        res = es.indices.delete(index=index)
        return res['acknowledged']


def test_create_index():
    body = {"name": "tom", "age": 18, "height": 178}
    is_create = es.create(index="student", id=1, body=body)
    print(is_create)


def test_add():
    item = ShiCiItem()
    item['poetry_name'] = "《今日你吃饭了吗》"
    item['poetry_author'] = '江景'
    item['poetry_content'] = "今日你吃饭了吗?今日你吃饭了吗??"
    is_create = es.index(index="shi_ci_ming_ju", id=12, body=json.dumps(item.__dict__))
    print(is_create)


def test_search():
    res = es.search(index="shi_ci_ming_ju")
    for item in res['hits']['hits']:
        print(item['_source'])


def test_search_condition():
    res = es.search(index="shi_ci_ming_ju")
    for item in res['hits']['hits']:
        print(item['_source'])


# test_create_index();
# test_delete("shi_ci_ming_ju")
# test_add()
# test_search()
test_add()

