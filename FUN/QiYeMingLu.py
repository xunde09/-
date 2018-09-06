# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 15:39:43 2018

@author: Administrator
"""

import requests
#import MySQLdb
import re
from bs4 import BeautifulSoup
from lxml import etree
import time
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
#with open('IPool.txt','wb') as f:
#    f.readline()
#print(f)    
#chrome_options.add_argument('--proxy-server=http://+f')
NameList = []
ProvinceList = ['ah','bj','cq','fj','gd','gs','gx','gz','hen','heb','han','hb','hun','jl','js','jx','lh','nmg','nx','qh','sc','sd','sh','snx','sx','tj','xj','xz','yn','zj']
url = 'tianyancha.com/search/oc'
#url = 'https://ah.tianyancha.com/search/ocD?rnd='
L = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']



for i in L:
    url1 = url+i
#    print(url1)
    for b in range(1,10000):
        url2 = url1 + '/p%s'%b
#        print(url2)
        for x in ProvinceList:
            url3 ='https://' + x + '.' + url2
#            req = requests.get(url3,headers=ua_headers)
            print(url3)
#            print(req.status_code)

            chrome_options.add_argument('--proxy-server=http://+118.190.95.43')
            driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='C:\ProgramData\Anaconda3\chromedriver.exe')
            driver.get(url3)
            driver.find_element_by_xpath('//*[@id="web-content"]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/input').send_keys('18615719364')
            driver.find_element_by_xpath('//*[@id="web-content"]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/input').send_keys('cy123456')
            driver.find_element_by_xpath('//*[@id="web-content"]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[5]').click()
#                driver.maximize_window
            time.sleep(3)
            for i in range(1,20):
                links = driver.find_element_by_xpath('//*[@id="web-content"]/div/div[1]/div/div[3]/div[%s]/div[2]/div[1]/a'%i).text
                print(links)                       
#            if req.status_code == 404 or req.status_code == 500:
#                print(req.status_code)
#                print(url3)
#                time.sleep(30)
#            else:  
#                Req = requests.get(url3,headers=ua_headers)
#                soup = BS(Req.text,'lxml')
#                Soup = (''.join('%s' %id for id in soup))
##                response = soup.get_text()
##                print(response)
##                for a in range(1,20):
##                    links = dom_tree.xpath('//*[@id="web-content"]/div/div[1]/div/div[3]/div[1]/div[2]/div[1]/a//text')
##                    print(links)
                pattern = re.compile('''tyc-event-ch="CompanySearch.Company" tyc-event-click="">([\s\S]*?)</a><div class="tag''')
                items = re.findall(pattern,links)
                items1 = ''.join(items)
                print(items1)
                with open('新企业名录.txt','a') as f:
                    f.write(links+',')
            driver.close()