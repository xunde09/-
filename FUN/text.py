# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:12:03 2018

@author: Administrator
"""

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
#chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
#chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
chrome_options.add_argument('--proxy-server=http://+220.248.125.82:8118')

url = 'http://www.xicidaili.com/nn/'
#proxies={'https':'http://220.248.125.82:8118'}
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
#req = requests.get(url,headers=headers,proxies=proxies)
#print(req.text)

driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='C:\ProgramData\Anaconda3\chromedriver.exe')
print(driver.page_source)