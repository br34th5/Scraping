# -*- coding: utf-8 -*-
import scrapy
import logging


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
            
            #to be able to send data between two parse methods, we have to use REQUESTS META         
            yield response.follow(url=link, callback=self.parse_country, meta={'country_name': name})
            
    def parse_country(self, response):
        #meta is a dictionary so we use []
        name = response.request.meta['country_name']
        rows = response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            yield {
                'country_name': name,
                'year': year,
                'population': population,
            }

# to run the spider , terminal: scrapy crawl countries 
# (virtual_workspace) C:\Users\Einaras\projects\Scraping\worldometers\worldometers>scrapy crawl countries