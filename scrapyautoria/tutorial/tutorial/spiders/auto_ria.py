import scrapy
import json

from tutorial.items import TutorialItem


class AutoRia(scrapy.Spider):
    name = 'auto_ria'
    allowed_domains = ['auto.ria.com']
    start_urls = ['https://auto.ria.com/uk/legkovie/tesla/']

    site_url = 'https://auto.ria.com/uk/'

    def parse(self, response):

        for car in response.css('div.content'):
            model = car.css('div.head-ticket > div > a > span > font > font::text').get()
            year = car.css('div.head-ticket > div > a > font > font::text').get()
            mileage = car.css('div.definition-data > ul > li.item-char.js-race > font > font::text').get()
            price_uah = car.css('div.price-ticket > span > span.i-block > span > font > font::text').get()
            price_dollar = car.css('div.price-ticket > span > span:nth-child(1) > font > font::text').get()
            vin_code = car.css('div.definition-data > div > span.label-vin > span:nth-child(2) > font > font::text').get()
            link = car.css('div.head-ticket > div > a::text').get()

            car_item = TutorialItem()
            car_item['model'] = model.strip()
            car_item['year'] = year.strip()
            car_item['mileage'] = mileage.strip()
            car_item['price_uah'] = price_uah.strip()
            car_item['price_dollar'] = price_dollar.strip()
            car_item['vin_code'] = vin_code.strip() if vin_code else None
            car_item['link'] = link.strip()

            next_page = response.css('span.page-item.next.text-r a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)

            filename = "auto_ria.json"
            with open(filename, "w", encoding="utf8") as f:
                f.write(json.dumps(vars(car_item), ensure_ascii=False))
                self.log(f"Saved file {filename}")
