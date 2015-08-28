# -*- coding: utf-8 -*-

from sgmllib import SGMLParser

from utility import attrs2dic


HOME_URL = "http://www.techweb.com.cn/roll"


class TechwebParser(SGMLParser):
      def __init__(self):
            SGMLParser.__init__(self)


      def reset(self):
            self.parseNext = True
            self.parseContent = False
            self.parseTitle = False
            self.hasValue = False
            self.url = ""
            self.title = ""
            self.msg = ""

            SGMLParser.reset(self)


      def start_div(self, attrs):
            nodes = attrs2dic(attrs)
            if not self.hasValue and "class" in nodes and nodes["class"] == "newslist":
                  self.parseContent = True
                  self.hasValue = True


      def start_a(self, attrs):
            if not self.parseContent:
                  return
            self.parseContent = False
            nodes = attrs2dic(attrs)
            self.url = "%s" % nodes["href"]
            self.parseTitle = True


      def end_a(self):
            pass


      def handle_data(self, text):
            if self.parseTitle:
                  self.parseTitle = False
                  self.title = text.strip()


      def getMsg(self):
            return "%s %s" % (self.title, self.url)



if __name__ == '__main__':

      import http

      def getMessage():
            html = http.get(HOME_URL)
            listname = TechwebParser()
            listname.feed(html)
            return listname.getMsg()

      for i in range(3):
            text = getMessage()
            print (text)