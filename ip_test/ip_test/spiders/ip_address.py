# -*- coding: utf-8 -*-
import scrapy
from ip_test.items import IpTestItem


class IpAddressSpider(scrapy.Spider):
    name = 'ip_address'
    allowed_domains = ['www.ip.cn/']
    start_urls = ['http://www.ip.cn//']


    def parse(self, response):
        item = IpTestItem()
        address = response.css('code::text').extract()
        print(address)
        item['ip_name'] = address[0]
        item['address_ip'] = address[1]
        yield item




