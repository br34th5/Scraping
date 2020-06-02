# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            #.//td/a because of selected object. instead of responsive object
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()
            
            #absolute_url = f"https://www.worldometers.info{link}"
            #absolute_url = response.urljoin(link)
            #yield scrapy.Request(url=absolute_url)
            
            yield response.follow(url=link)

# to run the spider , terminal: scrapy crawl countries 
# (virtual_workspace) C:\Users\Einaras\projects\Scraping\worldometers\worldometers>scrapy crawl countries