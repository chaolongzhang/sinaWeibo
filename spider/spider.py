# -*- coding: utf-8 -*-

import requests
from config import USER_AGENT

class Spider(object):
    '''spider base class'''

    def __init__(self, home_url):
        super(Spider, self).__init__()
        self.home_url = home_url
        self.session = requests.session()
        self.session.headers['User-Agent'] = USER_AGENT

    def download_text(self):
        '''get raw text such as html、json、or so on'''
        resp = self.session.get(self.home_url)
        resp.encoding = "utf-8"
        return resp.text

    def get_weibo_message(self):
        pass
