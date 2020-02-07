# -*- coding: utf-8 -*-
import scrapy
from myspider.items import MyspiderItem
import json
import re
import urllib.request

class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['xl.16888.com']
    start_urls = ['https://xl.16888.com/brand.html']

    def parse(self, response):
        item = {}
        tr_list = response.xpath("//html/body/div[5]/div[3]/div[2]/div/div[3]/div[1]/table/tr")
        
        for tr in tr_list[1:]:
    
            item["B_rank"] = tr.xpath("./td/text()").extract()[0] # 排名
            item["B_logo"] = tr.xpath("./td/a/img/@src").extract()[0] # 品牌logo链接
            item["B_name"] = tr.xpath("./td/a/text()").extract()[0] # 品牌名称
            item["B_country"] = tr.xpath("./td/text()").extract()[1] # 国别
            item["B_market_share"] = tr.xpath("./td/text()").extract()[3] # 占品牌份额
            item["B_sale_link"] = 'https://xl.16888.com'+tr.xpath("./td/div/a/@href").extract()[0] # 销量链接
            # 点进链接
            yield scrapy.Request(url = item["B_sale_link"], callback = self.parse_sale, meta=item)#, dont_filter=True)
        
        yield scrapy.Request(url = "https://xl.16888.com/brand-2.html", callback = self.parse)#, dont_filter=True)

        
            

    def parse_sale(self, response):
        item = MyspiderItem()
        item._values = response.meta

        tr_list = response.xpath("/html/body/div[5]/div[3]/div[2]/div/div[2]/div[1]/table/tr")
        item["B_S_date"] = []
        item["B_S_sale"] = []
        item["B_S_share"] = []
        item["B_S_detail"] = []
        for tr in tr_list[1: ]:

            item["B_S_date"].append(tr.xpath("./td/text()").extract()[0]) # 时间数组
            item["B_S_sale"].append(tr.xpath("./td/text()").extract()[1]) # 相应时间销量数组
            item["B_S_share"].append(tr.xpath("./td/text()").extract()[2]) # 相应时间市场份额数组
            item["B_S_detail"].append('https://xl.16888.com'+tr.xpath("./td/a/@href").extract()[0]) # 相应时间市场份额链接数组
        
        yield item
    

