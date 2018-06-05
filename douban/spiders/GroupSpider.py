# # /usr/bin/env python
# # encoding=utf-8
#
#
# # scrapy crawl # /usr/bin/env python
# # encoding=utf-8
# import scrapy
#
# from douban.items import GroupItem
#
#
# # scrapy crawl proxySpider
# class GroupSpider(scrapy.Spider):
#     name = "groupSpider"
#
#     def start_requests(self):
#         urls = ['https://www.douban.com/group/explore',
#                 'https://www.douban.com/group/culture',
#                 'https://www.douban.com/group/explore/travel',
#                 'https://www.douban.com/group/explore/ent',
#                 'https://www.douban.com/group/explore/fashion',
#                 'https://www.douban.com/group/explore/life',
#                 'https://www.douban.com/group/explore/tech']
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self, response):
#         for a in response.css("span.from a"):
#             group_item = GroupItem()
#             group_item["name"] = a.css("::text").extract_first().encode('utf-8')
#             group_item["url"] = a.css("::attr(href)").extract_first().encode('utf-8')
#             yield group_item
#             next_page = response.css("span.next a::attr(href)").extract_first()
#             yield response.follow(next_page, self.parse)
