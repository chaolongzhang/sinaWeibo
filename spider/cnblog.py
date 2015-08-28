# -*- coding: utf-8 -*-

from sgmllib import SGMLParser

from utility import attrs2dic


HOME_URL = "http://www.cnblogs.com"


class CnblogParser(SGMLParser):
      def __init__(self):
            SGMLParser.__init__(self)
            

      def reset(self):
            self.parseNext = True
            self.parseContent = False
            self.parseTitle = False
            self.parseP = False
            self.hasValue = False
            self.url = ""
            self.title = ""
            self.msg = ""

            SGMLParser.reset(self)


      def start_div(self, attrs):
            nodes = attrs2dic(attrs)
            if not self.hasValue and "class" in nodes and nodes["class"] == "post_item_body":
                  self.hasValue = True
                  self.parseContent = True


      def start_a(self, attrs):
            if not self.parseContent:
                  return

            nodes = attrs2dic(attrs)
            self.url = nodes["href"]
            self.parseTitle = True


      def start_p(self, attrs):
            if self.parseContent:
                  self.parseContent = False
                  self.parseP = True


      def handle_data(self, text):
            if self.parseTitle:
                  self.title = text
                  self.parseTitle = False
            elif self.parseP:
                  self.parseP = False
                  self.msg = text.replace("\r", "").replace("\n", "");
                  print self.msg

      def getMsg(self):
            return "%s %s" % (self.title, self.url)



if __name__ == '__main__':

      import http

      def getMessage():
            html = http.get(HOME_URL)
            listname = CnblogParser()
            listname.feed(html)
            return listname.getMsg()

      for i in range(3):
            text = getMessage()
            print (text)