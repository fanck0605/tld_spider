# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TLDItem(scrapy.Item):
    tld = scrapy.Field()
    type = scrapy.Field()
