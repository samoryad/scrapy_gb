from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

# from . import settings
# from .spiders.labirintru import LabirintruSpider
# from jobparser.spiders.sjru import SjruSpider
from bookparser.bookparser import settings
from bookparser.bookparser.spiders.labirintru import LabirintruSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LabirintruSpider)
    # process.crawl(SjruSpider)

    process.start()
