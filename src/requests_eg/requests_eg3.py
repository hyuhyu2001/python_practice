#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:     jinzj
@desc:
requests学习教程3
处理响应-基本API
"""

import requests

response =requests.get('https://api.github.com')
print '状态码，具体解释'
print response.status_code,response.reason
print '头部信息'
print response.headers
print 'URL信息'
print response.url
print 'redirect 信息'
print response.history #https打印为空，可改为http，打印为[<Response [301]>]
print '耗费时长'
print response.elapsed
print 'request 信息'
print response.request.method

print '----------------------'

print  '编码信息'
print response.encoding
print '消息主体内容：byte'
print response.content,type(response.content) #<type 'str'>
print '消息主体内容：解析'
print response.text,type(response.text)  # <type 'unicode'>
print '消息主体内容'
print response.json(),type(response.json())#<type 'dict'>

