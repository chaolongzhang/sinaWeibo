# -*- coding: utf-8 -*-

import time
from threading import Timer


import TextFactory

from config import TIME_SLOG, TIMER_REPEAT
from logger import log


class WeiboTask(object):
      def __init__(self, http, uid):
            super(WeiboTask, self).__init__()
            self.http = http
            self.uid = uid

      def start(self):
            log("开始任务")
            self.sendWeibo()
            self.newTimer()

      def newTimer(self):
            self.timer = Timer(TIME_SLOG, self.main, ()).start()

      def stop(self):
            log("结束任务")
            self.timer.cancel()
            pass

      def main(self):
            self.sendWeibo()

            if TIMER_REPEAT:
                  self.newTimer()

      def sendWeibo(self):
            text = TextFactory.getText()
            self.update(text)
            log(u"发送微博：" + text)


      def update(self, text):
            data = {
                  "location" : "v6_content_home", 
                  "appkey" : "", 
                  "style_type" : "1", 
                  "pic_id" : "", 
                  "text" : text, 
                  "pdetail" : "", 
                  "rank" : "0", 
                  "rankid" : "", 
                  "module" : "stissue", 
                  "pub_type" : "dialog", 
                  "_t" : "0", 
            }
            self.http.headers["Referer"] = "http://www.weibo.com/u/%s/home?wvr=5" % str(self.uid)
            resp = self.http.post(
                        "http://www.weibo.com/aj/mblog/add?ajwvr=6&__rnd=%d" % int(time.time() * 1000),
                        data = data
                  )

