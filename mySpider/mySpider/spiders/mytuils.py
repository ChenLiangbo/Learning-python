#!usr/bin/env/python 
# -*- coding: utf-8 -*-


class TianQiConfig(object):
    def __init__(self,):
        super(TianQiConfig,self).__init__()
        self.years    = list(range(2014,2016))
        self.months   = list(range(1,13)) 
        self.cityName = 'jiading'

    def getYearAndMonth(self,yearList,monthList):
        time = []
        for y in yearList:
            for m in monthList:
                if int(m) < 10:
                    t = str(y) + '0' + str(m)
                else:
                    t = str(y) + str(m)
                time.append(t)
        return time

    def getUrls(self,):
        # http://lishi.tianqi.com/jiading/201611.html
        domainUrl = 'http://lishi.tianqi.com'
        cityUrl = domainUrl + '/' + self.cityName + '/'
        times = self.getYearAndMonth(self.years,self.months)
        urls = []
        for t in times:
            timeUrl = cityUrl + t + '.html'
            urls.append(timeUrl)
        return urls

if __name__ == '__main__':
     tianqiObject = TianQiConfig()
     urls = tianqiObject.getUrls()
     for url in urls:
         print(url) 
