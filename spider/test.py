import os

# for test
import sys
sys.path.insert(0, '..')

from cnbeta import CnbetaParser
from cnblog import CnblogParser
from miaopai import MiaopaParser
from myBlog import MyBlogParser
from techweb import TechwebParser
from tuicool import TuicoolParser

if __name__ == '__main__':
    types = [
        CnbetaParser,
        CnblogParser,
        MiaopaParser,
        MyBlogParser,
        TechwebParser,
        TuicoolParser
    ]
    for c in types:
        print(os.linesep + '************* ' + str(c) + ' start *************')
        try:
            p = c()
            for i in range(1):
                weibo = p.get_weibo_message()
                print(weibo)
                print('has image: ' + str(weibo.has_image))
                print(str(c) + 'text success!')
        except Exception as e:
            print(e)
            print(str(c) + ' failure!')

        print('************* ' + str(c) + ' end *************' + os.linesep)
