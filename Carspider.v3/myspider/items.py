# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    B_rank = scrapy.Field()
    B_logo = scrapy.Field()
    B_name = scrapy.Field()
    B_country = scrapy.Field()
    B_market_share = scrapy.Field()
    B_sale_link = scrapy.Field()
    B_S_date = scrapy.Field()
    B_S_sale = scrapy.Field()
    B_S_share = scrapy.Field()
    B_S_detail = scrapy.Field()
    
    

