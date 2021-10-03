# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    model = scrapy.Field()
    year = scrapy.Field()
    mileage = scrapy.Field()
    price_uah = scrapy.Field()
    price_dollar = scrapy.Field()
    vin_code = scrapy.Field()
    link = scrapy.Field()
