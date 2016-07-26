# -*- coding: utf-8 -*-

import bs4
from utility import attrs2dic

HOME_URL = "http://www.techweb.com.cn/roll"


class TechwebParser:
      def getMsg(self, html):
            soup = bs4.BeautifulSoup(html, "html.parser")
            div = soup.find( attrs={ "class": "newslist" } )
            items = div.ul.find_all( 'li' )
            if len(items) > 0:
                  topItem = items[0]
                  title = topItem.a.string.strip()
                  url = topItem.a.get( 'href' )
                  return "%s %s" % ( title, url )
            return None



if __name__ == '__main__':

      import zHTTP

      def getMessage():
            html = zHTTP.get(HOME_URL)
            listname = TechwebParser()
            return listname.getMsg(html)

      for i in range(3):
            text = getMessage()
            print (text)