# -*- coding: utf-8 -*-
import scrapy

class GlassopSpider(scrapy.Spider):
    name = 'glassop'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    #Some glasses do have the price inside a 'del' element //del/text() while others are inside a 'span' element.
    #This method will basically check the return type of this XPath expression //del/text() if it's set to None 
    #then the original price will be extracted from the XPath expression I used in the else block.
    def get_price(self, selector):
        original_price = selector.xpath(
            ".//div[@class='p-price']/div/span/text()").get()
        if original_price is not None:
            return original_price
        else:
            return selector.xpath(".//div[@class='p-price']/div/span[@class='color-red']/text()").get()

    def parse(self, response):
        glasses = response.xpath("//div[contains(@class, 'product-list-row')]")
        for glass in glasses:
            yield {
                'url': glass.xpath(".//div[@class='product-img-outer']/a/@href").get(),
                'img_url': glass.xpath(".//div[@class='product-img-outer']/a/img[1]/@src").get(),
                'name': glass.xpath(".//div[@class='p-title']/a/text()").get(),
                'price': self.get_price(glass)
            }

        next_page = response.xpath(
            "//ul[@class='pagination']/li[position() = last()]/a/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)