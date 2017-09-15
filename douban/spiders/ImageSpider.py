# /usr/bin/env python
# encoding=utf-8
import random
import re

import scrapy
from douban.items import ImageItem
from douban.component import DBComponent


class ImageSpider(scrapy.Spider):
    name = "imageSpider"

    def start_requests(self):
        group_list = DBComponent.getAllGroup()
        random.shuffle(group_list)
        for url in group_list:
            yield scrapy.Request(url=url + "discussion?start=0", callback=self.parse_group)
            # yield scrapy.Request(url=url + "discussion?start=50", callback=self.parse_group)

    def parse_group(self, response):
        for url in response.css("table.olt tr:not(:first-child) td.title a::attr(href)").extract():
            yield scrapy.Request(url=url, callback=self.parse_content)

    def parse_content(self, response):
        download_flag = False
        topic_content = response.css(".topic-doc .topic-content")
        for content in topic_content.css("p::text").extract():
            content = content.encode("utf-8")
            if re.search("(微信群|群)", content):
                print response.url, content
                download_flag = True
                break
        if download_flag:
            group_url = response.css(".title.title ::attr(href)").extract_first()
            group_url = re.sub('\\?.*$', '', group_url)
            DBComponent.addGroupMatch(group_url)
            image_item = ImageItem()
            image_item["image_urls"] = topic_content.css("img::attr(src)").extract()
            return image_item
