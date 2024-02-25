# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LinkGraphItem(scrapy.Item):
    # define the fields for your item here like:
    source = scrapy.Field()
    target = scrapy.Field()
    pass
