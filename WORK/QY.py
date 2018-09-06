# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 09:23:12 2018

@author: Administrator
"""

import requests
from lxml import etree
#
url = 'http://b2b.huangye88.com/'
Province = ['sichuan','guangdong','zhejiang','jiangsu','hebei','shandong','fujian','hubei','liaoning','anhui','hunan','shanxi','jiangxi','shanxi','guangxi','heilongjiang','jilin','yunnan','xinjiang','gansu','guizhou','neimenggu','hainan','ningxia','qinghai','xizang']
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
#url1 = 'http://b2b.huangye88.com/jiangsu/jixie/'
#req = requests.get(url1,headers=headers)
#response = req.text
#dom_tree = etree.HTML(response)
l = ['1','3','4','6','7','9','10','12','13','15','16','18','19','21','22','24','25','27','28','30']
for x in Province:
    url = 'http://b2b.huangye88.com/%s/led/'%x
    for i in range(3,10000):
        url1 = url + 'pn%s'%i
        req = requests.get(url1,headers=headers)
        if req.url!= 'http://b2b.huangye88.com/%s/led/'%x:
            response = req.text
            dom_tree = etree.HTML(response)
            for q in l:
                text = dom_tree.xpath('//*[@id="jubao"]/dl[%s]/dt/h4//text()'%q)
                if text:
                    text1 = text[0]
                    try:
                        with open('qymlled.txt','a') as f:
                            f.write(text1+',')
                    except:
                        pass
            print(req.url)
        elif req.url== 'http://b2b.huangye88.com/%s/led/'%x:
            print('开始抓取下一个省份')
            break
       

#url = 'http://b2b.huangye88.com/%s/jixie/pn100000'
#req = requests.get(url,headers=headers)
#response = req.text
#
#print(response)
#print(req.status_code)
#print(req.url)


