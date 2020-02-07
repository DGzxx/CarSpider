# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.utils.project import get_project_settings


class MyspiderPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]
        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库表名
        self.post = mydb[sheetname]
        #self.post.drop()
        #self.post = mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        #with open('cars_name.txt', 'a', encoding='utf-8') as fr:
        #    fr.write(data["car_brand1"]+" "+data["car_types"]+"\n")
        self.post.update_one({"car_url": data["car_url"]},{'$set':data},True)
        return item