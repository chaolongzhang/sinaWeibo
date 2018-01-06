# -*- coding: utf-8 -*-

import time
import re
import json
from weibo.weibo_message import WeiboMessage
from config import ADD_WATERMARK, WATERMARK_URL, WATERMARK_NIKE
from config import MAX_IMAGES
from logger import logger


if MAX_IMAGES < 0 or MAX_IMAGES > 9:
    MAX_IMAGES = 9


class WeiboSender(object):

    def __init__(self, session, uid):
        super(WeiboSender, self).__init__()
        self.session = session
        self.uid = str(uid)
        self.Referer = "http://www.weibo.com/u/%s/home?wvr=5" % self.uid

    def send_weibo(self, weibo):
        if not isinstance(weibo, WeiboMessage):
            raise ValueError('weibo must WeiboMessage class type')
            logger.debug('weibo must WeiboMessage class type')
        if weibo.is_empty:
            logger.info('没有获得信息，不发送')
            return

        pids = ''
        if weibo.has_image:
            pids = self.upload_images(weibo.images)
        data = weibo.get_send_data(pids)
        self.session.headers["Referer"] = self.Referer
        try:
            self.session.post("https://www.weibo.com/aj/mblog/add?ajwvr=6&__rnd=%d"
                              % int(time.time() * 1000),
                              data=data)
            logger.info('微博[%s]发送成功' % str(weibo))
        except Exception as e:
            logger.debug(e)
            logger.info('微博[%s]发送失败' % str(weibo))

    def upload_images(self, images):
        pids = ""
        if len(images) > MAX_IMAGES:
            images = images[0: MAX_IMAGES]
        for image in images:
            pid = self.upload_image_stream(image)
            if pid:
                pids += " " + pid
            time.sleep(10)
        return pids.strip()

    def upload_image_stream(self, image_url):
        if ADD_WATERMARK:
            url = "http://picupload.service.weibo.com/interface/pic_upload.php?\
            app=miniblog&data=1&url=" \
                + WATERMARK_URL + "&markpos=1&logo=1&nick=" \
                + WATERMARK_NIKE + \
                "&marks=1&mime=image/jpeg&ct=0.5079312645830214"

        else:
            url = "http://picupload.service.weibo.com/interface/pic_upload.php?\
            rotate=0&app=miniblog&s=json&mime=image/jpeg&data=1&wm="

        # self.http.headers["Content-Type"] = "application/octet-stream"
        image_name = image_url
        try:
            f = self.session.get(image_name, timeout=30)
            img = f.content
            resp = self.session.post(url, data=img)
            upload_json = re.search('{.*}}', resp.text).group(0)
            result = json.loads(upload_json)
            code = result["code"]
            if code == "A00006":
                pid = result["data"]["pics"]["pic_1"]["pid"]
                return pid
        except Exception as e:
            logger.info(u"图片上传失败：%s" % image_name)
        return None
