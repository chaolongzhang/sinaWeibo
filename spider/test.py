import os

# for test
import sys
sys.path.insert( 0, '..' )

from spider.cnbeta import CnbetaParser
from spider.cnblog import CnblogParser
from spider.miaopai import MiaopaParser
from spider.myBlog import MyBlogParser
from spider.techweb import TechwebParser
from spider.tuicool import TuicoolParser

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
        print( os.linesep + '************* ' + str( c ) + ' start *************' )
        try:
            p = c()
            for i in range(1):
                weibo = p.get_weibo_message()
                print ( weibo )
                print( 'has image: ' + str( weibo.has_image ) )
                print( str( c ) + 'text success!' )
        except Exception as e:
            print(e)
            print( str( c ) + ' failure!' )
        
        print( '************* ' + str( c ) + ' end *************' + os.linesep )