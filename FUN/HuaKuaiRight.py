# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:26:10 2018

@author: Administrator
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.helloweba.com/demo/2017/unlock/")


dragger = driver.find_elements_by_class_name("slide-to-unlock-handle")[0]

action = ActionChains(driver)

action.click_and_hold(dragger).perform()  #鼠标左键按下不放

for index in range(200):
    try:
        action.move_by_offset(2, 0).perform() #平行移动鼠标
    except UnexpectedAlertPresentException:
        break
    action.reset_actions()
    sleep(0.001)  #等待停顿时间


# 打印警告框提示
success_text = driver.switch_to.alert.text
print(success_text)

sleep(5)

driver.quit()