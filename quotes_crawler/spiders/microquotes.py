# -*- coding: utf-8 -*-
import scrapy
from extruct.w3cmicrodata import LxmlMicrodataExtractor


class QuotesSpider(scrapy.Spider):
    name = "quotes-microdata"
    start_urls = (
        'http://spidyquotes.herokuapp.com/',
    )
    download_delay = 1.5

    def parse(self, response):
        extractor = LxmlMicrodataExtractor()
        items = extractor.extract(response.body_as_unicode(), response.url)['items']

        for it in items:
            yield it['properties']

        link_next = response.css('li.next a::attr("href")').extract_first()
        if link_next:
            yield scrapy.Request(response.urljoin(link_next))
