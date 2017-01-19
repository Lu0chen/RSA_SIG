#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-04-10 12:31:06
# @Last Modified by:   anchen
# @Last Modified time: 2016-05-09 20:47:46

import re
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf8')


url = "http://huaban.com/boards/19570858/"

def cbk(a,b,c):
    '''
    进度追踪器
    '''
    download = 100.0*a*b/c
    if download > 100:
        download = 100
    print '%.2f%%'%download

def get_content(url):
    '''
    获取页面源代码
    '''
    html = urllib.urlopen(url)
    content = html.read()
    html.close()

    return content

info = get_content(url)

def get_img(info):
    '''
    通过正则表达式识别并下载图片`
    '''
    regex = '<img src="(.+?\_fw236)"'

    pet = re.compile(regex)

    img_code = re.findall(pet,info)

    i = 0

    for img_url in img_code:
        print img_url

        urllib.urlretrieve(img_url,'%s.jpg' % i,cbk)
        i = i + 1

    return  img_code

info = get_content(url)
print get_img(info)