# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline


class ScrapersPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.scrapydb

    def process_item(self, item, spider):
        if spider.name == 'labirintru':
            item['full_price'] = self.str_to_int(item['full_price'])
            item['discount_price'] = self.str_to_int(item['discount_price'])
            collection = self.mongobase[spider.name]
            collection.insert_one(item)
            return item

        elif spider.name == 'leroymerlin':
            item['price'] = self.str_to_int(item['price'])
            collection = self.mongobase[spider.name]
            collection.insert_one(item)
            return item

    def str_to_int(self, string):
        if string is not None:
            return float(string)


class LeroymerlinPhotos(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for photo in item['photos']:
                try:
                    yield scrapy.Request(photo)
                except Exception as e:
                    print(e)

    # def file_path(self, request, response=None, info=None, *, item=None):
    #     pass

    def item_completed(self, results, item, info):
        item['photos'] = [item[1] for item in results if item[0]]
        return item
