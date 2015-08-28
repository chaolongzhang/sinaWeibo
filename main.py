# -*- coding: utf-8 -*-

import sendWeibo

from config import USER_NAME, PASSWD
from sinaWeiboLogin import wblogin

if __name__ == '__main__':
    (http, uid) = wblogin(USER_NAME, PASSWD)
    http.get('http://weibo.com/')
    task =  sendWeibo.WeiboTask(http, uid)
    task.start()