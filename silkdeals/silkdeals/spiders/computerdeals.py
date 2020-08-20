# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest

class ComputerdealsSpider(scrapy.Spider):
    name = 'computerdeals'
    
    def start_requests(self):
        yield SeleniumRequest(
            url='https://slickdeals.net/computer-deals/',
            wait_time=3,
            callback=self.parse
        )


    def parse(self, response):
        products = response.xpath("//ul[@class='dealTiles categoryGridDeals']/li")
        for product in products:
            yield {
                'name': product.xpath('.//a[@class="itemTitle"]/text()').get(),
                'link': product.xpath('.//a[@class="itemTitle"]@href').get(),
                'store_name': product.xpath('.//span[@class="itemStore"]/text()').get(),
                'price': product.xpath('.//div[@class="itemPrice  wide "]/text()').get()
            }
