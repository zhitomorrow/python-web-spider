# -*- coding: utf-8 -*-
import scrapy
from scrapy_test.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'  # 项目唯一的名字，用来区分不同的spider
    allowed_domains = ['quotes.toscrape.com']  # 允许爬取的域名，如果初始或者后续的请求连接不是在这个域名下，则请求连接或被过滤掉
    start_urls = ['http://quotes.toscrape.com/']  # spider启动时爬取的url列表，初始请求是由它来定义的

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            tags = quote.css('.tags .tag::text').extract()
            if len(tags) > 0:
                item['tags'] = '#'.join(tags)
            else:
                item['tags'] = ''
            yield item

        next_page = response.css('.pager .next a::attr("href")').extract_first()
        url = response.urljoin(next_page)
        yield scrapy.Request(url=url, callback=self.parse)
