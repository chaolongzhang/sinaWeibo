# -*- coding: utf-8 -*-

from __future__ import absolute_import
import bs4
import random
from spider.spider import Spider
from weibo.weibo_message import WeiboMessage

HOME_URL = "https://chaolongzhang.github.io"


class MyBlogParser(Spider):

    def __init__(self):
        super(MyBlogParser, self).__init__(HOME_URL)

    def download_text(self):
        page_count = 4
        page_index = random.randint(1, page_count)
        if page_index == 1:
            url = '%s/archives' % (HOME_URL)
        else:
            url = '%s/archives/page/%d/' % (HOME_URL, page_index)
        self.home_url = url
        html = super().download_text()
        return html

    def get_weibo_message(self):
        html = self.download_text()
        soup = bs4.BeautifulSoup(html, "html.parser")
        items = soup.find_all('article')
        msg = None
        n = len(items)
        if n > 0:
            index = random.randint(0, n - 1)
            topItem = items[index]
            title = topItem.a.span.string.strip()
            url = topItem.a.get('href')
            url = HOME_URL + url
            msg = "推荐阅读技术博客：%s - 茶码话桑麻 %s" % (title, url)
        return WeiboMessage(msg)
