# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo


class MongodbPipeline(object):
    collection_name = "best_movies"    
    
    def open_spider(self, spider):
        # what database you are connecting to. Remember to edit password in here
        self.client = pymongo.MongoClient("mongodb+srv://einaras:<testtest>@cluster0-a2wki.mongodb.net/<dbname>?retryWrites=true&w=majority")
        # creating table in the databse?
        self.db = self.client["IMDB"]
    
    def close_spider(self, spider):
        self.client.close()
    
    def process_item(self, item, spider):
        # saving each item scraped into database
        self.db[self.collection_name].insert(item)
        return item
