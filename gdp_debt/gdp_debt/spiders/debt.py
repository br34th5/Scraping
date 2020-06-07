# -*- coding: utf-8 -*-
import scrapy
import logging

class DebtSpider(scrapy.Spider):
    name = 'debt'
    allowed_domains = ['www.worldpopulationreview.com']
    start_urls = ['https://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath("//table/tbody/tr")
        for row in rows:
            yield {
                'country_name': row.xpath(".//td[1]/a/text()").get(),
                'gdp_debt': row.xpath(".//td[2]/text()").get()
            }