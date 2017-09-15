# /usr/bin/env python
# encoding=utf-8
import scrapy

from douban.items import ProxyItem


# scrapy crawl proxySpider
class ProxySpider(scrapy.Spider):
    name = "proxySpider"
    __page = 1

    def start_requests(self):
        urls = ['http://www.kuaidaili.com/free/inha/1/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies={
                "_ydclearance": "1949471bcaa144cc2a7e53dd-f305-4253-b7fd-af7067fa27e0-1505210171",
                "yd_cookie": "1bfebc39-cdab-432b77f84f97d600bcce4805be7708d381be"

            })

    def parse(self, response):
        tr_list = response.css("table tbody tr")
        for tr in tr_list:
            td_list = tr.css("td")
            proxy = ProxyItem()
            proxy["ip"] = td_list[0].css("::text").extract_first().encode('utf-8')
            proxy["port"] = td_list[1].css("::text").extract_first().encode('utf-8')
            proxy["speed"] = td_list[5].css("::text").extract_first().encode('utf-8')
            yield proxy
            ProxySpider.__page += 1
            next_page = "http://www.kuaidaili.com/free/inha/%d/" % ProxySpider.__page
            yield response.follow(next_page, self.parse)
