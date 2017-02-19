#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:     jinzj
@desc:
requests学习教程5
处理响应-事件钩子event hooks
钩子是事件驱动性的开发，事件完成后引起的一些动作
"""

import requests

def get_key_info(response,*arg,**kwargs):
    '''回调函数
    '''
    print response.headers['Content-Type']

def main():
    '''主程序
    '''
    requests.get('https://api.github.com',hooks = dict(response = get_key_info))

main() #application/json; charset=utf-8