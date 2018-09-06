# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:08:01 2018

@author: Administrator
"""
from flask import request
from selenium import webdriver      
from selenium.webdriver.common.keys import Keys  
from time import sleep   #时间模块 
from selenium.webdriver.support.select import Select  
from selenium.webdriver.common.by import By   
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import re
from flask import Flask
from flask_json import FlaskJSON, JsonError, json_response, as_json
import json
#user = request.args.get('user')
#password = request.args.get('password')
#    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='C:\ProgramData\Anaconda3\chromedriver.exe')
user = '15228940634'
password = 'Aa12345'
chrome_options = Options()
chrome_options.add_argument('--proxy-server=http://+46.29.12.231:53281')
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='C:\ProgramData\Anaconda3\chromedriver.exe')
#driver = webdriver.Chrome(executable_path='C:\ProgramData\Anaconda3\chromedriver.exe')
url = 'http://www.ctrip.com/'
# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "ticket_2400000Z550L")))

driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="c_ph_login"]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="nloginname"]').send_keys(user)
driver.find_element_by_xpath('//*[@id="npwd"]').send_keys(password)
sleep(15)
a = driver.find_element_by_xpath('//*[@id="nerr"]').text
print(a,'我是a')
#        button = driver.find_element_by_xpath('//*[@id="sliderddnormal"]/div[1]/div[2]/div/i[1]')    # 找到“蓝色滑块”
#action = ActionChains(driver)            # 实例化一个action对象
#action.click_and_hold(button).perform()  # perform()用来执行ActionChains中存储的行为
#action.reset_actions()
#action.move_by_offset(180, 0).perform()  # 移动滑块
#WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="nsubmit"]')))
#
#driver.find_element_by_xpath('//*[@id="nsubmit"]').click()

#try:
#    dragger = driver.find_elements_by_class_name("cpt-drop-btn")[0]
#    action = ActionChains(driver)    
#    action.click_and_hold(dragger).perform()  #鼠标左键按下不放    
#    for index in range(200):
#        try:
#            action.move_by_offset(2, 0).perform() #平行移动鼠标
#        except:
#            break
#        action.reset_actions()
#        sleep(0.001)  #等待停顿时间
#    a = driver.find_element_by_xpath('//*[@id="nerr"]').text
#    print(a)
#    if a == '用户名或密码不正确，请重新输入！':
#        print(a)
#    
#except:
#    try:
#        print('要开始了')
#        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="c_ph_myhome"]')))
#        driver.find_element_by_xpath('//*[@id="c_ph_myhome"]').click()
#
#     
#        #driver.find_element_by_xpath('//*[@id="nsubmit"]').click()
#    #    time.sleep(2)
#        
#        xx = {}
#        All = []
#        temps = {}
#        print('要结束了')
#    #    sleep(5)
#        for i in range(1,50):
#            try:
#                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[5]/div[2]/ul/li[1]')))
#                imformation = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[5]/div[2]/ul/li[%s]'%i).text
#                pattern = re.compile('([\s\S]*?)¥')
#                place = re.findall(pattern,imformation)
#                place = place[0]
#                place = re.sub('\n','',place)
#                print(place)
#                temps['place'] = place
#                
#                pattern = re.compile('¥([\s\S]*?)\|')
#                price = re.findall(pattern,imformation)
#                price = price[0]
#                price = re.sub('\n','',price)
#                print(price)
#                temps['price'] = price 我是a
#                
#                pattern = re.compile('\|([\s\S]*?)\d')
#                state = re.findall(pattern,imformation)
#                state = state[0]
#                state = re.sub('\n','',state)
#                print(state)
#                temps['state'] = state
#                
#                pattern = re.compile('票([\s\S]*?至  [\s\S]*?)[A-Z]')
#                time = re.findall(pattern,imformation)
#                time = time[0]
#                time = re.sub('\n','',time)
#                temps['time'] = time
#                All.append(temps)
#                print(time)
#                print(imformation)
#                xx['All'] = All
#        
#            except:
#                pass
#        
#        
#        driver.find_element_by_xpath('//*[@id="c_ph_logout"]').click()
#        driver.close()
#
#    except:
#        pass
