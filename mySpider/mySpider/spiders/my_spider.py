#!usr/bin/env/python 
# -*- coding: utf-8 -*-
from __future__ import print_function
from scrapy import Spider
from scrapy import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import os
import json
from bs4 import BeautifulSoup
import urllib
import csv


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



 
class QzoneSpider(CrawlSpider):

    name = "qzone"
 
    allowed_domains = ["qzone.qq.com"]

    # qq = '1873846630'
    qq = '2477153650'
 
    start_urls = [
        "https://user.qzone.qq.com/" + qq + '/',
    ]
 

 
    def parse(self, response):
        print("-"*80)
        mainPage = {"main":"主页","1":"资料","2":"日志","3":"访客","4":"相册","311":"说说","334":"留言板"}
        html = response.body
        # print("html = ",html)

        print('-'*80)




class TianqiSpider(CrawlSpider):
    name = "tianqi"
    

    allowed_domains = ["lishi.tianqi.com"]
 
    start_urls = [
        "http://lishi.tianqi.com/"
    ]
    
    # rules = [
    #     # 匹配正则表达式,处理下一页
    #     Rule(LinkExtractor(allow=(r'http://bj.lianjia.com/ershoufang/pg\s+$',)), callback='parse_item'),
 
    #     # 匹配正则表达式,结果加到url列表中,设置请求预处理函数
    #     # Rule(FangLinkExtractor(allow=('http://www.lianjia.com/client/', )), follow=True, process_request='add_cookie')
    # ]
 
    def parse(self, response):
        print("-"*80)
        # print("response = ",dir(response))
        # fp = open('first.txt','wb')
        # fp.write(response.body)
        # fp.close()
        hxs = HtmlXPathSelector(response)
        uls = response.xpath('//ul')
        # print("uls = ",type(uls),dir(uls))
        icount = 0
        filedir = os.getcwd() + '/' + str(icount)
        if not os.path.exists(filedir):
            os.mkdir(filedir)

        for ul in uls:
            jcount = 0
            filename = filedir + '/' + str(jcount) + '.txt'
            fp = open(filename,'w')
            # title = site.select('a/text()').extract()
            # link = site.select('a/@href').extract()
            # desc = site.select('text()').extract()
            # print("title = ",title, link, desc)
            # print("ul = ",type(ul),dir(ul))
            lis = ul.select('./li')
            print("lis = ",type(lis),len(lis))        
            for li in lis:
                title = li.select('//a/@title').extract()
                link = li.select('//a/@href').extract()
                # print("li = %s" % (li))
                print("title = %s" % (len(title),))
                print("link = %s" % (len(link),))
                cdict = {"title":title[0],"link":link[0]}
                cjson = json.dumps(cdict,separators = (',',':'))

                print(title[0],type(title[0]))
                print(link[0],type(link[0]))
                fp.write(cjson)
                fp.write('/r/n')
                fp.close()
                # print(dir(li))
                # print()
                # html = li.extract()
                # link = Selector(text=html).xpath('//a/@href').extract()
                # title = Selector(text=html).xpath('//a/@title').extract()
                # break
            icount = icount + 1
            # if icount > 5:
            #     break
        print("-"*80)


def get_from_li(liString):
    pass

citylist = []

class JiadingTianqiSpider(CrawlSpider):

    name = "JiadingTianqi"
    
    allowed_domains = ["lishi.tianqi.com"]
 
    start_urls = [
        "http://lishi.tianqi.com/jiading/index.html",
        'http://lishi.tianqi.com/songjiang/index.html',
    ]
    
    # rules = [
    #     # 匹配正则表达式,处理下一页
    #     Rule(LinkExtractor(allow=(r'http://bj.lianjia.com/ershoufang/pg\s+$',)), callback='parse_item'),
 
    #     # 匹配正则表达式,结果加到url列表中,设置请求预处理函数
    #     # Rule(FangLinkExtractor(allow=('http://www.lianjia.com/client/', )), follow=True, process_request='add_cookie')
    # ]
 
    def parse(self, response):
        print('-'*80)
        html = response.body
        # print(html)
        soup = BeautifulSoup(html,'html.parser')
        links = []
        for link in soup.find_all('a'):
            link = link.get('href')
            if 'lishi.tianqi.com/jiading' in link:
                # print("link = ",link)
                links.append(link)
        spiderdir = './jiadiangTianqi/'
        if not os.path.exists(spiderdir):
            os.mkdir(spiderdir)
        
        for url in links[1:]:
            # print("url = ",url)
            filename = spiderdir + url.split('/')[-1].split('.')[0] + '.txt'
            fp = open(filename,'a')
            res = urllib.request.urlopen(url)
            html = res.read()
            soup = BeautifulSoup(html,'html.parser')
            #//div class = 'tqtongji2' 
            div = soup.find_all("div", class_="tqtongji2")
            try:
                div = div[0]
            except Exception as ex:
                print("Exception happens that:",str(ex))
                continue
            # print("div = ",div,dir(div))
            uls = div.find_all('ul')
            # print("uls = ",uls)
            for ul in uls:
                alist = []
                lis = ul.find_all('li')
                # print("lis = ",lis)
                # print('-'*20)
                for li in lis:
                    c = li.string
                    alist.append(c)
                # print("alist = ",alist)
                try:
                    aline = ','.join(alist)
                except Exception as ex:
                    print("Exception happens that:",str(ex))
                    aline = "excption happens"
                fp.write(aline )
                fp.write('\n')
            fp.close()


            # break 
        print('-'*80)
