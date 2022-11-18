import scrapy


class LentaSpider(scrapy.Spider):
    name = 'lenta'
    start_urls = [
        'https://lenta.ru/',
    ]

    def parse(self, response):
        links = response.css('a._topnews')
        for link in links:
            print(link)
