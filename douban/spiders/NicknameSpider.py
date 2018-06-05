# /usr/bin/env python
# encoding=utf-8
# pip install pybloomfiltermmap
import scrapy
import re


class NicknameSpider(scrapy.Spider):
    name = "nicknameSpider"

    def __init__(self, name=None, **kwargs):
        self.nickname_list = []
        self.file_name = "/Users/youzhihao/Downloads/douban/nickname.txt"
        super().__init__(name, **kwargs)

    def start_requests(self):
        url = 'https://www.douban.com/group/shortstories/discussion?start=0'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        tr_list = response.css("table.olt tr:not(:first-child)")
        for tr in tr_list:
            nickname = tr.css("td:nth-child(2) a::text").extract_first()
            self.nickname_list.append(nickname)
        if self.is_more(response):
            start_num = int(re.search('start=(\d*)', response.url).group(1))  # 匹配url中start后的数字
            start_num += 25
            next_url = re.sub("start=\d*", "start=" + str(start_num), response.url)  # 获取新的数字
            yield response.follow(next_url, self.parse)
        else:
            self.write_to_file()

    def is_more(self, response):
        more = response.css('.next a')
        if more:
            return True
        return False

    def write_to_file(self):
        self.nickname_list = set(self.nickname_list)
        self.nickname_list.remove('[已注销]')
        file = open(self.file_name, 'w', encoding='utf-8')
        for nickname in self.nickname_list:
            file.write(nickname+'\n')
