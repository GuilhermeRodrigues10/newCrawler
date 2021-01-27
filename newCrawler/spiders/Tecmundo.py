# -*- coding: utf-8 -*-
import scrapy
from newCrawler.items import NewcrawlerItem


class GloboSpider(scrapy.Spider):
    name = 'Tecmundo'
    allowed_domains = ['tecmundo.com.br']
    start_urls = ['https://www.tecmundo.com.br/']

    def parse(self, response):
        for main in response.css("main div.swiper-container h2"):
            news = NewcrawlerItem(title = main.css("a::attr(title)").get(), link = main.css("a::attr(href)").get    ())
            yield news