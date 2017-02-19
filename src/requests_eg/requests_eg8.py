#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
致力于打造最详细的Requests使用
http://blog.csdn.net/mrlevo520/article/details/52006481
"""

import requests
import json
import base64

def base():
    url='https://github.com/timeline.json' #github的公共时间线
    response = requests.get(url)
    print response.text
    print type(response.text)   #<type 'unicode'>
    print response.content
    print type(response.content) #<type 'str'>
    print  response.json()     #等同于text = json.loads(response.content)
    print type(response.json())  #<type 'dict'>，这样便可以当字典处理，查看所有键、值、（键，值）对：dict.keys()、dict.values()、dict.items()；返回值的类型为列表
    print  response.json().get(u'message') #打印字典里的某一key
    for key in response.json():
        print key
#凡是和字典相关的，应该想到json

def requests_data():
    '''定制请求头；post发送json数据：如果你想为请求添加HTTP头部，只要简单地传递一个 dict 给headers 参数就可以了。'''
    url= 'http://httpbin.org/post'
    payload = {'some':'data'}
    headers = {'Content-Type':'application/json'}
    response = requests.post(url,data = json.dumps(payload),headers = headers)
    print response
    print response.text

def requests_raw():
    '''原始响应内容
    在罕见的情况下你可能想获取来自服务器的原始套接字响应，那么你可以访问 r.raw 。 如果你确实想这么干，那请你确保在初始请求中设置了 stream=True '''
    url= 'https://github.com/timeline.json'
    response = requests.get(url,stream = True)
    print response.raw  #结果<requests.packages.urllib3.response.HTTPResponse object at 0x02D2DE50>
    print response.raw.read(100) #结果：{"message":"Hello there, wayfaring stranger. If you’re reading this then you probably didn’t see

def requests_form():
    '''post提交表单：增加form'''
    url = 'http://httpbin.org/post'
    payload = {'key1': 'values1','key2': 'values2'}
    html_json = requests.post(url,data = payload)
    print html_json
    print html_json.text

def requests_Multipart_Encoded():
    '''post提交文件：POST一个多部分编码(Multipart-Encoded)的文件'''
    url = 'http://httpbin.org/post'
    files = {'file':open('Inception.txt','rb')} #在脚本的根目录下增加Inception.txt的文件，脚本才能运行成功
    # files = {'file': ('report.jpg', open('/home/lyb/sjzl.mpg', 'rb'))} #显式的设置文件名
    #files = {'file': ('test.txt', b'Hello Requests.')} #把字符串当着文件进行上传:必需显式的设置文件名
    html_file = requests.post(url,files = files)
    print html_file
    print html_file.text
    print html_file.json()
    print html_file.json()['files']['file']#字典取value的结构      会被base64编码#{u'file': u'data:application/octet-stream;base64,1eLKx9K7uPay4srUo6ENCnRoaXMgaXMgYSB0ZXN0o6E='}
    #print base64.b64decode('1eLKx9K7uPay4srUo6ENCnRoaXMgaXMgYSB0ZXN0o6E=')
    #base64进行解码，打印出现乱码，问题原因是编辑txt文件时采用的是ANSI编码，把文件格式转换为utf-8，不用解码也能展现

def requests_get():
    '''响应status状态，响应header,就是字典的操作而已'''
    url = 'http://httpbin.org/get'
    html = requests.get(url)
    print html.status_code
    print html.request.headers #访问服务器发送的报头
    print html.headers
    print html.headers.get('Content-Length')

def requests_cookies():
    '''cookie简介：使用cookie跟踪用户是否已登录状态信息，一旦网站验证了你的登录权限，它就会将他们保存在你的浏览器的cookie中，里面通常包含一个服务器生成的令牌，登录有效时限和状态跟踪信息。
    访问cookies，发送cookies到服务器，可以使用cookies参数'''
    url = 'http://httpbin.org/cookies'
    html = requests.get(url)
    cookies = dict(cookies_new = 'new one')
    #cookies = {'testCookies_1': 'Hello_Python3', 'testCookies_2': 'Hello_Requests'}
    #  在Cookie Version 0中规定空格、方括号、圆括号、等于号、逗号、双引号、斜杠、问号、@，冒号，分号等特殊符号都不能作为Cookie的内容。
    html_cookies = requests.get(url,cookies = cookies)
    print html_cookies.text

def requests_cookies_login():
    '''post填充表格的话，可以省去登录页面，一个post加上登录所需的账号密码即可进行填充表单'''
    url = 'http://pythonscraping.com/pages/cookies/welcome.php'
    params = {'username':'mrlevo','password':'password'} #构造表单params
    r = requests.post(url,params)#提交表单，填充账号和密码
    r = requests.get(url,cookies = r.cookies)#在利用登陆后的cookies进行get内容操作
    print r.text

def requests_session():
    '''如果刚开始就不需要cookies而且网站比较复杂，它会暗自调整cookie时候，采用session函数进行解决，他能持续跟踪会话信息，比如cookie，header，甚至运行HTTP协议的信息，比如HTTPAdapter
    会话对象让你能够跨请求保持某些参数，最方便的是在同一个Session实例发出的所有请求之间保持cookies，且这些都是自动处理的，甚是方便'''
    url = 'http://pythonscraping.com/pages/cookies/welcome.php'
    params = {'username':'mrlevo','password':'password'}
    r = requests.session().post(url,params)#先获取session
    r = requests.session().get(url,cookies = r.cookies) #获取session的get信息
    print r.text

def requests_session_2():
    '''Session Objects会话对象 ：Session对象在请求时允许你坚持一定的参数。此外，还坚持由Session实例的所有请求的cookie'''
    url = 'http://httpbin.org/cookies/set/sessioncookie/1234567S89'
    r = requests.session().get(url)#获取session
    print r.text
    #如果你想在一个session中删除一个参数，那么你只需要设置它为none，他便自动被删去.（通过更新字典的方式更新）

def requests_base_auth():
    '''在cookie出现之前，处理网站登录最常用的方法是用HTTP基本接入认证'''
    from requests.auth import AuthBase
    from requests.auth import HTTPBasicAuth
    url = 'http://pythonscraping.com/pages/auth/login.php'
    auth = HTTPBasicAuth('mrlevo','password')
    # requests.get(URL, auth=HTTPDigestAuth('user', 'pass'))  另一种非常流行的HTTP身份认证形式是摘要式身份认证，Requests对它的支持也是开箱即可用
    r = requests.post(url,auth = auth)
    print r.text

def requests_history_wrong():
    '''重定向，请求历史与超时
    使用GET或OPTIONS时，Requests会自动处理位置重定向。Github将所有的HTTP请求重定向到HTTPS。可以使用响应对象的 history 方法来追踪重定向。'''
    url = 'http://github.com'
    html = requests.get(url)
    print html.status_code
    print html.history #结果：[<Response [301]>]
    # 301代表永久性转移(Permanently Moved)，301重定向是网页更改地址后对搜索引擎友好的最好方法，只要不是暂时搬移的情况，都建议使用301来做转址

def requests_history_correct():
    '''重定向，请求历史与超时
    Response.history 是一个:class:Request 对象的列表，为了完成请求而创建了这些对象。这个对象列表按照从最老到最近的请求进行排序。如果你使用的是GET或OPTIONS，那么你可以通过 allow_redirects 参数禁用重定向处理:'''
    url = 'http://github.com'
    html = requests.get(url,allow_redirects=False,timeout=1)  #你可以告诉requests在经过以 timeout 参数设定的秒数时间之后停止等待响应
    print html.status_code
    print html.url
    print html.history #结果：[]

'''
错误与异常
r.raise_for_status() #失败请求(非200响应)抛出异常
遇到网络问题（如：DNS查询失败、拒绝连接等）时，Requests会抛出一个ConnectionError 异常。
遇到罕见的无效HTTP响应时，Requests则会抛出一个 HTTPError 异常。
若请求超时，则抛出一个 Timeout 异常。
若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常。
所有Requests显式抛出的异常都继承自 requests.exceptions.RequestException
'''
def requests_raise():
    URL = 'http://ip.taobao.com/service/getIpInfo.php' # 淘宝IP地址库API
    try:
        r = requests.get(URL, params={'ip': '8.8.8.8'}, timeout=1)
        r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
    except requests.RequestException as e:
        print e
    else:
        result = r.json()
        print type(result)
        print result  #HTTPConnectionPool(host='ip.taobao.com', port=80): Read timed out. (read timeout=10)

def requests_encoding():
    '''采集网易主页http://www.163.com/网易采用的是gbk编码方式，使用urllib2时候，我们一般进行decode处理来达到编码转换的目的
    而requests则不是，刚开始我想当然的以为可以这样进行编码解码，其实不然，需要用html.encoding = 'gbk'来规定编码方式'''
    from bs4 import BeautifulSoup #Beautiful Soup是python的一个库，最主要的功能是从网页抓取数据,pip install beautifulsoup,很帅气的爬虫包
    url = 'http://www.163.com'
    html = requests.get(url)
    html.encoding = 'utf-8'
    bs = BeautifulSoup(html.text)
    print bs.prettify()

requests_raise()