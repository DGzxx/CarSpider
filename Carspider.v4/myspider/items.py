# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    S_rank = scrapy.Field()
    S_name = scrapy.Field()
    S_manufacturer = scrapy.Field()
    S_price = scrapy.Field()
    S_sale_link = scrapy.Field()
    S_S_date = scrapy.Field()
    S_S_M_sale = scrapy.Field()
    S_S_M_rank = scrapy.Field()
    S_S_rank = scrapy.Field()


