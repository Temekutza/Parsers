import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class EmaelSpider(CrawlSpider):
    name = 'all_enamel'
    start_urls = ['https://nn.russcvet.ru/catalog/enamels/']

    rules = (
        Rule(LinkExtractor(allow='catalog')),
        Rule(LinkExtractor(allow='enamels'), callback='parse_items')
    )

    def parse_items (self, response):
        yield{
            'Name': response.css('h1::text').get().split()[1],
            'Price': response.css('.price span::text').get()
        }


# scrapy crawl all_enamel -o all_enamel.csv
