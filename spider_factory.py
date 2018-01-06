from spider.cnbeta import CnbetaParser
from spider.cnblog import CnblogParser
from spider.miaopai import MiaopaParser
from spider.myBlog import MyBlogParser
from spider.techweb import TechwebParser
from spider.tuicool import TuicoolParser

spiders = [
    MyBlogParser(),
    CnbetaParser(),
    CnblogParser(),
    MiaopaParser(),
    MyBlogParser(),
    TechwebParser(),
    TuicoolParser()
]

currentIndex = 0
count = len(spiders)

def nextSpider():
    global currentIndex
    spider = spiders[currentIndex]
    currentIndex = (currentIndex + 1) % count
    return spider
