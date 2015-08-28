# -*- coding: utf-8 -*-

from sgmllib import SGMLParser

from utility import attrs2dic


HOME_URL = "http://www.tuicool.com"


class TuicoolParser(SGMLParser):
      def __init__(self):
            SGMLParser.__init__(self)

      def reset(self):
            self.hasValue = False
            self.title = ""
            self.url = ""

            SGMLParser.reset(self)


      def start_a(self, attrs):
            if self.hasValue:
                  return
            nodes = attrs2dic(attrs)
            if "class" in nodes and nodes["class"] == "title":
                  hasValue = True
                  self.title = nodes["title"]
                  self.url = "%s%s" % (HOME_URL, nodes["href"])

      def getMsg(self):
            return "%s %s" % (self.title, self.url)


if __name__ == '__main__':

      import http

      def getMessage():
            html = http.get(HOME_URL)
            listname = TuicoolParser()
            listname.feed(html)
            return listname.getMsg()

      for i in range(3):
            text = getMessage()
            print (text)
            






