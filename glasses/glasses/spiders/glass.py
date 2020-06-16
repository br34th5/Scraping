# -*- coding: utf-8 -*-
import scrapy


class GlassSpider(scrapy.Spider):
    name = 'glass'
    allowed_domains = ['glassesshop.com']
    start_urls = ['https://glassesshop.com/bestsellers']

    def parse(self, response):
        for glasses in response.xpath("//div[@id='product-lists']/div"):
            yield {
                'product_url': glasses.xpath(".//div[@class='product-img-outer']/a/@href").get(),
                'product_image_link': glasses.xpath(".//div[@class='product-img-outer']/a/img/@src").get(),
                'product_name': glasses.xpath("normalize-space(.//div[@class='p-title']/a/text())").get(),
                'product_price': glasses.xpath(".//div[@class='p-price']/div/span/text()").get() 
            }
    
    
    def start_requests(self):
        yield scrapy.Request(url='https://glassesshop.com/bestsellers', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
        })