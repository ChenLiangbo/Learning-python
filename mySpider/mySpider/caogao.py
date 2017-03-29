#!usr/bin/env/python 
# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

# html = '<li><a href="http://www.baidu.com" class="one" title="C">C</a>li-text-li</li>'
# link = Selector(text=html).xpath('//a/@href').extract()
# title = Selector(text=html).xpath('//a/@title').extract()
# print("text = ",link)
# print("title = ",title)

from bs4 import BeautifulSoup
html = '<li><a href="http://lishi.tianqi.com/zhanghua/index.html" target="_blank" title="彰化历史天气">彰化</a></li>'
soup = BeautifulSoup(html,'html.parser')

link = str(soup.a['href'])
city = str(link.split('/')[3])
print('link = ',link)
print("city = ",city)