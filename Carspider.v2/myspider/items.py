# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    car_brand1 = scrapy.Field()
    car_brand2 = scrapy.Field()
    car_types = scrapy.Field()
    car_url = scrapy.Field()
    project = scrapy.Field()
    year = scrapy.Field()
    sale = scrapy.Field()
    #market_share = scrapy.Field()


