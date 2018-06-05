# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
import threading
from scrapy import signals, Request
from scrapy.exceptions import IgnoreRequest

from douban.component import DBComponent


class DoubanSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomUserAgent(object):
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.agents)


# class RandomProxy(object):
#     def __init__(self):
#         self.ip_list = DBComponent.getAllProxy()
#         self.ip_list_used = []
#         self.threadReadLock = threading.Lock()
#         self.threadWriteLock = threading.Lock()
#
#     def process_request(self, request, spider):
#         if self.ip_list:
#             self.threadReadLock.acquire()
#             ip_list_index = random.randint(0, len(self.ip_list) - 1)
#             self.ip_list_used.append(self.ip_list[ip_list_index])
#             del self.ip_list[ip_list_index]
#             ip_list_used_index = len(self.ip_list_used) - 1
#             request.meta['proxy'] = "http://%s" % self.ip_list_used[ip_list_used_index]
#             request.meta['index'] = ip_list_used_index
#             self.threadReadLock.release()
#         else:
#             request.meta['index'] = -1
#             # self.ip_list = DBComponent.getAllProxy()
#
#     def process_response(self, request, response, spider):
#         if response.status == 200:
#             return response
#         else:
#             for set_cookie in response.headers.getlist('Set-Cookie'):
#                 sts = set_cookie.split(";")[0].split("=")
#                 name = sts[0]
#                 value = sts[1]
#                 cookies = {name: value}
#                 url = request.url
#                 return Request(url=url, dont_filter=True,
#                                cookies=cookies)
#         return response
#
#     def process_exception(self, request, exception, spider):
#         index = request.meta["index"]
#         if index > -1:
#             ip = self.ip_list_used[index]
#             DBComponent.deleteProxy(ip)
#             self.threadWriteLock.acquire()
#             del self.ip_list_used[index]
#             self.threadWriteLock.release()
#         print(exception)
#         return None
