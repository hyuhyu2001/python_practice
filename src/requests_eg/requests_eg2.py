#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:     jinzj
@desc:
requests学习教程2
github的api地址：https://developer.github.com/  https://developer.github.com/v3/
GET:查看资源
POST：增加资源
PUT：修改资源
DELETE：删除资源
HEAD：查看响应头
OPTIONS：查看可用请求方法
requests使用某种方法：requests.[method](url)
#github api实例 https://developer.github.com/v3/users/
#发送请求学习
"""

import json
import requests
from requests import exceptions

URL = 'https://api.github.com'


#辅助性方法，构建一个URL
def build_uri(endpoint):
    return '/'.join([URL, endpoint])

#得到的输出更好的打印出来
def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4) #缩进为4

def request_method():
    response = requests.get(build_uri('users/imoocdemo'))
    #response = requests.get(build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo')) #auth账户名和密码
    print better_print(response.text)

def params_request():
    response = requests.get(build_uri('users'), params={'since': 11})
    print better_print(response.text)
    print response.request.headers
    print response.url

#patch方法
def json_request():
    #response = requests.patch(build_uri('user'), auth=('imoocdemo', 'imoocdemo123'),json={'name': 'babymooc2', 'email': 'hello-world@imooc.org'}) #patch，修改name和email
    response = requests.post(build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'),json=['helloworld@github.com']) #post，增加一个email信息
    print better_print(response.text)
    print response.request.headers
    print response.request.body
    print response.status_code

def timeout_request():
    try:
        response = requests.get(build_uri('user/emails'), timeout=10) #timeout10秒超时，timeout(3,7)分为请求3秒，返回7秒
        response.raise_for_status()
    except exceptions.Timeout as e:
        print e.message #打印超时的错误 'Connection to api.github.com timed out. (connect timeout=0.01)
    except exceptions.HTTPError as e:
        print e.message #打印没有认证的错误 401 Client Error: Unauthorized for url: https://api.github.com/user/emails
    else:
        print response.text
        print response.status_code

#自定义requests
def hard_requests():
    from requests import Request, Session
    s = Session() #初始化session
    headers = {'User-Agent': 'fake1.3.4'}
    req = Request('GET', build_uri('user/emails'), auth=('hyuhyu2001@163.com', '123456'), headers=headers)
    prepped = req.prepare()
    print prepped.body
    print prepped.headers

    resp = s.send(prepped, timeout=5)
    print resp.status_code
    print resp.request.headers
    print resp.text


if __name__ == '__main__':
    hard_requests()