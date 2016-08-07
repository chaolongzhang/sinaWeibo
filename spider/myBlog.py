import bs4
import random

import zHTTP
from spider.spider import Spider
from weibo.weibo_message import WeiboMessage

HOME_URL = "http://blog.5long.me/archives"

class MyBlogParser(Spider):
      def __init__(self):
            super(MyBlogParser, self).__init__(HOME_URL)

      def download_text(self):
            page_count = 4
            page_index = random.randint( 1, page_count )
            if page_index == 1:
                  url = 'http://blog.5long.me/archives/'
            else:
                  url = 'http://blog.5long.me/archives/page/%d/' % ( page_index ) 
            html = zHTTP.get( url )
            return html

      def get_weibo_message(self):
            html = self.download_text()
            soup = bs4.BeautifulSoup( html, "html.parser" )
            items = soup.find_all( attrs={ "class": "post" } )
            msg = None
            n = len(items)
            if n > 0:
                  index = random.randint(0, n - 1)
                  topItem = items[index]
                  title = topItem.a.get('title').strip()
                  url = topItem.a.get( 'href' )
                  url = 'http://blog.5long.me' + url
                  msg = "推荐阅读技术博客：%s - 茶码话桑麻 %s " % ( title, url )
            return WeiboMessage(msg)