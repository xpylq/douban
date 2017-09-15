# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from douban.component import DBComponent
from douban.items import ProxyItem, GroupItem


class DoubanPipeline(object):
    def process_item(self, item, spider):
        return item


class ProxyPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, ProxyItem):
            ip = item["ip"] + ":" + item["port"]
            speed = float(item["speed"].replace("秒", ""))
            if speed <= 1:
                DBComponent.insertProxy(ip, speed)
        return item


class GroupPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, GroupItem):
            name = item["name"]
            url = item["url"]
            if not DBComponent.isExistGroup(url):
                DBComponent.insertGroup(name, url)
        return item
