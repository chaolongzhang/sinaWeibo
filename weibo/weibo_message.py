# -*- coding: utf-8 -*-

import os

class WeiboMessage(object):
    """weibo message struct"""

    def __init__(self, text, images=None):
        super(WeiboMessage, self).__init__()
        self.text = text if text is not None else ""
        self.images = images

    @property
    def has_image(self):
        return self.images is not None \
            and len(self.images) > 0

    @property
    def is_empty(self):
        return len(self.text) == 0 \
            and not self.has_image

    def get_send_data(self, pids=''):
        data = {
            "location": "v6_content_home",
            "appkey": "",
            "style_type": "1",
            "pic_id": pids,
            "text": self.text,
            "pdetail": "",
            "rank": "0",
            "rankid": "",
            "module": "stissue",
            "pub_type": "dialog",
            "_t": "0",
        }
        return data

    def __str__(self):
        return "text: " + self.text + os.linesep \
            + "images: " + str(self.images)
