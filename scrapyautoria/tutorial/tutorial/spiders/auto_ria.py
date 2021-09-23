import scrapy
import json

from tutorial.items import TutorialItem

class AutoRia(scrapy.Spider):
    name = 'auto_ria'
    allowed_domains = ['auto.ria.com']
    start_urls = [
        'https://auto.ria.com/uk/legkovie/tesla/'
    ]

    site_url = 'https://auto.ria.com/uk/'

    def parse(self, response):

        for car in response.css('div.content'):
            model = car.css('div > div > span.blue.bold::text').get()
            # 'year' : cars.css('div > item ticket-title > a.span::text').get(),
            mileage = car.css('div > ul > li > i.icon-mileage::text').get()
            # 'price_uah' : cars.css('div > item ticket-title > a.span::text').get(),
            # 'price_dollar' : cars.css('div > item ticket-title > a.span::text').get(),
            # 'vin_code' : cars.css('div > item ticket-title > a.span::text').get(),
            # 'link' : cars.css('div > item ticket-title > a.span::text').get(),

            car_item = TutorialItem()
            car_item['model'] = model.strip()
            car_item['mileage'] = mileage.strip()


            next_page = response.css('span.page-item.next.text-r a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)

            filename = "auto_ria.json"
            with open(filename, "w", encoding="utf8") as f:
                f.write(json.dumps(vars(car_item), ensure_ascii=False))
                self.log(f"Saved file {filename}")
