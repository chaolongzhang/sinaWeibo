# -*- coding: utf-8 -*-

import zHTTP


class Spider(object):
    '''spider base class'''

    def __init__(self, homeUrl):
        super(Spider, self).__init__()
        self.homeUrl = homeUrl

    def download_text(self):
        '''get raw text such as html、json、or so on'''
        text = zHTTP.get(self.homeUrl)
        return text

    def get_weibo_message(self):
        pass
