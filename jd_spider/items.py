# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #用户ID
    id = scrapy.Field()
    #评论创建时间
    creationTime = scrapy.Field()
    #型号
    referenceName = scrapy.Field()
    #评论内容
    content = scrapy.Field()





