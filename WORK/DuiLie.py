# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 16:28:17 2018

@author: Administrator
"""

from queue import Queue

q = Queue(maxsize=10)
a = []
for i in range(5):
    q.put(i)
    print(q.get())
#    a.append(q.get())
#    print(a)