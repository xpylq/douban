# /usr/bin/env python
# encoding=utf-8
import scrapy

from douban.items import GroupItem
import json


# scrapy crawl groupSpider1
class GroupSpider(scrapy.Spider):
    name = "groupSpider1"

    def start_requests(self):
        urls = ['https://www.douban.com/j/search?q=%E7%94%B5%E5%BD%B1&start=0&cat=1019']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print  json.loads(response.body)
        for a in response.css("span.from a"):
            group_item = GroupItem()
            group_item["name"] = a.css("::text").extract_first().encode('utf-8')
            group_item["url"] = a.css("::attr(href)").extract_first().encode('utf-8')
            yield group_item
            next_page = response.css("span.next a::attr(href)").extract_first()
            yield response.follow(next_page, self.parse)
