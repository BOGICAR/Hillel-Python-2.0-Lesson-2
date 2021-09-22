import scrapy

class AutoRia(scrapy.Spider):
    name = 'autoria'
    allowed_domains = ['auto.ria.com']
    start_urls = [
        'https://auto.ria.com/uk/legkovie/tesla/'
    ]

    site_url = 'https://auto.ria.com/uk/'

    def parse(self, response):

        for cars in response.css('div.content-bar'):
            yield {
                'model' : cars.css('div.content div.head-ticket ')
                'year'
                'mileage'
                'price_uah'
                'price_dollar'
                'vin_code'
                'link'
            }
