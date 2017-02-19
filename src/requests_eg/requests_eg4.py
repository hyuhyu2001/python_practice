#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:     jinzj
@desc:
requests学习教程4
处理响应-下载图片、文件
"""

import  requests

def download_image():
    '''demo：下载图片'''
    # 伪造headers信息，浏览器模拟
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'}
    # 限定url
    url  = 'http://img3.imgtn.bdimg.com/it/u=2228635891,3833788938&fm=21&gp=0.jpg'
    response = requests.get(url, headers=headers, stream=True)  #stream用流的方式来传播
    #print response.content  #直接打印图片不能，打印会为乱码，通过下面的方式解决
    with open('demo.jpg','wb') as fd:   #执行完成后，会在默认脚本的目录下，下载demo.jpg文件
        for chunk in response.iter_content(128):
            fd.write(chunk)

def download_image_improved():
    """demo: 下载图片
    """
    # 伪造headers信息，浏览器模拟
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'}
    # 限定url
    url = "http://img3.imgtn.bdimg.com/it/u=2228635891,3833788938&fm=21&gp=0.jpg"
    response = requests.get(url, headers=headers, stream=True)
    from contextlib import closing #contextlib管理上下文信息，自动close
    with closing(requests.get(url, headers=headers, stream=True)) as response:
        # 打开文件
        with open('demo1.jpg', 'wb') as fd:
            # 每128写入一次
            for chunk in response.iter_content(128):
                fd.write(chunk)


if __name__ == '__main__':
    download_image_improved()