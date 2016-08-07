# Python纯代码登录新浪微博并自动发微博，不使用SDK

用Python模拟HTTP操作，实现微博登陆、定时从秒拍、cnBeta、博客园、TechWeb、推酷获取最新的内容，再转发到微博。

**注: 已兼容Python2和3。**

## 使用

1.  修改配置文件`config.py`，把微博账号和密码改为你自己的，还可以设置发送时间（默认是30分钟一次）。
2.  在`TextFactory.py`可以设置微博内容生成规则，也可以使用默认的规则。
3.  运行`main.py`，`python main.py`。

注意：
1. 该代码使用了代码依赖[requests](http://docs.python-requests.org/en/master/)、[rsa](https://pypi.python.org/pypi/rsa)和[beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)，没有安装的话需要先安装：

```
pip install rsa
pip install requests
pip install beautifulsoup4
```

2. 如果你的微博登录时要输入验证码，该代码是登录不成功的。

更多内容请参考：[Python代码登录新浪微博并自动发微博](http://blog.5long.me/2015/code-login-sina-weibo-update-weibo/ )

解决验证码登录问题、更多功能(sinaWeiboPro)请联系[开发者](http://blog.5long.me/)。

## License

sinaWeibo is published under GNU GPLv3 License. See the LICENSE file for more.
