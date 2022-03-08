# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class ScrapersPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.labirintru_books

    def process_item(self, item, spider):
        item['full_price'] = self.str_to_int(item['full_price'])
        item['discount_price'] = self.str_to_int(item['discount_price'])
        collection = self.mongobase[spider.name]
        collection.insert_one(item)
        return item

    def str_to_int(self, string):
        return int(string)
