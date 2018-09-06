# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:40:47 2018

@author: Administrator
"""
from flask_json import FlaskJSON, JsonError, json_response, as_json
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
#from lxml import etree
#import selenium.webdriver.support.ui as ui
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.by import By
from flask import Flask
from flask import request
import json



requests.packages.urllib3.disable_warnings(InsecureRequestWarning)#信任安全套接层
app = Flask(__name__)
FlaskJSON(app)
#@app.route('/search', methods=['POST', 'GET'])
#def search():
sfz = input('身份证')
name = input('姓名')
year = input('年份')
number = input('证号')

driver = webdriver.Chrome(executable_path='C:\ProgramData\Anaconda3\chromedriver.exe')
url = 'https://61.144.226.84/bank/CheckProperty.aspx'

driver.get(url)
driver.maximize_window()

time.sleep(5)
driver.find_element_by_xpath('//*[@id="imgBtnLogin"]').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="txtIdentityCardNo"]').send_keys('%s'%sfz)
driver.find_element_by_xpath('//*[@id="txtOwnerName"]').send_keys('%s'%name)
driver.find_element_by_xpath('//*[@id="btnGetRealty"]').click()
driver.switch_to.alert.accept()
time.sleep(5)

cqzlb = {}
cqzlb['xm'] = driver.find_element_by_xpath('//*[@id="gv1"]/tbody/tr[2]/td[1]').text
cqzlb['sfzh'] = driver.find_element_by_xpath('//*[@id="gv1"]/tbody/tr[2]/td[2]').text
cqzlb['yt'] = driver.find_element_by_xpath('//*[@id="gv1"]/tbody/tr[2]/td[3]').text
cqzlb['sl'] = driver.find_element_by_xpath('//*[@id="gv1"]/tbody/tr[2]/td[4]').text
print(cqzlb)

yshtrlb = {}
yshtrlb['xm'] = driver.find_element_by_xpath('//*[@id="gv2"]/tbody/tr[2]/td[1]').text
yshtrlb['sfzh'] = driver.find_element_by_xpath('//*[@id="gv2"]/tbody/tr[2]/td[2]').text
yshtrlb['hth'] = driver.find_element_by_xpath('//*[@id="gv2"]/tbody/tr[2]/td[3]').text
yshtrlb['sl'] = driver.find_element_by_xpath('//*[@id="gv2"]/tbody/tr[3]/td[3]').text
print(yshtrlb)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="frmInfo"]/table[2]/tbody/tr[1]/td/a[2]').click()


driver.find_element_by_xpath('//*[@id="chkCert_No_TypeList_1"]').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="txtNewCert_No_Year"]').send_keys('%s'%year)
driver.find_element_by_xpath('//*[@id="txtNewCert_No"]').send_keys('%s'%number)
driver.find_element_by_xpath('//*[@id="txtIdentityCardNo"]').send_keys('%s'%sfz)
driver.find_element_by_xpath('//*[@id="btnGetRealty"]').click()
driver.switch_to.alert.accept()
time.sleep(3)

cqzt = {}
zt = driver.find_element_by_xpath('//*[@id="divMessage"]/table/tbody/tr/td[3]/li[1]/span').text
cqzt['zt'] = zt 
print(cqzt['zt'])

xxzl = {}
zl =  driver.find_element_by_xpath('//*[@id="divMessage"]/table/tbody/tr/td[3]/li[2]').text
xxzl['zl'] = zl
print(xxzl['zl'])

    

#@as_json
@app.route('/search', methods=['POST', 'GET'])
def search():
    syxx = {}
    while True:    
        driver.find_element_by_xpath('//*[@id="frmInfo"]/table[2]/tbody/tr[1]/td/a[1]').click()
    
        a = request.args.get('lx')
        if a == 'bdc':
            sfz = request.args.get('sfz')
            name = request.args.get('name')
            year = request.args.get('year')
            number = request.args.get('number')
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="txtIdentityCardNo"]').send_keys('%s'%sfz)
            driver.find_element_by_xpath('//*[@id="txtOwnerName"]').send_keys('%s'%name)
            driver.find_element_by_xpath('//*[@id="btnGetRealty"]').click()
            driver.switch_to.alert.accept()
            time.sleep(5)
            
            
            cqzlb = {}
            cqzlb['xm'] = driver.find_element_by_xpath('//*[@id="gv1"]/tbody/tr[2]/td[1]').text
            cqzlb['sfzh'] = driver.find_element_by_xpath('//*[@id="gv1"]/tbody/tr[2]/td[2]').text
            cqzlb['yt'] = driver.find_element_by_xpath('//*[@id="gv1"]/tbody/tr[2]/td[3]').text
            cqzlb['sl'] = driver.find_element_by_xpath('//*[@id="gv1"]/tbody/tr[2]/td[4]').text
            print(cqzlb)
            syxx['cqzlb'] = cqzlb
            yshtrlb = {}
            yshtrlb['xm'] = driver.find_element_by_xpath('//*[@id="gv2"]/tbody/tr[2]/td[1]').text
            yshtrlb['sfzh'] = driver.find_element_by_xpath('//*[@id="gv2"]/tbody/tr[2]/td[2]').text
            yshtrlb['hth'] = driver.find_element_by_xpath('//*[@id="gv2"]/tbody/tr[2]/td[3]').text
            yshtrlb['sl'] = driver.find_element_by_xpath('//*[@id="gv2"]/tbody/tr[3]/td[3]').text
            print(yshtrlb)
            syxx['yshtrlb'] = yshtrlb
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="frmInfo"]/table[2]/tbody/tr[1]/td/a[2]').click()
            
            
            driver.find_element_by_xpath('//*[@id="chkCert_No_TypeList"]/label[2]').click()
            time.sleep(4)
            driver.find_element_by_xpath('//*[@id="txtNewCert_No_Year"]').send_keys('%s'%year)
            driver.find_element_by_xpath('//*[@id="txtNewCert_No"]').send_keys('%s'%number)
            driver.find_element_by_xpath('//*[@id="txtIdentityCardNo"]').send_keys('%s'%sfz)
            driver.find_element_by_xpath('//*[@id="btnGetRealty"]').click()
            driver.switch_to.alert.accept()
            time.sleep(3)
            
            cqzt = {}
            cqzt['zt'] = driver.find_element_by_xpath('//*[@id="divMessage"]/table/tbody/tr/td[3]/li[1]/span').text
            print(cqzt)
            syxx['cqzt'] = cqzt
            xxzl = {}
            xxzl['zl'] =  driver.find_element_by_xpath('//*[@id="divMessage"]/table/tbody/tr/td[3]/li[2]').text
            print(xxzl)
            syxx['xxzl'] = xxzl
            
            return json.dumps(syxx, skipkeys=True, ensure_ascii=False)
        elif a == 'cq':
            sfz = request.args.get('sfz')
            name = request.args.get('name')
            fczh = request.args.get('fczh')
    #            sfz = input('身份证')
    #            name = input('姓名')
    #            fczh = input('房产证号')
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="txtIdentityCardNo"]').send_keys('%s'%sfz)
            driver.find_element_by_xpath('//*[@id="txtOwnerName"]').send_keys('%s'%name)
            driver.find_element_by_xpath('//*[@id="btnGetRealty"]').click()
            driver.switch_to.alert.accept()
            time.sleep(3)
            
            cqzlb = {}
            cqzlb['xm'] = driver.find_element_by_xpath('//*[@id="gv1"]/tbody/tr[2]/td[1]').text
            cqzlb['sfzh'] = driver.find_element_by_xpath('//*[@id="gv1"]/tbody/tr[2]/td[2]').text
            cqzlb['yt'] = driver.find_element_by_xpath('//*[@id="gv1"]/tbody/tr[2]/td[3]').text
            cqzlb['sl'] = driver.find_element_by_xpath('//*[@id="gv1"]/tbody/tr[2]/td[4]').text
            print(cqzlb)
            syxx['cqzlb'] = cqzlb
            yshtrlb = {}
            yshtrlb['xm'] = driver.find_element_by_xpath('//*[@id="gv2"]/tbody/tr[2]/td[1]').text
            yshtrlb['sfzh'] = driver.find_element_by_xpath('//*[@id="gv2"]/tbody/tr[2]/td[2]').text
            yshtrlb['hth'] = driver.find_element_by_xpath('//*[@id="gv2"]/tbody/tr[2]/td[3]').text
            yshtrlb['sl'] = driver.find_element_by_xpath('//*[@id="gv2"]/tbody/tr[3]/td[3]').text
            print(yshtrlb)
            syxx['yshtrlb'] = yshtrlb
            
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="frmInfo"]/table[2]/tbody/tr[1]/td/a[2]').click()
            
            
            driver.find_element_by_xpath('//*[@id="chkCert_No_TypeList"]/label[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="txtCertificateNo"]').send_keys('%s'%fczh)
            driver.find_element_by_xpath('//*[@id="txtIdentityCardNo"]').send_keys('%s'%sfz)
            driver.find_element_by_xpath('//*[@id="btnGetRealty"]').click()
            driver.switch_to.alert.accept()
            time.sleep(3)
            
            cqzt = {}
            cqzt['zt'] = driver.find_element_by_xpath('//*[@id="divMessage"]/table/tbody/tr/td[3]/li[1]/span').text
            print(cqzt)
            syxx['cqzt'] = cqzt
            
            xxzl = {}
            xxzl['zl'] =  driver.find_element_by_xpath('//*[@id="divMessage"]/table/tbody/tr/td[3]/li[2]').text
            print(xxzl) 
            syxx['xxzl'] = xxzl
            return json.dumps(syxx, skipkeys=True, ensure_ascii=False)

if __name__ == '__main__':
    app.run(host='192.168.2.47', port=13457)