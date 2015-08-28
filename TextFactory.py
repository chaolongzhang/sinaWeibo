# -*- coding: utf-8 -*-

from spider.spider import Spider
import spider.tuicool as tuicool
import spider.cnbeta as cnbeta
import spider.cnblog as cnblog
import spider.techweb as techweb
import spider.miaopai as miaopai


spiders = [
      Spider(miaopai.HOME_URL, miaopai.MiaopaParser()),
      Spider(cnbeta.HOME_URL, cnbeta.CnbetaParser()),
      Spider(cnblog.HOME_URL, cnblog.CnblogParser()),
      Spider(techweb.HOME_URL, techweb.TechwebParser()),
      Spider(tuicool.HOME_URL, tuicool.TuicoolParser()),
      Spider(miaopai.HOME_URL, miaopai.MiaopaParser()),
]

currentIndex = 0
count = len(spiders)

def getText():
      spider = nextSpider()
      text = spider.getAMessage()
      return text

def nextSpider():
      global currentIndex
      spider = spiders[currentIndex]
      currentIndex = (currentIndex + 1) % count
      return spider


if __name__ == '__main__':
      for i in range(2 * count):
            print ("%d: %s" % (i, getText()))