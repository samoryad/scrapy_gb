from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapers import settings
from scrapers.spiders.labirintru import LabirintruSpider
from scrapers.spiders.leroymerlin import LeroymerlinSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    # process.crawl(LabirintruSpider)
    search = 'плитка'
    process.crawl(LeroymerlinSpider, search=search)

    process.start()
