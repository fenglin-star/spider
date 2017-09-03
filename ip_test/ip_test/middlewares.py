# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class IpTestSpiderMiddleware(object):
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



import requests
from fake_useragent import UserAgent
ua = UserAgent()

def get_proxy():
    r = requests.get('http://localhost:5000/get')
    proxy = r.text
    return proxy


class ProxyMiddleware(object):
    proxyList = get_proxy()
    def process_request(self, request, spider):
        # Set the location of the proxy
        pro_adr = self.proxyList
        print("USE PROXY -> " + pro_adr)
        request.meta['proxy'] = "http://" + pro_adr
        url = request.url;
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; windows NT)'
        headers = {'User-Agent': user_agent}
        r = requests.post(url, headers=headers)
        body = r.content
        return HtmlResponse(url, encoding='utf-8', status=200, body=body)