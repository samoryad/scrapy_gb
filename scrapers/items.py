# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapersItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    rate = scrapy.Field()
    author = scrapy.Field()
    full_price = scrapy.Field()
    discount_price = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    url = scrapy.Field()
    photos = scrapy.Field()
    _id = scrapy.Field()
