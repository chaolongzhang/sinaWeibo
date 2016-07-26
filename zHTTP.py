# -*- coding: utf-8 -*-

import requests

import sys
sys.path.append("..")
from config import user_agent

def get(url):
      session = initSession()
      resp = session.get(url)
      resp.encoding = "utf-8"
      return resp.text


def initSession():
      session = requests.session()
      session.headers['User-Agent'] = user_agent
      return session



