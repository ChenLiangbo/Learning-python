#!usr/bin/env/python 
# -*- coding: utf-8 -*-
from __future__ import print_function
from scrapy import Spider
from scrapy import Request



class TestSpider(Spider):
    name = 'test'
    start_urls = [
        "http://www.qq.com/",
    ]
 
    def login_parse(self, response):
        ''' 如果登录成功,手动构造请求Request迭代返回 '''
        # print response
        for i in range(0, 10):
            yield Request('http://www.example.com/list/1?page={0}'.format(i))
 
    def start_requests(self):
        ''' 覆盖默认的方法(忽略start_urls),返回登录请求页,制定处理函数为login_parse '''
        return Request('http://www.example.com/login', method="POST", body='username=bomo&pwd=123456', callback=self.login_parse)
 
 
    def parse(self, response):
        ''' 默认请求处理函数 '''
        # print response
        pass


from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
 
class LianjiaSpider(CrawlSpider):
    name = "lianjia"
 
    allowed_domains = ["lianjia.com"]
 
    start_urls = [
        "http://bj.lianjia.com/ershoufang/"
    ]
 
    rules = [
        # 匹配正则表达式,处理下一页
        Rule(LinkExtractor(allow=(r'http://bj.lianjia.com/ershoufang/pg\s+$',)), callback='parse_item'),
 
        # 匹配正则表达式,结果加到url列表中,设置请求预处理函数
        # Rule(FangLinkExtractor(allow=('http://www.lianjia.com/client/', )), follow=True, process_request='add_cookie')
    ]
 
    def parse_item(self, response):
        # 这里与之前的parse方法一样，处理
        pass