# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ProxyItem(scrapy.Item):
    # ip地址
    ip = scrapy.Field()
    # 端口
    port = scrapy.Field()
    # 速度
    speed = scrapy.Field()
    # 连接时间
    connect_time = scrapy.Field()
    # 存活时间
    alive_time = scrapy.Field()


class GroupItem(scrapy.Item):
    # 组名
    name = scrapy.Field()
    # url
    url = scrapy.Field()


class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
