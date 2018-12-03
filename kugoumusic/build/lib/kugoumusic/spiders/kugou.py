#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

__author__ = 'Zqf'

import scrapy
from kugoumusic.items import KugoumusicItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class KugouSpiders(scrapy.spiders.CrawlSpider):
    name = 'kugou'
    
    start_urls = ['http://www.kugou.com/']

    rules = (
        Rule(LinkExtractor(allow=['http://www.kugou.com/yy/html/singer.html',
                                  'http://www.kugou.com/yy/singer/index/\d-([a-z]|null)-1.html'])),
        Rule(LinkExtractor(allow=['http://www.kugou.com/yy/singer/home/\d+.html']), callback='parse_item')
    )
    
    def parse_item(self, response):
        singer = response.xpath('//div/div[@class="clear_fix"]/strong/text()').extract_first()
        print(singer)
        songs = response.xpath('//ul[@id="song_container"]/li//span[@class="text"]/i/text()').extract()
        print(songs)
    
        item = KugoumusicItem()
        item['singer'] = singer
        item['songs'] = songs
        
        yield item
