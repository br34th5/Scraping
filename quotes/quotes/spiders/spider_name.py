# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class SpiderNameSpider(scrapy.Spider):
    name = 'spider_name'
    allowed_domains = ['quotes.toscrape.com']

    script = '''
        function main(splash, args)
            splash.private_mode_enabled = false
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(1))
            usd_tab = assert(splash:select_all(".quote"))
            usd_tab[1]:mouse_click()
            assert(splash:wait(1))
            splash:set_viewport_full()
            return {
                html = splash:html(),
                png = splash:png(),
            }
        end
    '''
    def start_requests(self):
        yield SplashRequest(url="http://quotes.toscrape.com/js", callback=self.parse, endpoint="execute", args={
            'lua_source': self.script
        })
    
    
    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'quote_text': quote.xpath(".//div[@class='quote']/span[1]/text()").get(),
                'author': quote.xpath(".//div[@class='quote']/span[2]/small/text()").get(),
                'tags': quote.xpath(".//div[@class='tags']/a/text()").get()
            }
