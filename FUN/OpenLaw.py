# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:17:28 2018

@author: Administrator
"""

#import requests
#import re
#import execjs
#import time
##from get_proxy import func_proxy
#ip_list = []
#header1 = {
#    'Host': 'openlaw.cn',
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
#    'Accept-Encoding': 'gzip, deflate',
#    'Connection': 'keep-alive',
#    'Upgrade-Insecure-Requests': '1'
#}
## 代理ip
##ip_list.append(func_proxy())
#resp = requests.get(url='http://openlaw.cn/judgement/a66ac059bf924212a9b90f740e098060',headers=header1)
# 
#content = resp.text
##带有js混淆加密内容html标签
#print(content)
## 第一次请求服务端返回的SESSION
#session1 = resp.headers['Set-Cookie'].split("=")[1].split(';')[0]
## 生成token的必要参数，正则提取
#js1 = re.findall(r'_003(\s{1})=(\s{1})(.*?);', content, re.S)[0][2]
## 主要的js混淆加密代码，正则提取
#js2 = re.findall(r'\$\.\$\(\$\.\$\(\$\.\$\$\+(.*?)\)\(\)\)\(\);', content, re.S)[0]
#file = "jube.js"
## 加载js文件，
#ctx = execjs.get().compile(open(file, encoding='utf-8').read())
#data = ctx.call('Encrypted', js2)
# 
#func_js = data[213:-196]
## 执行生成c_token的方法，返回c_toke
#ctx2 = execjs.compile(func_js).call('_a', eval(js1))
# 
#header1 = {
#    'Host': 'openlaw.cn',
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
#    'Accept-Encoding': 'gzip, deflate',
#    'Cookie': 's_token=%s; c_token=%s; SESSION=%s' % (
#    eval(js1), ctx2, session1),
#    'Connection': 'keep-alive',
#    'Upgrade-Insecure-Requests': '1',
#    'Referer': 'http://openlaw.cn/judgement/a66ac059bf924212a9b90f740e098060'
#}
# 
#resp = requests.get(url='http://openlaw.cn/judgement/a66ac059bf924212a9b90f740e098060', proxies=ip_list[0],headers=header1)
#print(resp.content.decode())
import requests
import re
from lxml import html
#抓取详细信息
class OpenLawSpider:
    #页面初始化
    def __init__(self):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"
        }
    # 获取详细
    def getLawDetail(self):
        url = 'http://openlaw.cn/search/judgement/type?causeId=d8347b89678645e1887045b4200e822f'
        host = {'host': 'openlaw.cn',}
        headers = self.headers.copy()
        headers.update(host, )

        # 第一步，获取js文件内容
        ret_origin = requests.get(url, headers=headers)
        print(ret_origin.text)
        cookies = requests.utils.dict_from_cookiejar(ret_origin.cookies)
        # 第二步，js代码并还原j_token计算过程，正则匹配window.v
        cmp = re.compile('window.v="(.*)";')
        rst = cmp.findall(ret_origin.text)
        v_token = 'abcdefghijklmnopqrstuvwxyz'
        if len(rst):
            v_token = rst[0]
        j_token = v_token[2:4] + 'n' + v_token[0:1] + 'p' + v_token[4:8] + 'e' + v_token[1:2] + v_token[len(v_token)-17:] + v_token[8:16]
        cookies['j_token'] = j_token
        ret_next = requests.get(url, headers=headers, cookies = cookies)
        response = html.fromstring(ret_next.text)
        items = response.cssselect("div[id=primary] .ht-container .entry-title a")
        for item in items:
            title = item.text_content()
            print(title)

spider = OpenLawSpider()
spider.getLawDetail()