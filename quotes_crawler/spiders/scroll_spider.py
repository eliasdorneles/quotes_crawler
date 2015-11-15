import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = 'quotes-scroll'
    quotes_base_url = 'http://spidyquotes.herokuapp.com/api/quotes?page=%s'
    start_urls = [quotes_base_url % 1]
    download_delay = 1.5

    def parse(self, response):
        data = json.loads(response.body)
        for d in data.get('quotes', []):
            yield {
                'texto': d['text'],
                'autor': d['author']['name'],
                'tags': d['tags'],
            }
        if data['has_next']:
            next_page = data['page'] + 1
            yield scrapy.Request(self.quotes_base_url % next_page)
