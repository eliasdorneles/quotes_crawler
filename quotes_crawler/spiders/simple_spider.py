import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://spidyquotes.herokuapp.com/'
    ]

    def parse(self, response):
        for quote in response.css('.quote'):
            yield {
                'texto': quote.css('span::text').extract_first(),
                'autor': quote.css('small::text').extract_first(),
                'tags': quote.css('.tags a::text').extract(),
            }
        link_next = response.css('li.next a::attr("href")').extract_first()
        if link_next:
            yield scrapy.Request(response.urljoin(link_next))
