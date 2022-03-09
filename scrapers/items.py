# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, Compose


def list_to_float(price_list):
    try:
        result = float(price_list[0])
        return result
    except Exception:
        return price_list


class ScrapersItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    rate = scrapy.Field(output_processor=Compose(list_to_float))
    author = scrapy.Field(output_processor=TakeFirst())
    full_price = scrapy.Field(output_processor=Compose(list_to_float))
    discount_price = scrapy.Field(output_processor=Compose(list_to_float))
    price = scrapy.Field(output_processor=Compose(list_to_float))
    currency = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field()
    photos = scrapy.Field()
    _id = scrapy.Field()
