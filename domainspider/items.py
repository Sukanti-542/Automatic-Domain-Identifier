# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DomainSpiderItem(scrapy.Item):
    # define the custom fields for your item here like:
    words = scrapy.Field()
    page = scrapy.Field()
    domain = scrapy.Field()

    pass
