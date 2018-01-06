# -*- coding: utf-8 -*-

from __future__ import absolute_import
import json
import random
from spider.spider import Spider
from weibo.weibo_message import WeiboMessage

HOME_URL = "http://www.miaopai.com/miaopai/index_api?cateid=2002&per=20&page=1"


class MiaopaParser(Spider):

    def __init__(self):
        super(MiaopaParser, self).__init__(HOME_URL)

    def get_weibo_message(self):
        json_text = self.download_text()
        items = self.getItems(json_text)
        msg = ''
        count = len(items)
        if count > 0:
            index = random.randint(0, count - 1)
            msg = items[index]
        return WeiboMessage(msg)

    def getItems(self, jsonStr):
        items = []
        nodes = json.loads(jsonStr)
        results = nodes["result"]
        for node in results:
            scid = node["channel"]["scid"]
            url = "http://www.miaopai.com/show/%s.htm" % scid
            msg = node["channel"]["ext"]["_t"]
            item = "%s %s" % (msg, url)
            items.append(item)
        return items
