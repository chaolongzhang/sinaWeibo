# -*- coding: utf-8 -*-

from __future__ import absolute_import
import bs4
from spider.spider import Spider
from weibo.weibo_message import WeiboMessage

HOME_URL = "http://www.cnblogs.com"


class CnblogParser(Spider):

    def __init__(self):
        super(CnblogParser, self).__init__(HOME_URL)

    def get_weibo_message(self):
        html = self.download_text()
        soup = bs4.BeautifulSoup(html, "html.parser")
        items = soup.find_all(attrs={"class": "post_item_body"})
        msg = ''
        if len(items) > 0:
            topItem = items[0]
            title = topItem.a.string.strip()
            url = topItem.a.get('href')
            msg = "%s %s" % (title, url)
        return WeiboMessage(msg)
