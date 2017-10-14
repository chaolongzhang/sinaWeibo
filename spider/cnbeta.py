# -*- coding: utf-8 -*-

from __future__ import absolute_import
import bs4
from spider.spider import Spider
from weibo.weibo_message import WeiboMessage

HOME_URL = "http://www.cnbeta.com"


class CnbetaParser(Spider):

    def __init__(self):
        super(CnbetaParser, self).__init__(HOME_URL)

    def get_weibo_message(self):
        html = self.download_text()
        soup = bs4.BeautifulSoup(html, "html.parser")
        items_area = soup.find(attrs={"class": "items-area"})
        items = items_area.find_all(attrs={"class": "item"})
        msg = ''
        if len(items) > 0:
            topItem = items[0]
            title = topItem.a.string.strip()
            path = topItem.a.get('href')
            url = HOME_URL + path
            # infodiv = topItem.find(attrs={"class": "newsinfo"})
            # content = infodiv.get_text()
            msg = "%s %s" % (title, url)
        return WeiboMessage(msg)
