# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class China_StudentProjectItem(scrapy.Item):
    name = scrapy.Field()
    school = scrapy.Field()
    address = scrapy.Field()
    direction = scrapy.Field()
    industry = scrapy.Field()
    introduce = scrapy.Field()
    url = scrapy.Field()

