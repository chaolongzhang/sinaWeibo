# -*- coding: utf-8 -*-

def attrs2dic(attrs):
      nodes = {}
      for item in attrs:
            nodes[item[0]] = item[1]
      return nodes