# -*- coding: utf-8 -*-

import bs4
from utility import attrs2dic

HOME_URL = "http://www.cnbeta.com"

class CnbetaParser:
      def getMsg(self, html):
            soup = bs4.BeautifulSoup(html, "html.parser")
            items = soup.find_all(attrs={"class": "item"})
            if len(items) > 0:
                  topItem = items[0]
                  # print(topItem)
                  title = topItem.a.string.strip()
                  path = topItem.a.get('href')
                  url = HOME_URL + path
                  infodiv = topItem.find(attrs={"class": "newsinfo"})
                  content = infodiv.get_text()
                  return "%s %s" % (title, url)
            return None



if __name__ == '__main__':

      import zHTTP

      def getMessage():
            html = zHTTP.get(HOME_URL)
            listname = CnbetaParser()
            return listname.getMsg(html)

      for i in range(3):
            text = getMessage()
            print (text)