import scrapy


class LentaSpider(scrapy.Spider):
    name = 'lenta'
    start_urls = [
        'https://lenta.ru/',
    ]

    def parse(self, response):
        """ Парсинг главной страницы """
        links = response.css('a._topnews')
        for link in links:
            print(link)

    def parse_news(self, response):
        """ Парсинг новости """
        links = response.css('a._topnews')
        for link in links:
            print(link)
