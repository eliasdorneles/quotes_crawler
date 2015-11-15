import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes-tableful'
    start_urls = ['http://spidyquotes.herokuapp.com/tableful/']
    download_delay = 1.5

    def parse(self, response):
        quotes_xpath = '//tr[./following-sibling::tr[1]/td[starts-with(., "Tags:")]]'

        for quote in response.xpath(quotes_xpath):
            texto, autor = quote.xpath('normalize-space(.)').re('(.+) Author: (.+)')
            tags = quote.xpath('./following-sibling::tr[1]//a/text()').extract()
            yield dict(texto=texto, autor=autor, tags=tags)

        link_next = response.xpath('//a[contains(., "Next")]/@href').extract_first()
        if link_next:
            yield scrapy.Request(response.urljoin(link_next))
