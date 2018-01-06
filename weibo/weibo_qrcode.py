# -*- coding: utf-8 -*-

'''
二维码登录新浪微博
'''

import requests
import time
import re
import sys
from PIL import Image
import threading
from config import USER_AGENT

session = requests.session()
session.headers['User-Agent'] = USER_AGENT

def open_img(image_name):
    img = Image.open(image_name)
    img.show()

def login():
    image_name, qrcode_qrid = get_qrcode()
    thread = threading.Thread(target=open_img, name="open", args=(image_name,))
    thread.start()
    
    wait_scan(qrcode_qrid)
    alt = wait_confirm(qrcode_qrid)
    
    data = {
        "entry": "weibo",
        "returntype": "TEXT",
        "crossdomain": 1,
        "cdult": 3,
        "domain": "weibo.com",
        "alt": alt,
        "savestate": 30,
        "callback": "STK_" + str(int(time.time() * 100000))
    }

    login_url_list = "http://login.sina.com.cn/sso/login.php"
    login_list_page = session.get(login_url_list, params=data)
    url_list = [i.replace("\/", "/") for i in login_list_page.text.split('"') if "http" in i]
    for i in url_list:
        session.get(i)
        time.sleep(0.5)

    return session

def wait_scan(qrcode_qrid):
    '''
    提示扫描二维码，直到扫描完成
    '''
    scaned = False
    while not scaned:
        print('请扫描二维码')
        qrcode_check_page = scan_qrcode(qrcode_qrid, str(int(time.time() * 10000)))
        if "50114002" in qrcode_check_page:
            scaned = True
            print('扫描成功，请点击确认登录')
        time.sleep(2)

def wait_confirm(qrcode_qrid):
    '''
    提示点击确认登录，直到点击确认
    '''
    confirm = False
    while not confirm:
        qrcode_click_page = scan_qrcode(qrcode_qrid, str(int(time.time() * 100000)))
        if "succ" in qrcode_click_page:
            confirm = True
            alt = re.search(r'"alt":"(?P<alt>[\w\-\=]*)"', qrcode_click_page).group("alt")
            print('登录成功')
        time.sleep(2)
    return  alt

def get_qrcode():
    '''
    获取登录二维码
    :return:
    '''
    qrcode_url = "http://login.sina.com.cn/sso/qrcode/image?entry=weibo&size=180&callback=STK_" \
                    + str(int(time.time() * 10000))
    qrcode_page = session.get(qrcode_url)
    if qrcode_page.status_code != 200:
        sys.exit('可能微博改了接口!')

    qrcode_text = qrcode_page.text
    qrcode_image = re.search(r'"image":"(?P<image>.*?)"', qrcode_text).group("image").replace("\/", "/")
    if not qrcode_image.startswith('http:'):
        qrcode_image = 'http:' + qrcode_image
    qrcode_qrid = re.search(r'"qrid":"(?P<qrid>[\w\-]*)"', qrcode_text).group("qrid")
    qr_page = session.get(qrcode_image)
    image_name = "qr_login." + qr_page.headers['content-type'].split("/")[1]
    with open(image_name, 'wb') as f:
        f.write(qr_page.content)
        f.close()
    return image_name, qrcode_qrid

def scan_qrcode(qrcode_qrid, _time):
    params = {
        "entry": "weibo",
        "qrid": qrcode_qrid,
        "callback": "STK_" + _time
    }
    qrcode_check = "http://login.sina.com.cn/sso/qrcode/check"
    return session.get(qrcode_check, params=params).text

def wblogin():
    index_url = "http://weibo.com/"
    session = login()
    resp = session.get(index_url)
    uid = re.search(r"\$CONFIG\['uid'\]=(.*);", resp.text).group(1)
    return (session, uid)

if __name__ == '__main__':
    (session, uid) = wblogin()
    text = session.get('http://weibo.com/').text
    print(text)
