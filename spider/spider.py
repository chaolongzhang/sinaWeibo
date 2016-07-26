# -*- coding:utf-8 -*-

import zHTTP

class Spider(object):
      def __init__(self, homeUrl, parser):
            super(Spider, self).__init__()
            self.homeUrl = homeUrl
            self.parser = parser

      def getAMessage(self):
            html = zHTTP.get(self.homeUrl)
            return self.parser.getMsg(html)



if __name__ == '__main__':
      import techweb
      import cnbeta
      import cnblog
      import tuicool

      spiders = [
            Spider(cnbeta.HOME_URL, cnbeta.CnbetaParser()),
            Spider(cnblog.HOME_URL, cnblog.CnblogParser()),
            Spider(techweb.HOME_URL, techweb.TechwebParser()),
            Spider(tuicool.HOME_URL, tuicool.TuicoolParser()),
      ]

      count = len(spiders)
      for i in range(count):
            spider = spiders[i]
            print ("-----------------------------")
            print (spider.homeUrl)
            for j in range(3):
                  text = spider.getAMessage()
                  print (text)

