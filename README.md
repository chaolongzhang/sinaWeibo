# Python代码登录新浪微博并自动发微博，不使用SDK

## 功能

* 登录微博网页端，包括使用用户名和扫码登录两种方式；
* 从其它网站（秒拍、cnBeta、博客园、TechWeb、推酷等）爬取内容;
* 把爬取的内容转发到微博。
* 微博支持发文字和图文。

**注: 已兼容Python2和3。建议使用Python3，Python2下可能出现字符编码问题。**

## 使用

1.  根据注释修改配置文件`config.py`。
2.  运行`main.py`，`python main.py`。

注意：
1. 该代码使用了代码依赖[requests](http://docs.python-requests.org/en/master/)、[rsa](https://pypi.python.org/pypi/rsa)、[beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)和PIL(使用扫码登录)，没有安装的话需要先安装：

```
pip install rsa
pip install requests
pip install beautifulsoup4
pip install PIL
```
或者

```
pip install -r requirements.txt
```

2. 如果你的微博登录时需要输入验证码，该代码是登录不成功的，在使用该代码前请取消微博的登陆验证码。

更多内容请参考：[Python代码登录新浪微博并自动发微博](http://chaolongzhang.github.io/2015/code-login-sina-weibo-update-weibo/ )

## 更新

* 2018-01-06：增加扫码登录功能。

## License

sinaWeibo is published under GNU GPLv3 License. See the LICENSE file for more.

## 捐赠

如果您觉得该工具对你有帮助，欢迎给我一定的捐赠。

**支付宝扫码捐赠**

![](./doc/donate-alipay.png)

**微信扫码捐赠**

![](./doc/donate-wechatpay.png)

