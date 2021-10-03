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

            # catalogSearchAT > div.standart-view.m-view.result-explore > section.ticket-item.visited > div.content-bar > div.content > div.head-ticket > div > a

            model = car.css('div.head-ticket > div > a > span::text').get()
            year = car.css('div.head-ticket > div > a::text').get()
            mileage = car.css('div.definition-data > ul > li.item-char.js-race::text').get().strip()
            price_uah = car.css('div.price-ticket > span > span.i-block > span::text').get().strip()
            price_dollar = car.css('div.price-ticket > span > span:nth-child(1)::text').get().strip()
            vin_code = car.css('div.definition-data > div > span.label-vin > span:nth-child(2)::text').get().strip()
            link = car.css('div.head-ticket > div > a::attr(href)').get().strip()

            car_item = TutorialItem()
            car_item['model'] = model.strip()
            car_item['year'] = year.strip()
            car_item['mileage'] = mileage.strip()
            car_item['price_uah'] = price_uah.strip()
            car_item['price_dollar'] = price_dollar.strip()
            car_item['vin_code'] = vin_code.strip() if vin_code else None
            car_item['link'] = link.strip()

            next_page = response.css('pagination > nav > span.page-item.next.text-r > a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)

            filename = "auto_ria.json"
            with open(filename, "w", encoding="utf8") as f:
                f.write(json.dumps(vars(car_item), ensure_ascii=False))
                self.log(f"Saved file {filename}")
