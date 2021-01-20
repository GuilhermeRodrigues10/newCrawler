import scrapy
from newCrawler.items import NewcrawlerItem


class GloboSpider(scrapy.Spider):
    name = 'Globo'
    allowed_domains = ['tecmundo.com.br']
    start_urls = ['https://www.tecmundo.com.br/']

    def parse(self, response):
        for article in response.css("div.z--container"):
            news = NewcrawlerItem(title = article.css("div.tec--list__item figure a::attr(title)").get(), link = article.css("div.tec--list__item figure a::attr(href)").get())
            yield news