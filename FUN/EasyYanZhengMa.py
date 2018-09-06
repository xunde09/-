# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 17:26:24 2018

@author: Administrator
"""

from PIL import Image
from pytesseract import *
from fnmatch import fnmatch
from queue import Queue
import matplotlib.pyplot as plt
import cv2
import time
import os




def clear_border(img,img_name):
  '''去除边框
  '''

  filename = './out_img/' + img_name.split('.')[0] + '-clearBorder.jpg'
  h, w = img.shape[:2]
  for y in range(0, w):
    for x in range(0, h):
      # if y ==0 or y == w -1 or y == w - 2:
      if y < 4 or y > w -4:
        img[x, y] = 255
      # if x == 0 or x == h - 1 or x == h - 2:
      if x < 4 or x > h - 4:
        img[x, y] = 255

  cv2.imwrite(filename,img)
  return img


def interference_line(img, img_name):
  '''
  干扰线降噪  '''

  filename =  './out_img/' + img_name.split('.')[0] + '-interferenceline.jpg'
  h, w = img.shape[:2]
  # ！！！opencv矩阵点是反的
   # img[1,2] 1:图片的高度，2：图片的宽度
  for y in range(1, w - 1):
     for x in range(1, h - 1):
       count = 0
       if img[x, y - 1] > 245:
         count = count + 1
       if img[x, y + 1] > 245:
         count = count + 1
       if img[x - 1, y] > 245:
         count = count + 1
       if img[x + 1, y] > 245:
         count = count + 1
       if count > 2:
         img[x, y] = 255
  cv2.imwrite(filename,img)
  return img
 
def interference_point(img,img_name, x = 0, y = 0):
     """点降噪
     9邻域框,以当前点为中心的田字框,黑点个数
     :param x:
     :param y:
     :return:
     """
     filename =  './out_img/' + img_name.split('.')[0] + '-interferencePoint.jpg'
     # todo 判断图片的长宽度下限
     cur_pixel = img[x,y]# 当前像素点的值
     height,width = img.shape[:2]
 
     for y in range(0, width - 1):
       for x in range(0, height - 1):
         if y == 0:  # 第一行
             if x == 0:  # 左上顶点,4邻域
                 # 中心点旁边3个点
                 sum = int(cur_pixel) \
                       + int(img[x, y + 1]) \
                       + int(img[x + 1, y]) \
                       + int(img[x + 1, y + 1])
                 if sum <= 2 * 245:
                   img[x, y] = 0
             elif x == height - 1:  # 右上顶点
                 sum = int(cur_pixel) \
                       + int(img[x, y + 1]) \
                       + int(img[x - 1, y]) \
                       + int(img[x - 1, y + 1])
                 if sum <= 2 * 245:
                   img[x, y] = 0
             else:  # 最上非顶点,6邻域
                 sum = int(img[x - 1, y]) \
                       + int(img[x - 1, y + 1]) \
                       + int(cur_pixel) \
                       + int(img[x, y + 1]) \
                       + int(img[x + 1, y]) \
                       + int(img[x + 1, y + 1])
                 if sum <= 3 * 245:
                   img[x, y] = 0
         elif y == width - 1:  # 最下面一行
             if x == 0:  # 左下顶点
                 # 中心点旁边3个点
                 sum = int(cur_pixel) \
                       + int(img[x + 1, y]) \
                       + int(img[x + 1, y - 1]) \
                       + int(img[x, y - 1])
                 if sum <= 2 * 245:
                   img[x, y] = 0
             elif x == height - 1:  # 右下顶点
                 sum = int(cur_pixel) \
                       + int(img[x, y - 1]) \
                       + int(img[x - 1, y]) \
                       + int(img[x - 1, y - 1])
 
                 if sum <= 2 * 245:
                   img[x, y] = 0
             else:  # 最下非顶点,6邻域
                 sum = int(cur_pixel) \
                       + int(img[x - 1, y]) \
                       + int(img[x + 1, y]) \
                       + int(img[x, y - 1]) \
                       + int(img[x - 1, y - 1]) \
                       + int(img[x + 1, y - 1])
                 if sum <= 3 * 245:
                   img[x, y] = 0
         else:  # y不在边界
             if x == 0:  # 左边非顶点
                 sum = int(img[x, y - 1]) \
                       + int(cur_pixel) \
                       + int(img[x, y + 1]) \
                       + int(img[x + 1, y - 1]) \
                       + int(img[x + 1, y]) \
                       + int(img[x + 1, y + 1])
 
                 if sum <= 3 * 245:
                   img[x, y] = 0
             elif x == height - 1:  # 右边非顶点
                 sum = int(img[x, y - 1]) \
                       + int(cur_pixel) \
                       + int(img[x, y + 1]) \
                       + int(img[x - 1, y - 1]) \
                       + int(img[x - 1, y]) \
                       + int(img[x - 1, y + 1])
 
                 if sum <= 3 * 245:
                   img[x, y] = 0
             else:  # 具备9领域条件的1                 sum = int(img[x - 1, y - 1]) \
                       + int(img[x - 1, y]) \
                       + int(img[x - 1, y + 1]) \
                       + int(img[x, y - 1]) \
                       + int(cur_pixel) \
                       + int(img[x, y + 1]) \
                       + int(img[x + 1, y - 1]) \
                       + int(img[x + 1, y]) \
                       + int(img[x + 1, y + 1])
                 if sum <= 4 * 245:
                   img[x, y] = 0
     cv2.imwrite(filename,img)
     return img
 
 def _get_dynamic_binary_image(filedir, img_name):
   '''
   自适应阀值二值化
162   '''
163 
164   filename =   './out_img/' + img_name.split('.')[0] + '-binary.jpg'
165   img_name = filedir + '/' + img_name
166   print('.....' + img_name)
167   im = cv2.imread(img_name)
168   im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
169 
170   th1 = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
171   cv2.imwrite(filename,th1)
172   return th1
173 
174 def _get_static_binary_image(img, threshold = 140):
175   '''
176   手动二值化
177   '''
178 
179   img = Image.open(img)
180   img = img.convert('L')
181   pixdata = img.load()
182   w, h = img.size
183   for y in range(h):
184     for x in range(w):
185       if pixdata[x, y] < threshold:
186         pixdata[x, y] = 0
187       else:
188         pixdata[x, y] = 255
189 
190   return img
191 
192 
193 def cfs(im,x_fd,y_fd):
194   '''用队列和集合记录遍历过的像素坐标代替单纯递归以解决cfs访问过深问题
195   '''
196 
197   # print('**********')
198 
199   xaxis=[]
200   yaxis=[]
201   visited =set()
202   q = Queue()
203   q.put((x_fd, y_fd))
204   visited.add((x_fd, y_fd))
205   offsets=[(1, 0), (0, 1), (-1, 0), (0, -1)]#四邻域
206 
207   while not q.empty():
208       x,y=q.get()
209 
210       for xoffset,yoffset in offsets:
211           x_neighbor,y_neighbor = x+xoffset,y+yoffset
212 
213           if (x_neighbor,y_neighbor) in (visited):
214               continue  # 已经访问过了
215 
216           visited.add((x_neighbor, y_neighbor))
217 
218           try:
219               if im[x_neighbor, y_neighbor] == 0:
220                   xaxis.append(x_neighbor)
221                   yaxis.append(y_neighbor)
222                   q.put((x_neighbor,y_neighbor))
223 
224           except IndexError:
225               pass
226   # print(xaxis)
227   if (len(xaxis) == 0 | len(yaxis) == 0):
228     xmax = x_fd + 1
229     xmin = x_fd
230     ymax = y_fd + 1
231     ymin = y_fd
232 
233   else:
234     xmax = max(xaxis)
235     xmin = min(xaxis)
236     ymax = max(yaxis)
237     ymin = min(yaxis)
238     #ymin,ymax=sort(yaxis)
239 
240   return ymax,ymin,xmax,xmin
241 
242 def detectFgPix(im,xmax):
243   '''搜索区块起点
244   '''
245 
246   h,w = im.shape[:2]
247   for y_fd in range(xmax+1,w):
248       for x_fd in range(h):
249           if im[x_fd,y_fd] == 0:
250               return x_fd,y_fd
251 
252 def CFS(im):
253   '''切割字符位置
254   '''
255 
256   zoneL=[]#各区块长度L列表
257   zoneWB=[]#各区块的X轴[起始，终点]列表
258   zoneHB=[]#各区块的Y轴[起始，终点]列表
259 
260   xmax=0#上一区块结束黑点横坐标,这里是初始化
261   for i in range(10):
262 
263       try:
264           x_fd,y_fd = detectFgPix(im,xmax)
           # print(y_fd,x_fd)
           xmax,xmin,ymax,ymin=cfs(im,x_fd,y_fd)
           L = xmax - xmin
           H = ymax - ymin
           zoneL.append(L)
           zoneWB.append([xmin,xmax])
           zoneHB.append([ymin,ymax])
 
       except TypeError:
           return zoneL,zoneWB,zoneHB
 
   return zoneL,zoneWB,zoneHB
 
 
 def cutting_img(im,im_position,img,xoffset = 1,yoffset = 1):
   filename =  './out_img/' + img.split('.')[0]
   # 识别出的字符个数
   im_number = len(im_position[1])
   # 切割字符
   for i in range(im_number):
     im_start_X = im_position[1][i][0] - xoffset
     im_end_X = im_position[1][i][1] + xoffset
     im_start_Y = im_position[2][i][0] - yoffset
     im_end_Y = im_position[2][i][1] + yoffset
     cropped = im[im_start_Y:im_end_Y, im_start_X:im_end_X]
     cv2.imwrite(filename + '-cutting-' + str(i) + '.jpg',cropped)
 
 
 
 def main():
   filedir = './easy_img'
 
   for file in os.listdir(filedir):
     if fnmatch(file, '*.jpeg'):
       img_name = file
 
       # 自适应阈值二值化
       im = _get_dynamic_binary_image(filedir, img_name)
 
       # 去除边框
       im = clear_border(im,img_name)
 
       # 对图片进行干扰线降噪
       im = interference_line(im,img_name)
 
       # 对图片进行点降噪
       im = interference_point(im,img_name)
 
       # 切割的位置
       im_position = CFS(im)
 
       maxL = max(im_position[0])
       minL = min(im_position[0])
 
       # 如果有粘连字符，如果一个字符的长度过长就认为是粘连字符，并从中间进行切割
       if(maxL > minL + minL * 0.7):
         maxL_index = im_position[0].index(maxL)
         minL_index = im_position[0].index(minL)
         # 设置字符的宽度
         im_position[0][maxL_index] = maxL // 2
         im_position[0].insert(maxL_index + 1, maxL // 2)
         # 设置字符X轴[起始，终点]位置
         im_position[1][maxL_index][1] = im_position[1][maxL_index][0] + maxL // 2
         im_position[1].insert(maxL_index + 1, [im_position[1][maxL_index][1] + 1, im_position[1][maxL_index][1] + 1 + maxL // 2])
         # 设置字符的Y轴[起始，终点]位置
         im_position[2].insert(maxL_index + 1, im_position[2][maxL_index])
 
       # 切割字符，要想切得好就得配置参数，通常 1 or 2 就可以
       cutting_img(im,im_position,img_name,1,1)
 
       # 识别验证码
       cutting_img_num = 0
       for file in os.listdir('./out_img'):
         str_img = ''
         if fnmatch(file, '%s-cutting-*.jpg' % img_name.split('.')[0]):
           cutting_img_num += 1
       for i in range(cutting_img_num):
         try:
           file = './out_img/%s-cutting-%s.jpg' % (img_name.split('.')[0], i)
           # 识别验证码
           str_img = str_img + image_to_string(Image.open(file),lang = 'eng', config='-psm 10') #单个字符是10，一行文本是7
         except Exception as err:
           pass
       print('切图：%s' % cutting_img_num)
       print('识别为：%s' % str_img)
 
if __name__ == '__main__':
   main()