# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest

class ExampleSpider(scrapy.Spider):
    name = 'example'
    #since we gonna use selenium to send requests, we don't need allowed domains or start_url lists
    def start_requests(self):
        yield SeleniumRequest(
            url="https://duckduckgo.com"
            wait_time=3,
            screenshot=True,
            callback=self.parse
        )
    
    
    def parse(self, response):
        img = response.meta['screenshot']
        
        with open('screenshot.png', 'wb') as f:
            f.write(img)
