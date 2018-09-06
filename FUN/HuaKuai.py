# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:22:52 2018

@author: Administrator
"""

#图像处理标准库
#from PIL import Image   
##web测试
#from selenium import webdriver
##鼠标操作
#from selenium.webdriver.common.action_chains import ActionChains
##等待时间 产生随机数 
#import time,random
#
#from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.action_chains import ActionChains
#import PIL.Image as image
#from PIL import Image,ImageEnhance
#import time,re, random
#import requests
#try:
#    from StringIO import StringIO
#except ImportError:
#    from io import StringIO
#
#
##打开页面至屏幕最大尺寸
#driver = webdriver.Chrome(executable_path='C:\ProgramData\Anaconda3\chromedriver.exe')
#driver.get('https://account.ch.com/NonRegistrations-Regist')
#driver.maximize_window()
##获取输入手机号码的表单
#input1 = driver.find_element_by_name('phoneNumberInput')
## 输入注册号码
#input1.send_keys('18380150750')
#time.sleep(2)
##获取打开滑块验证码页面的元素
#getcheck=driver.find_element_by_xpath('//*[@id="getDynamicPwd"]')
##点击进入滑块验证码页面//*[@id="getDynamicPwd"]
#getcheck.click()
#
#time.sleep(2)
## 获取拖拽的圆球
#slideblock = driver.find_element_by_class_name('geetest_slider_button')
## 鼠标点击圆球不松开
#ActionChains(driver).click_and_hold(slideblock).perform()
## 将圆球滑至相对起点位置的最右边
#ActionChains(driver).move_by_offset(xoffset=250, yoffset=0).perform()
#time.sleep(0.4)
## 保存包含滑块及缺口的页面截图
#driver.save_screenshot('D:\quekou.png')
## 放开圆球
#ActionChains(driver).release(slideblock).perform()
##打开保存至本地的缺口页面截图
#quekouimg=Image.open('d://quekou.png')
## 匹配本地对应原图
#sourceimg= match_source(quekouimg)
#def match_source(image):
#    imagea=Image.open('C:/Users/Administrator/Desktop/WorkSpider/1534839189(1).jpg')
#    imageb=Image.open('C:/Users/Administrator/Desktop/WorkSpider/1534839234(1).jpg')
#    imagec=Image.open('C:/Users/Administrator/Desktop/WorkSpider/1534839315(1).jpg')
#    imaged=Image.open('C:/Users/Administrator/Desktop/WorkSpider/1534839346(1).jpg')
#    imagee=Image.open('C:/Users/Administrator/Desktop/WorkSpider/1534839372(1).jpg')
#    list=[imagea,imageb,imagec,imaged,imagee]
#    #通过像素差遍历匹配本地原图
#    for i in list:
#       #本人电脑原图与缺口图对应滑块图片横坐标相同，纵坐标原图比缺口图大88px，可根据实际情况修改
#        pixel1=image.getpixel((868,340))
#        pixel2=i.getpixel((868,428))
#        #pixel[0]代表R值，pixel[1]代表G值，pixel[2]代表B值
#        if abs(pixel1[0]-pixel2[0])<5:
#           return i
#    return image
#
#
## 获取缺口位置
#visualstack=get_diff_location(sourceimg,quekouimg)
## 获取移动距离loc，827为滑块起点位置
#loc=visualstack-827
## 计算滑块位移距离
#def get_diff_location(image1,image2):
#    #（825,1082）（335,463）为滑块图片区域，可根据实际情况修改
#    for i in range(825,1082):
#        for j in range(335,463):
#            #遍历原图与缺口图像素值寻找缺口位置
#            if is_similar(image1,image2,i,j)==False:
#               return i
#    return -1
## 对比RGB值得到缺口位置
#def is_similar(image1,image2,x,y):
#    pixel1=image1.getpixel((x, y+88))
#    pixel2=image2.getpixel((x, y))
#    # 截图像素也许存在误差，50作为容差范围
#    if abs(pixel1[0]-pixel2[0])>=50 and abs(pixel1[1]-pixel2[1])>=50 and abs(pixel1[2]-pixel2[2])>=50:
#        return False
#    return True
#
##滑块移动轨迹
#def get_track(self,distance):
#    track=[]
#    current=0
#    mid=distance*3/4
#    t=random.randint(2,3)/10
#    v=0
#    while current<distance:
#          if current<mid:
#             a=2
#          else:
#             a=-3
#          v0=v
#          v=v0+a*t
#          move=v0*t+1/2*a*t*t
#          current+=move
#          track.append(round(move))
#    return track
## 生成拖拽移动轨迹，加3是为了模拟滑过缺口位置后返回缺口的情况
#track_list=get_track(loc+3)
#time.sleep(2)
#ActionChains(driver).click_and_hold(slideblock).perform()
#time.sleep(0.2)
## 根据轨迹拖拽圆球
#for track in track_list:
#    ActionChains(driver).move_by_offset(xoffset=track,yoffset=0).perform()
## 模拟人工滑动超过缺口位置返回至缺口的情况，数据来源于人工滑动轨迹，同时还加入了随机数，都是为了更贴近人工滑动轨迹
#imitate=ActionChains(driver).move_by_offset(xoffset=-1, yoffset=0)
#time.sleep(0.015)
#imitate.perform()
#time.sleep(random.randint(6,10)/10)
#imitate.perform()
#time.sleep(0.04)
#imitate.perform()
#time.sleep(0.012)
#imitate.perform()
#time.sleep(0.019)
#imitate.perform()
#time.sleep(0.033)
#ActionChains(driver).move_by_offset(xoffset=1, yoffset=0).perform()
## 放开圆球
#ActionChains(driver).pause(random.randint(6,14)/10).release(slideblock).perform()
#time.sleep(2)
##务必记得加入quit()或close()结束进程，不断测试电脑只会卡卡西
#driver.close()

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

#爬虫模拟的浏览器头部信息
agent = "Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0"
headers = {
        "User-Agent": agent
        }

# 根据位置对图片进行合并还原
# filename:图片
# location_list:图片位置
#内部两个图片处理函数的介绍
#crop函数带的参数为(起始点的横坐标，起始点的纵坐标，宽度，高度）
#paste函数的参数为(需要修改的图片，粘贴的起始点的横坐标，粘贴的起始点的纵坐标）
def get_merge_image(filename,location_list):
    #打开图片文件
    im = image.open(filename)
    #创建新的图片,大小为260*116
    new_im = image.new("RGB", (260,116))
    im_list_upper=[]
    im_list_down=[]
    # 拷贝图片
    for location in location_list:
        #上面的图片
        if location["y"]==-58:
            im_list_upper.append(im.crop((abs(location["x"]),58,abs(location["x"])+10,166)))
        #下面的图片
        if location["y"]==0:
            im_list_down.append(im.crop((abs(location["x"]),0,abs(location["x"])+10,58)))
    new_im = image.new("RGB", (260,116))
    x_offset = 0
    #黏贴图片
    for im in im_list_upper:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]
    x_offset = 0
    for im in im_list_down:
        new_im.paste(im, (x_offset,58))
        x_offset += im.size[0]
    return new_im

#对比RGB值
def is_similar(image1,image2,x,y):
    pass
    #获取指定位置的RGB值
    pixel1=image1.getpixel((x,y))
    pixel2=image2.getpixel((x,y))
    for i in range(0,3):
        # 如果相差超过50则就认为找到了缺口的位置
        if abs(pixel1[i]-pixel2[i])>=50:
            return False
    return True

#计算缺口的位置
def get_diff_location(image1,image2):
    i=0
    # 两张原始图的大小都是相同的260*116
    # 那就通过两个for循环依次对比每个像素点的RGB值
    # 如果相差超过50则就认为找到了缺口的位置
    for i in range(62,260):#有人可能看不懂这个位置为什么要从62开始看最后一张图（图：3）
        for j in range(0,116):
            if is_similar(image1,image2,i,j)==False:
                return  i

#根据缺口的位置模拟x轴移动的轨迹
def get_track(length):
    pass
    list=[]
    #间隔通过随机范围函数来获得,每次移动一步或者两步
    x=random.randint(1,3)
    #生成轨迹并保存到list内
    while length-x>=5:
        list.append(x)
        length=length-x
        x=random.randint(1,3)
    #最后五步都是一步步移动
    for i in range(length):
        list.append(1)
    return list

#滑动验证码破解程序
def main():
    driver = webdriver.Chrome(executable_path='C:\ProgramData\Anaconda3\chromedriver.exe')
    driver.get("https://account.geetest.com/register")
#    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys('1472278616@qq.com')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="captcha"]/div/div[3]/span[2]').click()
    time.sleep(20)

    driver.get_screenshot_as_file("D:\\test2\\滑动验证\\img.jpg")#对整个页面截图,注意！！！！！此处的路径不会自动创建，要先手动创建才能存入
    imgelement = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]')  # 定位验证码
    location = imgelement.location  # 获取验证码x,y轴坐标
    size = imgelement.size  # 获取验证码的长宽
    rangle = (int(location['x'] ), int(location['y']), int(location['x'] + size['width']),
              int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
    i = Image.open("D:\\test2\\滑动验证\\img.jpg")  # 打开截图
    i = i.convert('RGB')
    frame1 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    frame1.save('D:\\test2\\滑动验证\\new.jpg')
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[2]/div/a[2]').click()
    time.sleep(4)

    driver.get_screenshot_as_file("D:\\test2\\滑动验证\\img.jpg")
    imgelement = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/a/div[1]/div/canvas[2]')  # 定位验证码
    location = imgelement.location  # 获取验证码x,y轴坐标
    size = imgelement.size  # 获取验证码的长宽
    rangle = (int(location['x'] ), int(location['y']), int(location['x'] + size['width']),
              int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
    i = Image.open("D:\\test2\\滑动验证\\img.jpg")  # 打开截图
    i = i.convert('RGB')
    frame2 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    frame2.save('D:\\test2\\滑动验证\\new2.jpg')

    #计算缺口位置
    loc=get_diff_location(frame1, frame2)
    print('-------------')
    print(loc)
    #找到滑动的圆球
    element=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]')
    location=element.location
    #获得滑动圆球的高度
    y=location["y"]
    #鼠标点击元素并按住不放
    print ("第一步,点击元素")
    ActionChains(driver).click_and_hold(on_element=element).perform()

    time.sleep(0.15)

    print ("第二步，拖动元素")
    ActionChains(driver).move_to_element_with_offset(to_element=element, xoffset=loc + 30, yoffset=y - 445).perform()
    #释放鼠标
    ActionChains(driver).release(on_element=element).perform()

if __name__ == "__main__":
    pass
    main()

    #滑块移动轨迹
#def get_track(self,distance):
#    track=[]
#    current=0
#    mid=distance*3/4
#    t=random.randint(2,3)/10
#    v=0
#    while current<distance:
#          if current<mid:
#             a=2
#          else:
#             a=-3
#          v0=v
#          v=v0+a*t
#          move=v0*t+1/2*a*t*t
#          current+=move
#          track.append(round(move))
#    return track
## 生成拖拽移动轨迹，加3是为了模拟滑过缺口位置后返回缺口的情况
#track_list=get_track(loc+3)
#time.sleep(2)
#ActionChains(driver).click_and_hold(slideblock).perform()
#time.sleep(0.2)
## 根据轨迹拖拽圆球
#for track in track_list:
#    ActionChains(driver).move_by_offset(xoffset=track,yoffset=0).perform()
## 模拟人工滑动超过缺口位置返回至缺口的情况，数据来源于人工滑动轨迹，同时还加入了随机数，都是为了更贴近人工滑动轨迹
#imitate=ActionChains(driver).move_by_offset(xoffset=-1, yoffset=0)
#time.sleep(0.015)
#imitate.perform()
#time.sleep(random.randint(6,10)/10)
#imitate.perform()
#time.sleep(0.04)
#imitate.perform()
#time.sleep(0.012)
#imitate.perform()
#time.sleep(0.019)
#imitate.perform()
#time.sleep(0.033)
#ActionChains(driver).move_by_offset(xoffset=1, yoffset=0).perform()
## 放开圆球
#ActionChains(driver).pause(random.randint(6,14)/10).release(slideblock).perform()
#time.sleep(2)
#务必记得加入quit()或close()结束进程，不断测试电脑只会卡卡西
#driver.close()
#    关闭浏览器,为了演示方便,暂时注释掉.
#driver.quit()

#主函数入口



#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.common.action_chains import ActionChains
#import random
#import time
#import requests
#from io import BytesIO
#from PIL import Image
#import cv2
#import numpy as np
#
#
#cut_width = 91
#cut_height = 240
#back_width = 480
#back_height = 240
#
#class WangYi(object):
#    
#    def __init__(self):
#        self.browser = webdriver.Edge()
#        self.back_img = None
#        self.cut_img = None
#        self.scaling_ratio = 1.0
#        
#        
#    def visit(self, url):
#        self.browser.get(url)
#        WebDriverWait(self.browser, 10, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'big-heart')))
#        time.sleep(2)
#        self.browser.find_element_by_class_name("big-heart").click() 
#        
#    def get_image(self):
#        # 等待加载       
#        WebDriverWait(self.browser, 10, 0.5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'yidun_bgimg')))
#        back_url= self.browser.find_element_by_class_name("yidun_bg-img").get_attribute('src')
#        cut_url = self.browser.find_element_by_class_name("yidun_jigsaw").get_attribute('src')
#        # 从url获取图片并保存到本地
#        resq = requests.get(back_url)
#        file = BytesIO(resq.content)
#        back_img = Image.open(file)
#        back_img.save("back_img.jpg")
#        resq = requests.get(cut_url)
#        file = BytesIO(resq.content)
#        cut_img = Image.open(file)
#        cut_img.save("cut_img.png")
#        # opencv读取图片
#        self.back_img = cv2.imread("back_img.jpg")
#        self.cut_img = cv2.imread("cut_img.png")
#        self.scaling_ratio = self.browser.find_element_by_class_name("yidun_bg-img").size['width'] / back_width
#        return self.cut_img, self.back_img 
#        
#    def get_distance(self):
#        back_canny = get_back_canny(self.back_img)
#        operator = get_operator(self.cut_img)
#        pos_x, max_value = best_match(back_canny, operator)
#        distance = pos_x * self.scaling_ratio
#        return distance
#        
#    def auto_drag(self, distance):
#        element = self.browser.find_element_by_class_name("yidun_slider")
#        
#        # 这里就是根据移动进行调试，计算出来的位置不是百分百正确的，加上一点偏移
#        #distance -= element.size.get('width') / 2
#        distance += 13
#        has_gone_dist = 0
#        remaining_dist = distance
#        #distance += randint(-10, 10)
# 
#        # 按下鼠标左键
#        ActionChains(self.browser).click_and_hold(element).perform()
#        time.sleep(0.5)
#        while remaining_dist > 0:
#            ratio = remaining_dist / distance
#            if ratio < 0.2:
#                # 开始阶段移动较慢
#                span = random.randint(5, 8)
#            elif ratio > 0.8:
#                # 结束阶段移动较慢
#                span = random.randint(5, 8)
#            else:
#                # 中间部分移动快
#                span = random.randint(10, 16)
#            ActionChains(self.browser).move_by_offset(span, random.randint(-5, 5)).perform()
#            remaining_dist -= span
#            has_gone_dist += span
#            time.sleep(random.randint(5,20)/100)
#         
#        ActionChains(self.browser).move_by_offset(remaining_dist, random.randint(-5, 5)).perform()
#        ActionChains(self.browser).release(on_element=element).perform()
# 
#        
#        
#      
#def read_img_file(cut_dir, back_dir):
#    cut_image = cv2.imread(cut_dir)
#    back_image = cv2.imread(back_dir)
#    return cut_image, back_image
#
#def best_match(back_canny, operator):
#    max_value, pos_x = 0, 0
#    for x in range(cut_width, back_width - cut_width):
#        block = back_canny[:, x:x + cut_width]
#        value = (block * operator).sum()
#        if value > max_value:
#            max_value = value
#            pos_x = x
#    return pos_x, max_value
#        
#def get_back_canny(back_img):
#    img_blur = cv2.GaussianBlur(back_img, (3, 3), 0)
#    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
#    img_canny = cv2.Canny(img_gray, 100, 200)
#    return img_canny
#    
#def get_operator(cut_img):
#    
#    cut_gray = cv2.cvtColor(cut_img, cv2.COLOR_BGR2GRAY)
#
#    _, cut_binary = cv2.threshold(cut_gray, 127, 255, cv2.THRESH_BINARY)
#    # 获取边界
#    _, contours, hierarchy = cv2.findContours(cut_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#    # 获取最外层边界
#    contour = contours[-1]
#    # operator矩阵
#    operator = np.zeros((cut_height, cut_width))
#    # 根据 contour填写operator
#    for point in contour:
#        operator[point[0][1]][point[0][0]] = 1
#    return operator
#
#    
#    
#if __name__ == '__main__':
#    
#    page = WangYi()
#    page.visit('http://game.academy.163.com/minigame/2018/showcase/detail/143')
#    cut_image, back_image = page.get_image()
#    distance = page.get_distance()
#    page.auto_drag(distance)
#    
#    
#    
#    
#    
#    '''
#    browser = webdriver.Chrome()
#    browser.get('http://game.academy.163.com/minigame/2018/showcase/detail/125')
#    WebDriverWait(browser, 10, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'big-heart')))
#    time.sleep(0.25)
#    browser.find_element_by_class_name("big-heart").click()
#    
#    WebDriverWait(browser, 10, 0.5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'yidun_bgimg')))
#    
#    back_url= browser.find_element_by_class_name("yidun_bg-img").get_attribute('src')
#    cut_url = browser.find_element_by_class_name("yidun_jigsaw").get_attribute('src')
#    
#    resq = requests.get(back_url)
#    file = BytesIO(resq.content)
#    back_img = Image.open(file)
#    
#    resq = requests.get(cut_url)
#    file = BytesIO(resq.content)
#    cut_img = Image.open(file)
#    
#    
#    
#    element = browser.find_element_by_class_name("yidun_slider")
#    distance -= element.size.get('width') / 2
#    distance += 15
# 
#    # 按下鼠标左键
#    ActionChains(browser).click_and_hold(element).perform()
#    time.sleep(0.5)
#    while distance > 0:
#        if distance > 10:
#            # 如果距离大于10，就让他移动快一点
#            span = random.randint(5, 8)
#        else:
#            # 快到缺口了，就移动慢一点
#            span = random.randint(2, 3)
#        ActionChains(browser).move_by_offset(span, 0).perform()
#        distance -= span
#        time.sleep(random.randint(10,50)/100)
#     
#    ActionChains(browser).move_by_offset(distance, 1).perform()
#    ActionChains(browser).release(on_element=element).perform()'''