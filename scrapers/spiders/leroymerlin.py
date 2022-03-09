import scrapy
from scrapy.http import HtmlResponse

from scrapers.items import ScrapersItem


class LeroymerlinSpider(scrapy.Spider):
    name = 'leroymerlin'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [
            f"https://leroymerlin.ru/search/?q={kwargs.get('search')}/"]

    def parse(self, response: HtmlResponse):
        # ограничил сбор данных пока двумя страницами (а то их более 100)
        next_page = response.xpath(
            "//a[@data-qa-pagination-item='right']/@href").get()
        if int(next_page.split('=')[-1]) <= 2:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath(
            "//a[contains(@data-qa, 'product-image')]/@href")
        for link in links:
            yield response.follow(link, callback=self.parse_materials)

    def parse_materials(self, response: HtmlResponse):
        name = response.xpath("//h1[@itemprop='name']/text()").get()
        url = response.url
        price = response.xpath(
            "//uc-pdp-price-view[@class='primary-price']/meta[@itemprop='price']/@content").get()
        currency = response.xpath(
            "//uc-pdp-price-view[@class='primary-price']/span[@slot='currency']/text()").get()
        photos = response.xpath(
            "//picture[@slot='pictures']//@src").getall()

        yield ScrapersItem(name=name, url=url, price=price, currency=currency, photos=photos)
