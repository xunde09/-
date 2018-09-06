# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:57:18 2018

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
import random
from queue import Queue

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面

app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
#@as_json
def s():
#    sleep(60)
    user = request.args.get('user')
    password = request.args.get('password')
    q = Queue(maxsize=10)
    lst = []
    q.put(user)
    print('开始睡觉')
#    sleep(120)
    print('开始取出')
    q.get(user)
    print('我卡在这了')

    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='C:\ProgramData\Anaconda3\chromedriver.exe')
#    driver = webdriver.Chrome(executable_path='C:\ProgramData\Anaconda3\chromedriver.exe')
    url = 'https://passport.ctrip.com/user/login'
    # WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "ticket_2400000Z550L")))
    
    driver.get(url)
    driver.maximize_window()
#    driver.find_element_by_xpath('//*[@id="c_ph_login"]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="nloginname"]').send_keys(user)
    driver.find_element_by_xpath('//*[@id="npwd"]').send_keys(password)
    
   
    try:
        dragger = driver.find_elements_by_class_name("cpt-drop-btn")[0]
        action = ActionChains(driver)    
        action.click_and_hold(dragger).perform()  #鼠标左键按下不放    
        for index in range(200):
            try:
                action.move_by_offset(2, 0).perform() #平行移动鼠标
            except:
                break
            action.reset_actions()
            sleep(0.001)  #等待停顿时间
        
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="nsubmit"]')))
        driver.find_element_by_xpath('//*[@id="nsubmit"]').click()
        print('要开始了')
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="c_ph_myhome"]')))
        driver.find_element_by_xpath('//*[@id="c_ph_myhome"]').click()

     
        #driver.find_element_by_xpath('//*[@id="nsubmit"]').click()
    #    time.sleep(2)
        
        xx = {}
        All = []
        temps = {}
        print('要结束了')
    #    sleep(5)
        for i in range(1,50):
            try:
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[5]/div[2]/ul/li[1]')))
                imformation = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[5]/div[2]/ul/li[%s]'%i).text
                pattern = re.compile('([\s\S]*?)¥')
                place = re.findall(pattern,imformation)
                place = place[0]
                place = re.sub('\n','',place)
                print(place)
                temps['place'] = place
                
                pattern = re.compile('¥([\s\S]*?)\|')
                price = re.findall(pattern,imformation)
                price = price[0]
                price = re.sub('\n','',price)
                print(price)
                temps['price'] = price
                
                pattern = re.compile('\|([\s\S]*?)\d')
                state = re.findall(pattern,imformation)
                state = state[0]
                state = re.sub('\n','',state)
                print(state)
                temps['state'] = state
                
                pattern = re.compile('票([\s\S]*?至  [\s\S]*?)[A-Z]')
                time = re.findall(pattern,imformation)
                time = time[0]
                time = re.sub('\n','',time)
                temps['time'] = time
                All.append(temps)
                print(time)
                print(imformation)
                xx['All'] = All
        
            except:
                pass
        
        
        driver.find_element_by_xpath('//*[@id="c_ph_logout"]').click()
        driver.close()
        return json.dumps(xx,skipkeys=True, ensure_ascii=False)
    except:
        try:
            print('要开始了')
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="c_ph_myhome"]')))
            driver.find_element_by_xpath('//*[@id="c_ph_myhome"]').click()
            
         
            #driver.find_element_by_xpath('//*[@id="nsubmit"]').click()
        #    time.sleep(2)
            
            xx = {}
            All = []
            temps = {}
            print('要结束了')
        #    sleep(5)
            for i in range(1,50):
                try:
                    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[5]/div[2]/ul/li[1]')))
                    imformation = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[5]/div[2]/ul/li[%s]'%i).text
                    pattern = re.compile('([\s\S]*?)¥')
                    place = re.findall(pattern,imformation)
                    place = place[0]
                    place = re.sub('\n','',place)
                    print(place)
                    temps['place'] = place
                    
                    pattern = re.compile('¥([\s\S]*?)\|')
                    price = re.findall(pattern,imformation)
                    price = price[0]
                    price = re.sub('\n','',price)
                    print(price)
                    temps['price'] = price
                    
                    pattern = re.compile('\|([\s\S]*?)\d')
                    state = re.findall(pattern,imformation)
                    state = state[0]
                    state = re.sub('\n','',state)
                    print(state)
                    temps['state'] = state
                    
                    pattern = re.compile('票([\s\S]*?至  [\s\S]*?)[A-Z]')
                    time = re.findall(pattern,imformation)
                    time = time[0]
                    time = re.sub('\n','',time)
                    temps['time'] = time
                    All.append(temps)
                    print(time)
                    print(imformation)
                    xx['All'] = All
            
                except:
                    pass
            
            
            driver.find_element_by_xpath('//*[@id="c_ph_logout"]').click()
            driver.close()
        #        sleep(60)
            return json.dumps(xx,skipkeys=True, ensure_ascii=False)
#            sleep(120)
        except:
            try:
                a = driver.find_element_by_xpath('//*[@id="nerr"]').text
                print(a)
                driver.close()
                if a == '用户名或密码不正确，请重新输入！':
                    return '您的用户名和密码输入错误请重新输入'
                else:
                    return '您的操作太频繁请5分钟后再试'
            except:
                driver.close()
                return '您的操作太频繁请5分钟后再试'
    
    
#        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="nsubmit"]')))
#    
#        driver.find_element_by_xpath('//*[@id="nsubmit"]').click()
#
#
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
#                temps['price'] = price
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
##        sleep(60)
#        return json.dumps(xx,skipkeys=True, ensure_ascii=False)
#    except:
#        try:
#            dragger = driver.find_elements_by_class_name("cpt-drop-btn")[0]
#            action = ActionChains(driver)    
#            action.click_and_hold(dragger).perform()  #鼠标左键按下不放    
#            for index in range(200):
#                try:
#                    action.move_by_offset(2, 0).perform() #平行移动鼠标
#                except:
#                    break
#                action.reset_actions()
#                sleep(0.001)  #等待停顿时间
#            print('要开始了')
#            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="c_ph_myhome"]')))
#            driver.find_element_by_xpath('//*[@id="c_ph_myhome"]').click()
    
         
            #driver.find_element_by_xpath('//*[@id="nsubmit"]').click()
        #    time.sleep(2)
            
#            xx = {}
#            All = []
#            temps = {}
#            print('要结束了')
#        #    sleep(5)
#            for i in range(1,50):
#                try:
#                    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[5]/div[2]/ul/li[1]')))
#                    imformation = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[5]/div[2]/ul/li[%s]'%i).text
#                    pattern = re.compile('([\s\S]*?)¥')
#                    place = re.findall(pattern,imformation)
#                    place = place[0]
#                    place = re.sub('\n','',place)
#                    print(place)
#                    temps['place'] = place
#                    
#                    pattern = re.compile('¥([\s\S]*?)\|')
#                    price = re.findall(pattern,imformation)
#                    price = price[0]
#                    price = re.sub('\n','',price)
#                    print(price)
#                    temps['price'] = price
#                    
#                    pattern = re.compile('\|([\s\S]*?)\d')
#                    state = re.findall(pattern,imformation)
#                    state = state[0]
#                    state = re.sub('\n','',state)
#                    print(state)
#                    temps['state'] = state
#                    
#                    pattern = re.compile('票([\s\S]*?至  [\s\S]*?)[A-Z]')
#                    time = re.findall(pattern,imformation)
#                    time = time[0]
#                    time = re.sub('\n','',time)
#                    temps['time'] = time
#                    All.append(temps)
#                    print(time)
#                    print(imformation)
#                    xx['All'] = All
#            
#                except:
#                    pass
#            
#            
#            driver.find_element_by_xpath('//*[@id="c_ph_logout"]').click()
#            driver.close()
#            return json.dumps(xx,skipkeys=True, ensure_ascii=False)
#        except:
##            sleep(120)
#            a = driver.find_element_by_xpath('//*[@id="nerr"]/i').text
#            if a == '用户名或密码不正确，请重新输入！':
#                return '您的用户名和密码输入错误请重新输入'
#            else:
#                return '您的操作过于频繁请稍后再试'





#    except:
#        try:
#            print('要开始了')
#            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="c_ph_myhome"]')))
#            driver.find_element_by_xpath('//*[@id="c_ph_myhome"]').click()
#    
#         
#            #driver.find_element_by_xpath('//*[@id="nsubmit"]').click()
#        #    time.sleep(2)
#            
#            xx = {}
#            All = []
#            temps = {}
#            print('要结束了')
#        #    sleep(5)
#            for i in range(1,50):
#                try:
#                    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[5]/div[2]/ul/li[1]')))
#                    imformation = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[5]/div[2]/ul/li[%s]'%i).text
#                    pattern = re.compile('([\s\S]*?)¥')
#                    place = re.findall(pattern,imformation)
#                    place = place[0]
#                    place = re.sub('\n','',place)
#                    print(place)
#                    temps['place'] = place
#                    
#                    pattern = re.compile('¥([\s\S]*?)\|')
#                    price = re.findall(pattern,imformation)
#                    price = price[0]
#                    price = re.sub('\n','',price)
#                    print(price)
#                    temps['price'] = price
#                    
#                    pattern = re.compile('\|([\s\S]*?)\d')
#                    state = re.findall(pattern,imformation)
#                    state = state[0]
#                    state = re.sub('\n','',state)
#                    print(state)
#                    temps['state'] = state
#                    
#                    pattern = re.compile('票([\s\S]*?至  [\s\S]*?)[A-Z]')
#                    time = re.findall(pattern,imformation)
#                    time = time[0]
#                    time = re.sub('\n','',time)
#                    temps['time'] = time
#                    All.append(temps)
#                    print(time)
#                    print(imformation)
#                    xx['All'] = All
#            
#                except:
#                    pass
#            
#            
#            driver.find_element_by_xpath('//*[@id="c_ph_logout"]').click()
#            driver.close()
#            return json.dumps(xx,skipkeys=True, ensure_ascii=False)
#        except:
#            return '您的操作太频繁请稍等5分钟再试'

    
    
    
if __name__ == '__main__':
    app.run('192.168.2.47',port=14725)
    

















