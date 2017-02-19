#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:     jinzj
@desc:
requests学习教程6
走进requesrs库 HTTP认证
"""

import  requests

BSER_URL = 'https://api.github.com'

def construct_url(end_point):
    return '/'.join([BSER_URL,end_point])

def basic_auth():
    '''基本认证
    '''
    response = requests.get(construct_url('user'),auth = ('hyuhyu2001@163.com','123456') )
    print response.text
    print response.request.headers

#basic_auth()  #'基本认证，headers上加了下面一串码：Authorization': 'Basic aHl1aHl1MjAwMUAxNjMuY29tOmpydHkxMzI2M23',  base64的码

import base64
#print  base64.b64decode('aHl1aHl1MjAwMUAxNjMuY29tOmpydHkxMzI2M23')  #bsse64解码出来 用户名和密码 hyuhyu2001@163.com:123456

#OAUTH认证 第三方认证，获取一些公共信息，第三方认证
#github可以新生成一个token，可以设置这个token有哪些权限

def basic_oauth():
    headers = {'Authorization':'token dd6322fa6c57a548268453dc245cbcdc352a7811'}
    #user/emails
    response = requests.get(construct_url('user/emails'),headers = headers)
    print response.request.headers
    print response.text
    print response.status_code

#basic_oauth()

from requests.auth import AuthBase
class GithubAuth(AuthBase):
    def __init__(self,token):
        self.token = token

    def __call__(self, r):
        #requests加headers
        r.headers['Authorization'] = ''.join(['token',self.token])
        return r

def oauth_advanced():
    auth = GithubAuth ('dd6322fa6c57a548268453dc245cbcdc352a7811')
    response = requests.get(construct_url('user/emails'),auth = auth)
    print response.request.headers
    print response.text
    print response.status_code

oauth_advanced()