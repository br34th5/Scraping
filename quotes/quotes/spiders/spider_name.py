# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class SpiderNameSpider(scrapy.Spider):
    name = 'spider_name'
    allowed_domains = ['quotes.toscrape.com']

    script = '''
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(1))
            return splash:html()
        end
    '''
    def start_requests(self):
        yield SplashRequest(url="http://quotes.toscrape.com/js", callback=self.parse, endpoint="execute", args={
            'lua_source': self.script
        })
    
    
    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']")
        for quote in quotes:
            yield {
                'quote_text': quote.xpath(".//span[@class='text']/text()").get(),
                'author': quote.xpath(".//span[2]/small/text()").get(),
                'tags': quote.xpath(".//div[@class='tags']/a/text()").getall()
            }
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            abosolute_url = f"http://quotes.toscrape.com{next_page}"
            yield SplashRequest(url=abosolute_url, callback=self.parse, endpoint='execute', args={
                'lua_source': self.script
            })