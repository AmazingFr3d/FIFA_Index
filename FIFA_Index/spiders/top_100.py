# -*- coding: utf-8 -*-
import scrapy


class Top100Spider(scrapy.Spider):
    name = 'top_100'
    allowed_domains = ['www.fifaindex.com']
    start_urls = ['https://www.fifaindex.com/players/top/#']

    def parse(self, response):
        for player in response.xpath("//table[@class='table table-striped table-players']/tbody/tr"):
            yield{
                'name': player.xpath("./td[4]/a/text()").get(),
                'age': player.xpath("./td[6]/text()").get(),
                'country': player.xpath("./td[2]/a/@title").get(),
                'position': player.xpath("./td[5]/a/span/text()").get(),
                'club': player.xpath("./td[7]/a/@title").get()
            }

        nextpage = response.xpath("//li[@class='ml-auto']/a/@href").get()
        if nextpage:
            yield response.follow(url=nextpage, callback=self.parse)
