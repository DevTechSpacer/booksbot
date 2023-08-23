import scrapy
from pagination_demo.items import QuoteItem


class MegaknihySpider(scrapy.Spider):
    name = "megaknihy"
    start_urls = ["https://www.megaknihy.cz/10957-hlodavci"]
    
    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.css('div.quote'):
            quote_item['name'] = quote.css('#product_list > li:nth-child(1) > h2 > a::text').getall()
            quote_item['stocked'] = quote.css('#product_list > li:nth-child(1) > span::text').getall()
            quote_item['brand'] = quote.css('div.tags a.tag::text').getall()
            yield quote_item
        
        # go to next page 
        next_page = response.css("#product_list > li:nth-child(1) > a::attr(href)").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
            
            
            
