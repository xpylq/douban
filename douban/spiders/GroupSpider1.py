# /usr/bin/env python
# encoding=utf-8
import scrapy
import json
import re

from douban.component import DBComponent
from douban.items import GroupItem
from urllib import unquote


# scrapy crawl groupSpider1
class GroupSpider(scrapy.Spider):
    name = "groupSpider1"

    def start_requests(self):
        urls = ['https://www.douban.com/j/search?q=%E7%94%B5%E5%BD%B1&start=0&cat=1019']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        start_num = int(re.search('start=(\d*)&', response.url).group(1))  # 匹配url中start后的数字
        start_num += 20
        next_url = re.sub("start=\d*", "start=" + str(start_num), response.url)  # 获取新的数字
        json_str = json.loads(response.body)
        more = json_str['more']
        for item in json_str['items']:
            url = re.search('\?url=(.*)&amp;query', item).group(1)
            url = unquote(url)
            name = re.search('alt=\"(.*)\">', item).group(1)
            if not DBComponent.isExistGroup(url):
                DBComponent.insertGroup(name, url)
        if more:
            yield response.follow(next_url, self.parse)
