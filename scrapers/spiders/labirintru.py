import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader

from scrapers.items import ScrapersItem


class LabirintruSpider(scrapy.Spider):
    name = 'labirintru'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/search/%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/?stype=0']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath(
            "//a[contains(@class, 'pagination-next__text')]/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath(
            "//a[contains(@class, 'product-title-link')]/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.book_parse)

    def book_parse(self, response: HtmlResponse):
        loader = ItemLoader(item=ScrapersItem(), response=response)
        loader.add_xpath('name', "//div[contains(@class, 'prodtitle')]/h1/text()")
        loader.add_xpath(
            'discount_price',
            "//span[contains(@class, 'buying-pricenew-val-number')]/text()")
        loader.add_xpath(
            'full_price',
            "//span[contains(@class, 'buying-priceold-val-number')]/text()")
        loader.add_xpath('currency', "//span[contains(@class, 'buying-pricenew-val-currency')]/text()")
        loader.add_xpath('rate', "//div[contains(@id, 'rate')]/text()")
        loader.add_xpath('author', "//a[contains(@data-event-label, 'author')]/text()")
        loader.add_value('url', response.url)
        loader.add_value('photos', 'None')

        yield loader.load_item()

        # реализация без ItemLoader, пока оставил
        # name = response.xpath(
        #     "//div[contains(@class, 'prodtitle')]/h1/text()").get()
        # discount_price = response.xpath(
        #     "//span[contains(@class, 'buying-pricenew-val-number')]/text()").get()
        # full_price = response.xpath(
        #     "//span[contains(@class, 'buying-priceold-val-number')]/text()").get()
        # currency = response.xpath(
        #     "//span[contains(@class, 'buying-pricenew-val-currency')]/text()").get()
        #
        # rate = response.xpath(
        #     "//div[contains(@id, 'rate')]/text()").get()
        # author = response.xpath(
        #     "//a[contains(@data-event-label, 'author')]/text()").get()
        #
        # url = response.url
        # yield ScrapersItem(name=name, author=author, rate=rate, full_price=full_price, discount_price=discount_price, currency=currency, url=url, photos=None)
