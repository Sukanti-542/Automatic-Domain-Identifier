# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo


class DomainSpiderPipeline(object):

    def __init__(self):
        # Initiate the connection. Use the port on which your mongo db is running
        self.conn = pymongo.MongoClient('localhost', 27017)
        db = self.conn['mdomain']
        # Define the collection to be used/ created
        self.collection = db['dom_tb']
        print("Writing to DB")

    def process_item(self, item, spider):
        # Insert the data
        self.collection.insert(dict(item))
        return item
