# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class GlassopSpider(scrapy.Spider):
    name = 'glassop'
    allowed_domains = ['https://www.glassesshop.com']
    start_urls = ['https://https://www.glassesshop.com/bestsellers']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    
    def start_requests(self):
        #no need for call-back method inside request class
        yield scrapy.Request(url='https://https://www.glassesshop.com/bestsellers', headers={
            'User-Agent': self.user_agent
        })

    rules = (
        #allow / deny / restrict_xpaths / restrict_css
        #adding proccess_request for changing user_agent
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row']")), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="(//li[@class='page-item'][4]/a"), follow=True, process_request='set_user_agent')
    )

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request
    
    def parse_item(self, response):
        yield {
            'title': ,
        }

