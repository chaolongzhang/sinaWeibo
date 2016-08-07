# -*- coding: utf-8 -*-

import send_task

from weibo.weibo_login import wblogin

if __name__ == '__main__':
    (http, uid) = wblogin()
    http.get('http://weibo.com/')
    task =  send_task.SendTask(http, uid)
    task.start()
    # task.stop()
    