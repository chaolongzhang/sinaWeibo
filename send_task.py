# -*- coding: utf-8 -*-

from threading import Thread, Event
import spider_factory
from config import TIME_SLOG
from weibo.weibo_sender import WeiboSender
from logger import logger


class SendTask(Thread):

    def __init__(self, http, uid):
        Thread.__init__(self)
        self.stopped = Event()
        self.sender = WeiboSender(http, uid)

    def run(self):
        logger.info("start task...")
        self.sendWeibo()
        while not self.stopped.wait(TIME_SLOG):
            self.sendWeibo()
        logger.info("end task...")

    def stop(self):
        self.stopped.set()

    def sendWeibo(self):
        spider = spider_factory.nextSpider()
        weibo = spider.get_weibo_message()
        self.sender.send_weibo(weibo)
