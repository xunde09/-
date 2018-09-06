# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 16:07:01 2018

@author: Administrator
"""
import requests
from lxml import etree
from PIL import Image
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import PIL.Image as image
from PIL import Image,ImageEnhance
import time,re, random
import requests
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


broswer = webdriver.Chrome(executable_path='C:\ProgramData\Anaconda3\chromedriver.exe')
broswer.get("http://www.cdgdc.edu.cn/cqva/gateway.html")
broswer.get_screenshot_as_file('D:\\test2\\滑动验证\\yzm.jpg')
baidu = broswer.find_element_by_xpath('//*[@id="query_form"]/div[4]/div/span/img')
left = baidu.location['x']
top = baidu.location['y']
elementWidth = baidu.location['x'] + baidu.size['width']
elementHeight = baidu.location['y'] + baidu.size['height']
picture = Image.open('D:\\test2\\滑动验证\\yzm.jpg')
rgb_im = picture.convert('RGB')
rgb_im = rgb_im.crop((left, top, elementWidth, elementHeight))
rgb_im.save(r'D:\\test2\\滑动验证\\yzm2.jpg')


#url = 'http://www.cdgdc.edu.cn/cqva/gateway.html'
#headers = {
#        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
#        }
#
#response = requests.get(url,headers=headers)
#req = response.text
#dom_tree = etree.HTML(req)
#print(dom_tree.xpath('//*[@id="query_form"]/div[2]//text()'))
