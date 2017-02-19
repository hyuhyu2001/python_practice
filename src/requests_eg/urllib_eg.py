#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
urllib学习教程
1、urllib、urllib2、urllib3不是进化关系
2、urllib和urllib2是相互独立的模块
3、requests库使用了urllib3（可以多次请求重复使用一个socket）
"""

import urllib2
import urllib

URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'

def use_simple_urllib2():
    response =  urllib2.urlopen(URL_IP)
    print '>>>>Response Headers:'
    print response.info()
    print '>>>>Response Body:'
    print ''.join([line for line in response.readlines()])

def use_params_urllib2():
    #构建请求参数
    params = urllib.urlencode({'param1':'hello','param2':'world'})
    print '>>>>Request Params:'
    print params
    #发送请求
    response = urllib2.urlopen('?'.join([URL_GET,'%s'])%params)
    #处理响应
    print '>>>>Response Headers:'
    print response.info()
    print '>>>>Status Code:'
    print response.getcode()
    print '>>>>Response Body:'
    print ''.join([line for line in response.readlines()])

def github_timeline():
    '''获取github的公共时间线'''
    url = 'https://github.com/timeline.json' #github时间线，此种方式获取其他网站http://www.bing.com正常
    req = urllib2.Request(url)
    response = urllib2.urlopen(url)
    html = response.read()
    print html
    '''不能抓取的原因是：410 gone  410响应主要的目的是为了web维护任务，这通过告诉接收者资源已经不可得了并且告诉接收者服务器拥有者已经把那个资源的远程连接给移除了。
    对有时间限制的，推销性的服务，和对不再继续工作在服务器站点人员的资源，这个事件（410响应）是非常普遍的。
    它不需要把所有长久不可得的资源标记为“gone”或者保持任意长时间—这需要服务器拥有者自己的判断'''

def github_timeline_requests():
    import requests, os, time
    url = 'https://github.com/timeline.json'#用requests能抓取
    start = time.clock()
    html = requests.get(url, allow_redirects=True)
    end = time.clock()
    print html.status_code  #410状态码
    print html.text

if __name__ == '__main__':
    print '>>>>Use Simple urllib2:'
    use_simple_urllib2()
    print '---------------------------'
    print '>>>>Use params urllib2:'
    use_params_urllib2()
    print '>>>>github_timeline:'
    #github_timeline()
    print '>>>>github_timeline_requests:'
    github_timeline_requests()
