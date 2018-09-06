# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:56:24 2018

@author: Administrator
"""
import re

with open('qyml.txt','r') as f:
    f = ''.join(f)
    s1 = re.split(',', f)
for i in s1:
    if i:
        print(i)
        break
  

