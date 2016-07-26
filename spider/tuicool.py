# -*- coding: utf-8 -*-

import bs4
from utility import attrs2dic

HOME_URL = "http://www.tuicool.com"

class TuicoolParser:
      def getMsg(self, html):
            soup = bs4.BeautifulSoup(html, "html.parser")
            items = soup.find_all( attrs={ "class": "index-item" } )
            if len(items) > 0:
                  topItem = items[0]
                  title = topItem.a.string.strip()
                  url = HOME_URL + topItem.a.get( 'href' )
                  return "%s %s" % ( title, url )
            return None


if __name__ == '__main__':

      import zHTTP

      def getMessage():
            html = zHTTP.get(HOME_URL)
            listname = TuicoolParser()
            return listname.getMsg(html)

      for i in range(3):
            text = getMessage()
            print (text)
            






