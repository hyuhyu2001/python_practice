#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
requests学习教程
requests作者的学习网站：httpbin.org

Http协议：request分为（1）start line：方法 地址和协议 （2）Headers： key：value
response分为（1）Start line：状态码 具体解释（2）Headers： key：value
"""
'''
r1 = requests.get('http://www.zhidaow.com') # 发送请求
print r1.status_code # 返回码
print r1.headers['content-type'] # 返回头部信息
print r1.encoding # 编码信息
print r1.content #r.text内容部分（PS，由于编码问题，建议这里使用r.content）

'''

import requests

URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'

def use_simple_requests():
    response =  requests.get(URL_IP)
    print '>>>>Response Headers:'
    print response.headers
    print '>>>>Response Body:'
    print response.text

def use_params_requests():
    #构建请求参数
    params ={'param1':'hello','param2':'world'}
    #发送请求
    response = requests.get(URL_GET,params = params)
    #处理响应
    print '>>>>Response Headers:'
    print response.headers
    print '>>>>Status Code:'
    print response.status_code
    print '>>>>Response Body:'
    print response.text

if __name__ == '__main__':
    print '>>>>Use Simple requests:'
    use_simple_requests()
    print '---------------------------'
    print '>>>>Use params requests:'
    use_params_requests()
