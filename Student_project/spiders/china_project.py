# -*- coding: utf-8 -*-
import scrapy
from Student_project.items import China_StudentProjectItem
from urllib.parse import urlencode

class ChinaProjectSpider(scrapy.Spider):
    name = 'china_project'
    allowed_domains = ['cy.ncss.org.cn']
    start_urls = ['http://cy.ncss.org.cn/search/projectlist?name=&industryCode=&typeCode=&wasBindUniTechnology=-9&investStageCode=&provinceCode=&pageIndex=0&pageSize=15']

    def parse_page(self, response):
        datas = response.css('.search-list-item')
        for data in datas:
            item = China_StudentProjectItem()
            name = data.css('.project-list-item-title::text').extract_first()
            school = data.css('.project-list-item-tags-text>span::text')[0].extract()
            address = data.css('.project-list-item-tags-text>span::text')[1].extract()
            direction = data.css('.project-list-item-tags-text>span::text')[2].extract()
            industry = data.css('.project-list-item-tags-img>span::text').extract()
            introduce = data.css('.project-list-item-desc::text').extract_first()
            project_url = data.xpath('//a/@href').extract_first()
            url = 'http://cy.ncss.org.cn/' + project_url

            item['name'] = name
            item['school'] = school
            item['address'] = address
            item['direction'] = direction
            item['industry'] = industry
            item['introduce'] = introduce
            item['url'] = url
            yield item


    def parse(self, response):
        datas = response.css('.search-list-item')
        for data in datas:
            item = China_StudentProjectItem()
            name = data.css('.project-list-item-title::text').extract_first()
            school = data.css('.project-list-item-tags-text>span::text')[0].extract()
            address = data.css('.project-list-item-tags-text>span::text')[1].extract()
            direction = data.css('.project-list-item-tags-text>span::text')[2].extract()
            industry = data.css('.project-list-item-tags-img>span::text').extract()
            introduce = data.css('.project-list-item-desc::text').extract_first()
            project_url = data.xpath('//a/@href').extract_first()
            url = 'http://cy.ncss.org.cn/' + project_url

            item['name'] = name
            item['school'] = school
            item['address'] = address
            item['direction'] = direction
            item['industry'] = industry
            item['introduce'] = introduce
            item['url'] = url
            yield item

        for i in range(1,17208):
            data = {
                'name':"",
                'industryCode': "",
                'typeCode':"",
                'wasBindUniTechnology' :"-9",
                'investStageCode':"",
                'provinceCode' :'',
                'pageIndex':i,
                'pageSize':'15',

            }

            params = urlencode(data)
            base = 'http://cy.ncss.org.cn/search/projectlist?'
            url = base + params
            print(url)

            yield scrapy.Request(url=url, callback=self.parse_page)


