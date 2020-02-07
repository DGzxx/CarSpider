# -*- coding: utf-8 -*-
import scrapy
from myspider.items import MyspiderItem
import json
import re
import urllib.request

class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['http://db.auto.sohu.com/']
    #start_urls = ['http://db.auto.sohu.com/brand_191/salesbrand.shtml']
    all_urls = []
    cur_id = 0
    urls_num = 0
    with open('all_urls.json') as fr:
        all_urls = json.load(fr)
    start_urls = ['http:'+all_urls[cur_id]]
    urls_num = len(all_urls)
    print("number of car type(item)", urls_num)

    def parse(self, response):
        '''
        links = response.xpath('//*[contains(@class, "model-a")]')
        for link in links:
            #print("!!!!")
            #print(link.css('a::attr(href)').extract())
            self.all_urls.append(link.css('a::attr(href)').extract()[0])
        self.urls_num = len(self.all_urls)
        print("total type number:", self.urls_num)
        with open('./all_urls.json', 'w') as fw:
            json.dump(self.all_urls, fw)
        '''
        item = MyspiderItem()
        try:
            item["car_brand1"] = response.xpath('//*[@id="content"]/div[1]/a[5]/text()').extract()[0][:-2]
        except:
            item["car_brand1"] = None
        try:
            item["car_brand2"] = response.xpath('//*[@id="content"]/div[1]/a[6]/text()').extract()[0][:-2]
        except:
            item["car_brand2"] = None
        try:
            item["car_types"] = response.xpath('//*[@id="content"]/div[1]/a[7]/text()').extract()[0][:-2]
        except:
            item["car_types"] = None
        try:
            item["car_url"] = "http:"+response.xpath('//*[@id="content"]/div[1]/a[7]').css('a::attr(href)').extract()[0]
        except:
            item["car_url"] = None

        url = self.all_urls[self.cur_id]
        car_id = re.search('model_([0-9]*)/', url).group(1)
        api_url = 'http://db.auto.sohu.com/api/newSales/model?modelIds='+str(car_id)+'&section=0'
        try:
            html = urllib.request.urlopen(api_url).read().decode('utf-8')
            cars = json.loads(html)["result"][0]["salesList"]
            item["year"] = []
            item["sale"] = []
            for car in cars:
                item["year"].append(car["xTime"])
                item["sale"].append(car["y"])
            yield item
        except:
            pass
        #table = response.xpath('//*[contains(@class, "salenum")]')
        #item["year"] = table.xpath('./tbody/tr/th/text()').extract()[1:]
        #row2 = table.xpath('./tbody/tr')[1].xpath('./td/text()').extract()
        #item["project"] = row2[0]
        #item["sale"] = row2[1:]

        
        '''
        #item["market_share"] = []
        # 提取饼图份额
        
        url = self.all_urls[self.cur_id]
        car_id = re.search('model_([0-9]*)/', url).group(1)
        sales_url = 'http://db.auto.sohu.com/cxdata/json/corp/'+str(car_id)+'CorpModelChart.json'
        try:
            html = urllib.request.urlopen(sales_url).read().decode('utf-8')
            cars = json.loads(html)["elements"][0]["values"]
            for car in cars:
                item["market_share"].append(car["label"])
                item["market_share"].append(car["value"])
            yield item
        except:
            pass
        '''
        if self.cur_id < self.urls_num:
            self.cur_id += 1
        #print('http:'+self.all_urls[self.cur_id])
        
        yield scrapy.Request('http:'+self.all_urls[self.cur_id], callback = self.parse, dont_filter=True)
    

