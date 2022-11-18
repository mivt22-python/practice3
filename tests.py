from datetime import datetime
from os.path import join
from unittest import TestCase

from scrapy.http import Request, Response

from lenta_spider import LentaSpider


class TestLentaSpider(TestCase):

    def test_page_valuev(self):
        # Создаем тестовый набор данных из файла
        url = 'https://lenta.ru/news/2022/11/18/valuev/'
        headers = {}
        with open(join('fixtures', 'valuev.html')) as f:
            body = f.read()
        fixture = Response(url, 200, headers, body, Request(url))

        # Запускаем тестируемую функцию
        result = LentaSpider.parse_news(fixture)

        # Проверим что пришел словарь
        self.assertIsInstance(result, dict)

        # Проверяем что в словаре имеются все нужные ключи
        keys = ['title', 'category', 'author', 'datetime', 'text']
        self.assertTrue(all(k in result for k in keys))

        # Проверяем заголовок
        title = 'Николая Валуева госпитализировали'
        self.assertEqual(title, result['title'])

        # Проверяем категорию
        category = 'Спорт'
        self.assertEqual(category, result['category'])

        # Проверяем дату и время
        dt = datetime(2002, 11, 18, 50)
        self.assertEqual(dt, result['datetime'])

        # Проверяем автора
        author = 'Андрей Стрельцов'
        self.assertEqual(author, result['author'])

        # Проверяем текст
        self.assertGreater(len(result['text'].split()), 145)
        self.assertIn('Николая Валуева', result['text'])
        self.assertIn('(WBA)', result['text'])
        self.assertIn('Склифосовского', result['text'])
