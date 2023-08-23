# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
from supabase import create_client, Client

class BooksPipeline(object):
    def process_item(self, item, spider):
        return item

class SavingToSupabasePipeline(object):
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        self.connection: Client = create_client(url, key)
        self.curr = self.connection.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        #we need to return the item below as scrapy expects us to!
        return item

    def store_db(self, item):
        try:
            self.insert({"id": 1, "name": item["name"], price: item["price"], url: item["url"]})

        except BaseException as e:
            print(e)
            self.connection.execute()
