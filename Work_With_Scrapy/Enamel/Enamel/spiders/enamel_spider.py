import scrapy

class EmaelSpider(scrapy.Spider):
    name = 'russcvet'
    start_urls = ['https://nn.russcvet.ru/catalog/enamels/']

    def parse(self, response):
        for link in response.css('div.catalog a::attr(href)'):
            yield response.follow(link, callback=self.parse_emael)
        
        for i in range (1, 17):
            next_page = f'https://nn.russcvet.ru/catalog/enamels/page-{i}/'
            yield response.follow(next_page, callback=self.parse)
    

    def parse_emael(self, response):

        yield{
            
            'Name': response.css('h1::text').get().split()[1],
            'Price':response.css('.price span::text').get()
        }



# scrapy crawl russcvet -o enamel.xlsx



    

