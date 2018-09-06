# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 17:11:56 2018

@author: Administrator
"""

#import requests
#
#url = 'http://openlaw.cn/search/judgement/type?causeId=d8347b89678645e1887045b4200e822f'
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
#req = requests.get(url)
#print(req.text)

import re

a = '{"code":200,"msg":"成功","data":{"authentication":"7d27f53a-81d8-419d-b772-b4ef374cc598","displayName":"yxrjj","accountType":0}}'
pattern= re.compile(r'authentication":"([\s\S]*?)","displayName')
match= pattern.search('%s'%a)
print(match.group(1))
