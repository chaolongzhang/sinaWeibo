# -*- coding: utf-8 -*-

import json
import random

HOME_URL = "http://www.miaopai.com/miaopai/index_api?cateid=2002&per=20&page=1"


class MiaopaParser(object):
      def __init__(self):
            self.items = []

      def feed(self, jsonStr):
            nodes = json.loads(jsonStr, "utf-8")
            results = nodes["result"]
            for node in results:
                  scid = node["channel"]["scid"]
                  url = "http://www.miaopai.com/show/%s.htm" % scid
                  msg = node["channel"]["ext"]["_t"]
                  item = "%s %s" % (msg, url)
                  self.items.append(item)


      def getMsg(self):
            count = len(self.items)
            if count == 0:
                  return
            index = random.randint(0, count - 1)
            print index
            return self.items[index]



if __name__ == '__main__':

      import http

      def getMessage():
            html = http.get(HOME_URL)
            listname = MiaopaParser()
            listname.feed(html)
            return listname.getMsg()

      for i in range(30):
            text = getMessage()
            print (text)