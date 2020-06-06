# -*- coding: utf-8 -*-
import scrapy
import logging

class DebtSpider(scrapy.Spider):
    name = 'debt'
    allowed_domains = ['www.worldpopulationreview.com']
    
    
    
    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()
            
            yield response.follow(url=link, callback=self.parse_country, meta={'country_name': name})
            
    
    def parse_country(self, response):
        name = response.request.meta['country_name']
        rows = response.xpath('//table[@class="datatableStyles__StyledTable-bwtkle-1 cyosFW table table-striped"]/tbody/tr')
        for row in rows:
            debt = row.xpath('.//td[1]/text()').get()
            
            yield {
                'country_name': name,
                'gdp_debt': debt,
            }
            
            #does not work mehh reik variables pervadint