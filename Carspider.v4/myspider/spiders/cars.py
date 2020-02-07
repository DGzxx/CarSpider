# -*- coding: utf-8 -*-
import scrapy
from myspider.items import MyspiderItem
import json
import re
import urllib.request

class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['xl.16888.com']
    start_urls = ['https://xl.16888.com/style.html']
    page_num = 11
    cur_page = 1

    def parse(self, response):
        item = {}
        tr_list = response.xpath("/html/body/div[5]/div[3]/div[2]/div/div[2]/div[1]/table/tr")
        
        for tr in tr_list[1:]:
    
            item["S_rank"] = tr.xpath("./td/text()").extract()[0] # 排名
            item["S_name"] = tr.xpath("./td/a/text()").extract()[0] # 车型
            item["S_manafacturer"] = tr.xpath("./td/a/text()").extract()[1] # 厂商
            item["S_price"] = tr.xpath("./td/a/text()").extract()[2] # 售价
            item["S_sale_link"] = 'https://xl.16888.com'+tr.xpath("./td/div/a/@href").extract()[0] # 销量链接
            # 点进链接
            yield scrapy.Request(url = item["S_sale_link"], callback = self.parse_sale, meta=item)#, dont_filter=True)
        
        if self.cur_page < self.page_num:
            self.cur_page += 1
        yield scrapy.Request(url = "https://xl.16888.com/style-"+str(self.cur_page)+".html", callback = self.parse)#, dont_filter=True)

    def parse_sale(self, response):
        item = MyspiderItem()
        item._values = response.meta

        tr_list = response.xpath("/html/body/div[5]/div[3]/div[2]/div/div[2]/div[1]/table/tr")
        item["S_S_date"] = []
        item["S_S_M_sale"] = []
        item["S_S_M_rank"] = []
        item["S_S_rank"] = []
        for tr in tr_list[1: ]:

            item["S_S_date"].append(tr.xpath("./td/text()").extract()[0]) # 时间数组
            item["S_S_M_sale"].append(tr.xpath("./td/text()").extract()[1]) # 相应时间月销量数组
            item["S_S_M_rank"].append(tr.xpath("./td/a/text()").extract()[0]) # 相应时间月销量排名数组
            item["S_S_rank"].append(tr.xpath("./td/text()").extract()[2]) # 相应时间占厂商份额数组
        
        yield item
    

