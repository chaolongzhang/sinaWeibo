# -*- coding: utf-8 -*-

import json
import random

HOME_URL = "http://www.miaopai.com/miaopai/index_api?cateid=2002&per=20&page=1"


class MiaopaParser(object):
      def getItems(self, jsonStr):
            items = []
            nodes = json.loads(jsonStr, "utf-8")
            results = nodes["result"]
            for node in results:
                  scid = node["channel"]["scid"]
                  url = "http://www.miaopai.com/show/%s.htm" % scid
                  msg = node["channel"]["ext"]["_t"]
                  item = "%s %s" % (msg, url)
                  items.append(item)
            return items

      def getMsg(self, html):
            items = self.getItems(html)
            count = len(items)
            if count == 0:
                  return
            index = random.randint(0, count - 1)
            return items[index]



if __name__ == '__main__':

      import zHTTP

      def getMessage():
            html = zHTTP.get(HOME_URL)
            listname = MiaopaParser()
            return listname.getMsg(html)

      for i in range(3):
            text = getMessage()
            print (text)