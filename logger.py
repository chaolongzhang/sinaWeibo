# -*- coding: utf-8 -*-

from datetime import datetime

def log(msg):
      text = "[%s]:%s" % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), msg)
      print (text)