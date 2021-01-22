import scrapy
from newCrawler.items import NewcrawlerItem


class CanaltechSpider(scrapy.Spider):
    name = 'Canaltech'
    allowed_domains = ['https://canaltech.com.br/']
    start_urls = ['https://canaltech.com.br/']

    def parse(self, response):
        for section in response.css("section.features div.item"):
            news = NewcrawlerItem(title = section.css("a span.title::text").get(), link = section.css("a::attr(href)").get())
            yield news
