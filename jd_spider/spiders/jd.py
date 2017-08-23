# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.http import Request
from jd_spider.items import JdSpiderItem

class JdSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["club.jd.com"]
    start_urls = ['https://club.jd.com']

    def parse(self, response):
        #url = "https://club.jd.com/comment/productPageComments.action?&productId=3245078&score=0&sortType=5&page=0&pageSize=10"
        #yield Request(url=url,callback=self.page)
        #pass
        #url="https://club.jd.com/comment/productPageComments.action?&productId=3245078&score=0&sortType=5&page=0&pageSize=10"
        #yield Request(url=url,callback=self.page)

        url1 = "https://club.jd.com/comment/productPageComments.action?&productId="
        productId = "3245078"
        url2 = "&score=0&sortType=5&page="
        page = "page"
        url3 = "&pageSize=10"
        for i in range(0, 10):
            page = str(i)
            url = url1+productId+url2+page+url3
            yield Request(url=url,callback=self.page)
        pass
    def page(self,response):
        js = json.loads(response.body_as_unicode())
        #json.loads(unicode(str, "utf-8"))
        #用json.loads将数据解析成python可以操作的对象
        comments = js['comments']
        for comment in comments:
            item = JdSpiderItem()
            item['id'] = comment['id']
            item['creationTime'] = comment['creationTime']
            item['referenceName'] = comment['referenceName']
            item['content'] = comment['content']
            yield item

