# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class KugoumusicPipeline(object):
    
    def open_spider(self, spider):
        mongo_config = spider.settings['MONGO_CONFIG']
        # host = '127.0.0.1', port = 27017
        # self.client = MongoClient(host='127.0.0.1', port=27017)
        self.client = MongoClient(**mongo_config)
        self.coll = self.client['student_db']['kugou']
        self.li = []
        
    def close_spider(self, spider):
        self.insert()
        self.client.close()
        
    def insert(self):
        self.coll.insert_many(self.li)
    
    def process_item(self, item, spider):
        if len(self.li) >= 100:
            self.insert()
            self.li = []
            print("成功插入100条数据-------------------------------------")
        else:
            self.li.append(dict(item))
        
        return item
