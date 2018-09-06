from flask import Flask
from flask import request
from flask_json import FlaskJSON, JsonError, json_response, as_json
import random
import json
import time
import re 
import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from http import cookiejar
from lxml import etree
import signal
import errno
from time import sleep 
import socket
import sys
import time
import socket
from http import cookiejar
import socket



app = Flask(__name__)
FlaskJSON(app)
CK = ['TYCID=0e1b9a307f3e11e88e51ff713ccdd166; undefined=0e1b9a307f3e11e88e51ff713ccdd166; ssuid=8709034186; jsid=SEM-NEW360-PP-SY-000009; _ga=GA1.2.1019756149.1531444101; tyc-user-info=%257B%2522isExpired%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNTcxOTM2NCIsImlhdCI6MTUzMjA3MTQ5OSwiZXhwIjoxNTQ3NjIzNDk5fQ.cQtS0VT6tvC9rBM80YZVgPZn4TwEOGqftHoRLUwFCbiY7x_e9A4Oh2_KeW78hjIBR2XIWfs6mQIZdGvAQXtrwg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25225%2522%252C%2522surday%2522%253A%2522166%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%252220%2522%252C%2522onum%2522%253A%252219%2522%252C%2522mobile%2522%253A%252218615719364%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNTcxOTM2NCIsImlhdCI6MTUzMjA3MTQ5OSwiZXhwIjoxNTQ3NjIzNDk5fQ.cQtS0VT6tvC9rBM80YZVgPZn4TwEOGqftHoRLUwFCbiY7x_e9A4Oh2_KeW78hjIBR2XIWfs6mQIZdGvAQXtrwg; aliyungf_tc=AQAAAFF3824PewwAmwW5bgIvb/yiAUFI; csrfToken=Z54xVSyXcUKmfmhER3ROhbc1; _gid=GA1.2.1438444975.1532307892; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1531961837,1531987579,1532307892,1532307916; RTYCID=01d543f5dd764fb5bcaefc2343dd3a8c; bannerFlag=true; _gat_gtag_UA_122238368_3=1; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1532316457',
      'TYCID=0e1b9a307f3e11e88e51ff713ccdd166; undefined=0e1b9a307f3e11e88e51ff713ccdd166; ssuid=8709034186; jsid=SEM-NEW360-PP-SY-000009; _ga=GA1.2.1019756149.1531444101; tyc-user-info=%257B%2522isExpired%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNTcxOTM2NCIsImlhdCI6MTUzMjA3MTQ5OSwiZXhwIjoxNTQ3NjIzNDk5fQ.cQtS0VT6tvC9rBM80YZVgPZn4TwEOGqftHoRLUwFCbiY7x_e9A4Oh2_KeW78hjIBR2XIWfs6mQIZdGvAQXtrwg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25225%2522%252C%2522surday%2522%253A%2522166%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%252220%2522%252C%2522onum%2522%253A%252219%2522%252C%2522mobile%2522%253A%252218615719364%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNTcxOTM2NCIsImlhdCI6MTUzMjA3MTQ5OSwiZXhwIjoxNTQ3NjIzNDk5fQ.cQtS0VT6tvC9rBM80YZVgPZn4TwEOGqftHoRLUwFCbiY7x_e9A4Oh2_KeW78hjIBR2XIWfs6mQIZdGvAQXtrwg; aliyungf_tc=AQAAAFF3824PewwAmwW5bgIvb/yiAUFI; csrfToken=Z54xVSyXcUKmfmhER3ROhbc1; _gid=GA1.2.1438444975.1532307892; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1531961837,1531987579,1532307892,1532307916; RTYCID=01d543f5dd764fb5bcaefc2343dd3a8c; bannerFlag=true; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1532316465',
      'TYCID=0e1b9a307f3e11e88e51ff713ccdd166; undefined=0e1b9a307f3e11e88e51ff713ccdd166; ssuid=8709034186; jsid=SEM-NEW360-PP-SY-000009; _ga=GA1.2.1019756149.1531444101; tyc-user-info=%257B%2522isExpired%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNTcxOTM2NCIsImlhdCI6MTUzMjA3MTQ5OSwiZXhwIjoxNTQ3NjIzNDk5fQ.cQtS0VT6tvC9rBM80YZVgPZn4TwEOGqftHoRLUwFCbiY7x_e9A4Oh2_KeW78hjIBR2XIWfs6mQIZdGvAQXtrwg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25225%2522%252C%2522surday%2522%253A%2522166%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%252220%2522%252C%2522onum%2522%253A%252219%2522%252C%2522mobile%2522%253A%252218615719364%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNTcxOTM2NCIsImlhdCI6MTUzMjA3MTQ5OSwiZXhwIjoxNTQ3NjIzNDk5fQ.cQtS0VT6tvC9rBM80YZVgPZn4TwEOGqftHoRLUwFCbiY7x_e9A4Oh2_KeW78hjIBR2XIWfs6mQIZdGvAQXtrwg; aliyungf_tc=AQAAAFF3824PewwAmwW5bgIvb/yiAUFI; csrfToken=Z54xVSyXcUKmfmhER3ROhbc1; _gid=GA1.2.1438444975.1532307892; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1531961837,1531987579,1532307892,1532307916; RTYCID=01d543f5dd764fb5bcaefc2343dd3a8c; bannerFlag=true; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1532316495',
      'TYCID=0e1b9a307f3e11e88e51ff713ccdd166; undefined=0e1b9a307f3e11e88e51ff713ccdd166; ssuid=8709034186; jsid=SEM-NEW360-PP-SY-000009; _ga=GA1.2.1019756149.1531444101; tyc-user-info=%257B%2522isExpired%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNTcxOTM2NCIsImlhdCI6MTUzMjA3MTQ5OSwiZXhwIjoxNTQ3NjIzNDk5fQ.cQtS0VT6tvC9rBM80YZVgPZn4TwEOGqftHoRLUwFCbiY7x_e9A4Oh2_KeW78hjIBR2XIWfs6mQIZdGvAQXtrwg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25225%2522%252C%2522surday%2522%253A%2522166%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%252220%2522%252C%2522onum%2522%253A%252219%2522%252C%2522mobile%2522%253A%252218615719364%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNTcxOTM2NCIsImlhdCI6MTUzMjA3MTQ5OSwiZXhwIjoxNTQ3NjIzNDk5fQ.cQtS0VT6tvC9rBM80YZVgPZn4TwEOGqftHoRLUwFCbiY7x_e9A4Oh2_KeW78hjIBR2XIWfs6mQIZdGvAQXtrwg; aliyungf_tc=AQAAAFF3824PewwAmwW5bgIvb/yiAUFI; csrfToken=Z54xVSyXcUKmfmhER3ROhbc1; _gid=GA1.2.1438444975.1532307892; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1531961837,1531987579,1532307892,1532307916; RTYCID=01d543f5dd764fb5bcaefc2343dd3a8c; bannerFlag=true; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1532316546',
      'TYCID=0e1b9a307f3e11e88e51ff713ccdd166; undefined=0e1b9a307f3e11e88e51ff713ccdd166; ssuid=8709034186; jsid=SEM-NEW360-PP-SY-000009; _ga=GA1.2.1019756149.1531444101; tyc-user-info=%257B%2522isExpired%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNTcxOTM2NCIsImlhdCI6MTUzMjA3MTQ5OSwiZXhwIjoxNTQ3NjIzNDk5fQ.cQtS0VT6tvC9rBM80YZVgPZn4TwEOGqftHoRLUwFCbiY7x_e9A4Oh2_KeW78hjIBR2XIWfs6mQIZdGvAQXtrwg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25225%2522%252C%2522surday%2522%253A%2522166%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%252220%2522%252C%2522onum%2522%253A%252219%2522%252C%2522mobile%2522%253A%252218615719364%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNTcxOTM2NCIsImlhdCI6MTUzMjA3MTQ5OSwiZXhwIjoxNTQ3NjIzNDk5fQ.cQtS0VT6tvC9rBM80YZVgPZn4TwEOGqftHoRLUwFCbiY7x_e9A4Oh2_KeW78hjIBR2XIWfs6mQIZdGvAQXtrwg; aliyungf_tc=AQAAAFF3824PewwAmwW5bgIvb/yiAUFI; csrfToken=Z54xVSyXcUKmfmhER3ROhbc1; _gid=GA1.2.1438444975.1532307892; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1531961837,1531987579,1532307892,1532307916; RTYCID=01d543f5dd764fb5bcaefc2343dd3a8c; bannerFlag=true; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1532316597',]

@app.route('/search', methods=['POST', 'GET'])
@as_json
def search():

    name = request.args.get('name')
    print("输入的公司名字为：%s" % name)
    # 去抓取name对应公司的数据
    url = 'https://www.tianyancha.com/search?key=%s'%name
    ua_headers = {"Cookie":'TYCID=0e1b9a307f3e11e88e51ff713ccdd166; undefined=0e1b9a307f3e11e88e51ff713ccdd166; ssuid=8709034186; _ga=GA1.2.1019756149.1531444101; jsid=SEM-SOUGOU-PP-SY-000001; aliyungf_tc=AQAAAAUA2kJHGAMA4bGWtpmiSwoH96ck; csrfToken=biY7DU-0vxHL9urzPaXu82tE; _gid=GA1.2.1460895880.1532932958; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1532670055,1532680324,1532684172,1532932958; tyc-user-info=%257B%2522isExpired%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNTcxOTM2NCIsImlhdCI6MTUzMjkzMjk3NywiZXhwIjoxNTQ4NDg0OTc3fQ.KjfEr16KNJd9WFQ2wugWPiWhiAj2RwTrxwkK0up8W1l13KhoAVd-wt2qMyr3bYAWZtw4YqWDM7WLqM4MkAqdUA%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25225%2522%252C%2522surday%2522%253A%2522156%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%252220%2522%252C%2522onum%2522%253A%252220%2522%252C%2522mobile%2522%253A%252218615719364%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNTcxOTM2NCIsImlhdCI6MTUzMjkzMjk3NywiZXhwIjoxNTQ4NDg0OTc3fQ.KjfEr16KNJd9WFQ2wugWPiWhiAj2RwTrxwkK0up8W1l13KhoAVd-wt2qMyr3bYAWZtw4YqWDM7WLqM4MkAqdUA; RTYCID=cc29a976964141058e3f8ca32b644182; bannerFlag=true; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1532933312',
                  "User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0",
                  "Connection":"keep-alive",
                  "Host":"www.tianyancha.com"    
            }
    
    
    #proxy_dict = {'111.155.116.234':'8123','187.190.221.71':'3128','62.80.190.57':'41258','194.146.230.9':'41258'}
    #
    #proxy_dict = {
    #    'http': proxy_url
    #}
    #response = requests.post(url,data=Postdata,headers=headers,proxies = proxy_dict,timeout = 10)
    
    
    req2 = requests.get(url,headers=ua_headers)
    req3 = (req2.text)
    #print('req3',req3)
    pattern = re.compile('href="(https://www.tianyancha.com/company/([\s\S]*?))"')
    #req4 = bytes(req3,encoding='utf-8')
    #print(re.search(pattern,req3))
    AA = re.search(pattern,req3)
    #print(AA)
    pattern1 = re.compile('"https://www.tianyancha.com/company/([\s\S]*?)"')
    BB = re.findall(pattern1,AA.group(0))
    CC = (''.join(BB))

    url2 = 'https://www.tianyancha.com/company/'+CC
    print(url2)
    req = requests.get(url2,headers=ua_headers)
    
    soup = BS(req.text,'lxml')
    response = soup.get_text()
    #print(response)
    
    req1 = bytes(response,encoding='utf-8')
    pattern = re.compile('网址[\s\S]*?我想联系这家企业')
    items = re.findall(pattern, response)
    #print(items)
    response1 = req.text
    dom_tree = etree.HTML(response1)
    
    GongShangBeiJing = {}
    
    gsxx = {}
    
    dom_tree
    gsxx['mz'] = dom_tree.xpath('//*[@id="company_web_top"]/div[2]/div[2]/div[1]/h1//text()')[0]
    
    gsxx['dh'] = dom_tree.xpath('//*[@id="company_web_top"]/div[2]/div[2]/div[5]/div[1]/div[1]/span[2]//text()')[0]
    
    gsxx['yx'] = dom_tree.xpath('//*[@id="company_web_top"]/div[2]/div[2]/div[5]/div[1]/div[2]/span[2]//text()')[0]
    
    gsxx['wz'] = dom_tree.xpath('//*[@id="company_web_top"]/div[2]/div[2]/div[5]/div[2]/div[1]/a/@href')
    if gsxx['wz']:
        gsxx['wz'] = gsxx['wz'][0]
    else:
        gsxx['wz'] = '-'
    
    
    gsxx['dz'] = dom_tree.xpath('//*[@id="company_web_top"]/div[2]/div[2]/div[5]/div[2]/div[2]/span[2]/@title')
    
    if not gsxx['dz']:
        gsxx['dz'] = dom_tree.xpath('//*[@id="company_web_top"]/div[2]/div[2]/div[5]/div[2]/div[2]/text()')
        if gsxx['dz']:
            gsxx['dz'] = gsxx['dz'][0]
        else:
            gsxx['dz'] = '-'
    else:
        gsxx['dz'] = dom_tree.xpath('//*[@id="company_web_top"]/div[2]/div[2]/div[5]/div[2]/div[2]/span[2]/@title')[0]
    
    gsxx['fddbr'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[1]/tbody/tr[1]/td[1]/div/div[1]/div[2]/div[1]//text()')
    if gsxx['fddbr']:
        gsxx['fddbr'] = gsxx['fddbr'][0]
    
    gsxx['fddbrgs'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[1]/tbody/tr[1]/td[1]/div/div[1]/div[2]/div[2]/span//text()')
    
    print(gsxx['fddbrgs'])
    gsxx['zczb'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[1]/tbody/tr[1]/td[2]/div[2]//text()')[0]  #注册资本
    itemss4 =  ''.join(gsxx['zczb'])
    a = ['0',"1", "2",'3','4','5','6','7','8','9']
    b = ["5","2", "0",'7','1','3','8','6','9','4']
    dic = dict(zip(a,b))
    pattern1 = re.compile('(' + '|'.join(a) + ')')
    itemsss4 = pattern1.sub(lambda a:dic[a.group()], itemss4)
    NB1 = re.sub('万团民币','万人民币',itemsss4)
    NB2 = (''.join('%s' %id for id in NB1))
    #itemss4 = (''.join('%s' %id for id in NB20))
    gsxx['zczb'] = NB2
    print(gsxx['zczb'])
                
    gsxx['zcsj'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[1]/tbody/tr[2]/td/div[2]//text()')[0]  #注册时间
    items5 =  ''.join(gsxx['zcsj'])
    a = ['0',"1", "2",'3','4','5','6','7','8','9']
    b = ["5","2", "0",'7','1','3','8','6','9','4']
    dic = dict(zip(a,b))
    pattern2 = re.compile('(' + '|'.join(a) + ')')
    itemss5 = pattern2.sub(lambda a:dic[a.group()], items5)
    NB3 = re.sub('万团民币','万人民币',itemss5)
    NB4 = (''.join('%s' %id for id in NB3))
    #itemss4 = (''.join('%s' %id for id in NB20))
    gsxx['zcsj'] = NB4
    print(gsxx['zcsj'])
    
    gsxx['gszt'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[1]/tbody/tr[3]/td/div[2]//text()')[0]  #公司状态
    
    gsxx['gszch'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[1]/td[2]//text()')[0]  #工商注册号
    
    gsxx['zzjgdm'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[1]/td[4]//text()')[0]  #组织机构代码
    
    gsxx['tyxydm'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[2]/td[2]//text()')[0]  #统一信用代码
    
    gsxx['gslx'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[2]/td[4]//text()')[0]#公司类型
    
    gsxx['nsrsbh'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[3]/td[2]//text()')[0]  #纳税人识别号
    
    gsxx['hy'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[3]/td[4]//text()')[0]   #行业
    
    gsxx['yyqx'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[4]/td[2]/span//text()')[0]  #营业期限
    
    gsxx['hzrq'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[4]/td[4]/text//text()')[0]  #核准日期
    items6 =  ''.join(gsxx['hzrq'])
    a = ['0',"1", "2",'3','4','5','6','7','8','9']
    b = ["5","2", "0",'7','1','3','8','6','9','4']
    dic = dict(zip(a,b))
    pattern3 = re.compile('(' + '|'.join(a) + ')')
    itemss6 = pattern3.sub(lambda a:dic[a.group()], items6)
    NB5 = re.sub('万团民币','万人民币',itemss6)
    NB6 = (''.join('%s' %id for id in NB5))
    #itemss4 = (''.join('%s' %id for id in NB20))
    gsxx['hzrq'] = NB6
    print(gsxx['hzrq'])
    
    gsxx['nsrzz'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[5]/td[2]//text()')[0]  #纳税人资质
    
    gsxx['rygm'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[5]/td[4]//text()')[0]  #人员规模
    
    gsxx['sjzb'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[6]/td[2]//text()')[0]  #实缴资本
    
    gsxx['djjg'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[6]/td[4]//text()')[0]   #登记机关
    
    gsxx['cbrs'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[7]/td[2]//text()')[0]   #参保人数
    
    gsxx['ywmc'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[7]/td[4]//text()')[0]   #英文名称
    
    gsxx['zcdz'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[8]/td[2]//text()')[0]   #注册地址
    
    gsxx['jyfw'] = dom_tree.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[9]/td[2]/span/span/span[1]//text()')[0] #经营范围
    
    gsxx['tyfxzsts'] = dom_tree.xpath('//*[@id="web-content"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[1]/div[1]//text()')  #天眼风险
    print(gsxx['tyfxzsts'],'天眼风险自身提示')
    if gsxx['tyfxzsts']:
        gsxx['tyfxzsts'] = gsxx['tyfxzsts'][1]
    else:
        gsxx['tyfxzsts'] = '-'
    
    gsxx['tyfxzbts'] = dom_tree.xpath('//*[@id="web-content"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[2]/div[1]//text()')
    if gsxx['tyfxzbts']:                  
        gsxx['tyfxzbts'] = gsxx['tyfxzbts'][1]
    else:
        gsxx['tyfxzbts'] = '-'
        
    
    gsxx['tyfxyjts'] = dom_tree.xpath('//*[@id="web-content"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[3]/div[1]//text()')
    if gsxx['tyfxyjts']:
        gsxx['tyfxyjts'] = gsxx['tyfxyjts'][1]
    else:
        gsxx['tyfxyjts'] = '-'
    
    
    gsxx['tyfxzsxx'] = dom_tree.xpath('//*[@id="web-content"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[1]/span//text()')
    if gsxx['tyfxzsxx']:
        gsxx['tyfxzsxx'] = gsxx['tyfxzsxx'][0]
    elif not gsxx['tyfxzsxx']:
        gsxx['tyfxzsxx'] = dom_tree.xpath('//*[@id="web-content"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[1]/div[2]//text()')
        gsxx['tyfxzsxx'] = ''.join(gsxx['tyfxzsxx'])    
    
    gsxx['tyfxzbxx'] = dom_tree.xpath('//*[@id="web-content"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[2]/span//text()')
    if gsxx['tyfxzbxx']:
        gsxx['tyfxzbxx'] = gsxx['tyfxzbxx'][0]
    elif not gsxx['tyfxzbxx']:
        gsxx['tyfxzbxx'] = dom_tree.xpath('//*[@id="web-content"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[2]/div[2]//text()')
        gsxx['tyfxzbxx'] = ''.join(gsxx['tyfxzbxx']) 

    gsxx['tyfxyjxx'] = dom_tree.xpath('//*[@id="web-content"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[3]/span//text()')
    if gsxx['tyfxyjxx']:
        gsxx['tyfxyjxx'] = gsxx['tyfxyjxx'][0]
    elif not gsxx['tyfxyjxx']:
        gsxx['tyfxyjxx'] = dom_tree.xpath('//*[@id="web-content"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[3]/div[2]//text()')
        gsxx['tyfxyjxx'] = ''.join(gsxx['tyfxyjxx']) 
    
    GongShangBeiJing['gsxx'] = gsxx
    
    zyryxx = []     #主要人员
    for i in range(1,20):
        temp = {};
        temp['xh'] = i
        temp['zyrymz'] = dom_tree.xpath('//*[@id="_container_staff"]/div/table/tbody/tr[%s]/td[2]/div/a[1]//text()'%i)
        if not temp['zyrymz']:
            break
        temp['zyrymz'] = temp['zyrymz'][0]
        temp['zyrygx'] = dom_tree.xpath('//*[@id="_container_staff"]/div/table/tbody/tr[%s]/td[2]/div/a[2]//text()'%i)
        if temp['zyrygx']:
            temp['zyrygx'] = temp['zyrygx'][0]
        elif not temp['zyrygx']:
            temp['zyrygx'] = '-'
        temp['zyryzw'] = dom_tree.xpath('//*[@id="_container_staff"]/div/table/tbody/tr[%s]/td[3]//text()'%i)
        if not temp['zyryzw']:
            temp['zyryzw'] = '-'
        else:
            temp['zyryzw'] = ''.join(temp['zyryzw'])
        zyryxx.append(temp)
    GongShangBeiJing['zyryxx'] = zyryxx
    
    gdxx = []
    for i in range(1,20):  #股东信息
        temp = {};
        temp['xh'] = i
        temp['gdmz'] = dom_tree.xpath('//*[@id="_container_holder"]/table/tbody/tr[%s]/td[2]/div/div[2]/a//text()'%i)
        if not temp['gdmz']:           
            break
        temp['gdmz'] = temp['gdmz'][0]
        temp['gdgs'] = dom_tree.xpath('//*[@id="_container_holder"]/table/tbody/tr[%s]/td[2]/div/div[3]/span/a//text()'%i)
        if temp['gdgs']:
            temp['gdgs'] = temp['gdgs'][0]
        elif not temp['gdgs']:
            temp['gdgs'] = '-'
        temp['czbl'] = dom_tree.xpath('//*[@id="_container_holder"]/table/tbody/tr[%s]/td[3]/div/div/span//text()'%i)
        if temp['czbl']:
            temp['czbl'] = temp['czbl'][0]
        elif not temp['czbl']:
            temp['czbl'] = '-'
        temp['rjcz'] = dom_tree.xpath('//*[@id="_container_holder"]/table/tbody/tr[%s]/td[4]/div/span//text()'%i)
        if temp['rjcz']:
            temp['rjcz'] = temp['rjcz'][0]
        elif not temp['rjcz']:
            temp['rjcz'] = '-'
        temp['czsj'] = dom_tree.xpath('//*[@id="_container_holder"]/table/tbody/tr[%s]/td[5]/div/span//text()'%i)
        if not temp['czsj']:
            temp['czsj'] = '-'
        else:
            temp['czsj'] = temp['czsj'][0]
        gdxx.append(temp)
    GongShangBeiJing['gdxx'] = gdxx
    
    
    dwtz = []
    for i in range(1,20):   #对外投资
        temp = {};
        temp['xh'] = i
        temp['btzgsmc'] = dom_tree.xpath('//*[@id="_container_invest"]/table/tbody/tr[%s]/td[2]//text()'%i)
        print(temp['btzgsmc'])
        if not temp['btzgsmc']:
            break
        temp['btzgsmc'] = temp['btzgsmc'][0]
        temp['btzfddbr'] = dom_tree.xpath('//*[@id="_container_invest"]/table/tbody/tr[%s]/td[3]//text()'%i)
        if temp['btzfddbr']:
            temp['btzfddbr'] = temp['btzfddbr'][0]
        elif not temp['btzfddbr']:
            temp['btzfddbr'] = '-'
        temp['btzgsgs'] = dom_tree.xpath('//*[@id="_container_invest"]/table/tbody/tr[%s]/td[3]/span/span/a//text()'%i)
        if temp['btzgsgs']:
            temp['btzgsgs'] = temp['btzgsgs'][0]
        else:
            temp['btzgsgs'] = '-'
        temp['dwtzzczz'] = dom_tree.xpath('//*[@id="_container_invest"]/table/tbody/tr[%s]/td[4]/span//text()'%i)
        if temp['dwtzzczz']:
            temp['dwtzzczz'] = temp['dwtzzczz'][0]
        elif not temp['dwtzzczz']:
            temp['dwtzzczz'] = '-'
        temp['dwtzzb'] = dom_tree.xpath('//*[@id="_container_invest"]/table/tbody/tr[%s]/td[5]/span//text()'%i)
        if temp['dwtzzb']:
            temp['dwtzzb'] = temp['dwtzzb'][0]
        elif not temp['dwtzzb']:
            temp['dwtzzb'] = '-'
        temp['dwtzzcsj'] = dom_tree.xpath('//*[@id="_container_invest"]/table/tbody/tr[%s]/td[6]/span//text()'%i)
        if temp['dwtzzcsj']:
            temp['dwtzzcsj'] = temp['dwtzzcsj'][0]
        elif not temp['dwtzzcsj']:
            temp['dwtzzcsj'] = '-'
        temp['dwtzzt'] = dom_tree.xpath('//*[@id="_container_invest"]/table/tbody/tr[%s]/td[7]/span//text()'%i)
        if not temp['dwtzzt']:
            temp['dwtzzt'] = '-'
        else:
            temp['dwtzzt'] = temp['dwtzzt'][0]
        dwtz.append(temp)
    GongShangBeiJing['dwtz'] = dwtz
        
    
    zzsyr = []
    for i in range(1,20):  #最终受益人
        temp = {};
        temp['xh'] = i
        temp['zzsyrmc'] = dom_tree.xpath('//*[@id="_container_humanholding"]/table/tbody/tr[%s]/td[2]//text()'%i)
        if not temp['zzsyrmc']:             
            break
        temp['zzsyrmc'] = temp['zzsyrmc'][0]
        temp['zzsyrgs'] = dom_tree.xpath('//*[@id="_container_humanholding"]/table/tbody/tr[%s]/td[2]/span/span/a//text()'%i)
        if temp['zzsyrgs']:
            temp['zzsyrgs'] = temp['zzsyrgs'][0]
        elif not temp['zzsyrgs']:
            temp['zzsyrgs'] = '-'
        temp['cgbl'] = dom_tree.xpath('//*[@id="_container_humanholding"]/table/tbody/tr[%s]/td[3]/span//text()'%i)
        if temp['cgbl']:
            temp['cgbl'] = temp['cgbl'][0]
        elif not temp['cgbl']:
            temp['cgbl'] = '-'
        temp['gqllj'] = dom_tree.xpath('//*[@id="_container_humanholding"]/table/tbody/tr[%s]/td[4]/div/div[1]/b//text()'%i)
        if temp['gqllj']:
            temp['gqllj'] = temp['gqllj'][0]
        elif not temp['gqllj']:
            temp['gqllj'] = '-'
        temp['gqlmz'] = dom_tree.xpath('//*[@id="_container_humanholding"]/table/tbody/tr[%s]/td[4]/div/span[1]/a//text()'%i)
        if temp['gqlmz']:
            temp['gqlmz'] = temp['gqlmz'][0]
        elif not temp['gqlmz']:
            temp['gqlmz'] = '-'
        temp['gqlgs'] = dom_tree.xpath('//*[@id="_container_humanholding"]/table/tbody/tr[%s]/td[4]/div/span[2]/a//text()'%i)
        if temp['gqlgs']:
            temp['gqlgs'] = temp['gqlgs'][0]
        elif not temp['gqlgs']:
            temp['gqlgs'] = '-'
        zzsyr.append(temp)
    GongShangBeiJing['zzsyr'] = zzsyr

    sjkzq = []
    for i in range(1,20):   #实际控制权
        temp = {};
        temp['xh'] = i
        temp['kgqymc'] = dom_tree.xpath('//*[@id="_container_companyholding"]/table/tbody/tr[%s]/td[2]/span/a//text()'%i)
        if not temp['kgqymc']:             
            break
        temp['kgqymc'] = temp['kgqymc'][0]
        temp['tzbl'] = dom_tree.xpath('//*[@id="_container_companyholding"]/table/tbody/tr[%s]/td[3]/span//text()'%i)
        if temp['tzbl']:
            temp['tzbl'] = temp['tzbl'][0]
        elif not temp['tzbl']:
            temp['tzbl'] = '-'
        temp['gqllj'] = dom_tree.xpath('//*[@id="_container_companyholding"]/table/tbody/tr[%s]/td[4]/div/div[1]/b//text()'%i)
        if temp['gqllj']:
            temp['gqllj'] = temp['gqllj'][0]
        elif not temp['gqllj']:
            temp['gqllj'] = '-'
        temp['gqlgs1'] = dom_tree.xpath('//*[@id="_container_companyholding"]/table/tbody/tr[%s]/td[4]/div/span[1]/a//text()'%i)
        if temp['gqlgs1']:
            temp['gqlgs1'] = temp['gqlgs1'][0]
        elif not temp['gqlgs1']:
            temp['gqlgs1'] = '-'
        temp['gqlgs2'] = dom_tree.xpath('//*[@id="_container_companyholding"]/table/tbody/tr[%s]/td[4]/div/span[2]/a//text()'%i)
        if temp['gqlgs2']:
            temp['gqlgs2'] = temp['gqlgs2'][0]
        elif not temp['gqlgs2']:
            temp['gqlgs2'] = '-'
        sjkzq.append(temp)
    GongShangBeiJing['sjkzq'] = sjkzq
        
    
    bgjl = []
    for i in range(1,100):    #变更记录
        temp = {};
        temp['xh'] = i
        temp['bgsj'] = dom_tree.xpath('//*[@id="_container_changeinfo"]/table/tbody/tr[%s]/td[2]//text()'%i)
        if not temp['bgsj']:
           break
        temp['bgsj'] = temp['bgsj'][0]
        temp['bgxm'] = dom_tree.xpath('//*[@id="_container_changeinfo"]/table/tbody/tr[%s]/td[3]//text()'%i)
        if temp['bgxm']:
            temp['bgxm'] = temp['bgxm'][0]
        elif not temp['bgxm']:
            temp['bgxm'] = '-'
        temp['bgq'] = dom_tree.xpath('//*[@id="_container_changeinfo"]/table/tbody/tr[%s]/td[4]//text()'%i)
        if temp['bgq']:
            temp['bgq'] = temp['bgq'][0]
        elif not temp['bgq']:
            temp['bgq'] = '-'
        temp['bgh'] = dom_tree.xpath('//*[@id="_container_changeinfo"]/table/tbody/tr[%s]/td[5]//text()'%i)
        if temp['bgh']:
            temp['bgh'] = temp['bgh'][0]
        elif not temp['bgh']:
            temp['bgh'] = '-'
        bgjl.append(temp)
    GongShangBeiJing['bgjl'] = bgjl

    fzjg = []
    for i in range(1,100):   #分支机构
       temp = {};
       temp['xh'] = i

       temp['qymc'] = dom_tree.xpath('//*[@id="_container_branch"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['qymc']:
           break
       temp['qymc'] = temp['qymc'][1]
       temp['fzr'] = dom_tree.xpath('//*[@id="_container_branch"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['fzr']:
            temp['fzr'] = temp['fzr'][0]
       elif not temp['fzr']:
            temp['fzr'] = '-'
       temp['fzjg_zcsj'] = dom_tree.xpath('//*[@id="_container_branch"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['fzjg_zcsj']:
            temp['fzjg_zcsj'] = temp['fzjg_zcsj'][0]
       elif not temp['fzjg_zcsj']:
            temp['fzjg_zcsj'] = '-'
       temp['fzjg_zt'] = dom_tree.xpath('//*[@id="_container_branch"]/table/tbody/tr[%s]/td[5]//text()'%i)
       if temp['fzjg_zt']:
            temp['fzjg_zt'] = temp['fzjg_zt'][0]
       elif not temp['fzjg_zt']:
            temp['fzjg_zt'] = '-'
       fzjg.append(temp)
    GongShangBeiJing['fzjg'] = fzjg
    
    ktgg = []
    for i in range(1,20):  #开庭公告
       temp = {};
       temp['xh'] = i
       temp['ktrq'] = dom_tree.xpath('//*[@id="_container_announcementcourt"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['ktrq']:
           break
       temp['ktrq'] = temp['ktrq'][0]

       temp['ktgg_ay'] = dom_tree.xpath('//*[@id="_container_announcementcourt"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['ktgg_ay']:
            temp['ktgg_ay'] = temp['ktgg_ay'][0]
       elif not temp['ktgg_ay']:
            temp['ktgg_ay'] = '-'
       temp['yg_ssr'] = dom_tree.xpath('//*[@id="_container_announcementcourt"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['yg_ssr']:
            temp['yg_ssr'] = temp['yg_ssr'][0]
       elif not temp['yg_ssr']:
            temp['yg_ssr'] = '-'
       temp['bg_bssr'] = dom_tree.xpath('//*[@id="_container_announcementcourt"]/table/tbody/tr[%s]/td[5]//text()'%i)
       if temp['bg_bssr']:
            temp['bg_bssr'] = temp['bg_bssr'][0]
       elif not temp['bg_bssr']:
            temp['bg_bssr'] = '-'
       ktgg.append(temp)
    GongShangBeiJing['ktgg'] = ktgg 
       
       
    flss = []
    for i in range(1,20):       #法律诉讼
        temp = {};
        temp['xh'] = i
        temp['rq'] = dom_tree.xpath('//*[@id="_container_lawsuit"]/table/tbody/tr[%s]/td[2]//text()'%i)
        if not temp['rq']:
            break
        temp['rq'] = temp['rq'][0]

        temp['cpws'] = dom_tree.xpath('//*[@id="_container_lawsuit"]/table/tbody/tr[%s]/td[3]//text()'%i)
        if temp['cpws']:
            temp['cpws'] = temp['cpws'][0]
        temp['flss_ay'] = dom_tree.xpath('//*[@id="_container_lawsuit"]/table/tbody/tr[%s]/td[4]/span//text()'%i)
        if temp['flss_ay']:
            temp['flss_ay'] = temp['flss_ay'][0]
        elif not temp['flss_ay']:
            temp['flss_ay'] = '-'
        temp['ajsf'] = dom_tree.xpath('//*[@id="_container_lawsuit"]/table/tbody/tr[%s]/td[5]//text()'%i)
        if temp['ajsf']:
            temp['ajsf'] = temp['ajsf'][0]
        elif not temp['ajsf']:
            temp['ajsf'] = '-'
        temp['flah'] = dom_tree.xpath('//*[@id="_container_lawsuit"]/table/tbody/tr[%s]/td[6]//text()'%i)
        if temp['flah']:
            temp['flah'] = temp['flah'][0]
        elif not temp['flah']:
            temp['flah'] = '-'
        flss.append(temp)
    GongShangBeiJing['flss'] = flss
    
        
    fygg = []
    for i in range(1,20):  #法院公告
       temp = {};
       temp['xh'] = i
       temp['ggsj'] = dom_tree.xpath('//*[@id="_container_court"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['ggsj']:
           break
       temp['ggsj'] = temp['ggsj'][0]

       temp['ssf'] = dom_tree.xpath('//*[@id="_container_court"]/table/tbody/tr[%s]/td[3]/span/a//text()'%i)
       if temp['ssf']:
            temp['ssf'] = temp['ssf'][0]
       elif not temp['ssf']:
            temp['ssf'] = '-'
       temp['bsf'] = dom_tree.xpath('//*[@id="_container_court"]/table/tbody/tr[%s]/td[4]/span//text()'%i)
       if temp['bsf']:
            temp['bsf'] = temp['bsf'][0]
       elif not temp['bsf']:
            temp['bsf'] = '-'
       temp['gglx'] = dom_tree.xpath('//*[@id="_container_court"]/table/tbody/tr[%s]/td[5]/span//text()'%i)
       if temp['gglx']:
            temp['gglx'] = temp['gglx'][0]
       elif not temp['gglx']:
            temp['gglx'] = '-'
       temp['fy'] = dom_tree.xpath('//*[@id="_container_court"]/table/tbody/tr[%s]/td[6]/span//text()'%i)
       if temp['fy']:
            temp['fy'] = temp['fy'][0]
       elif not temp['fy']:
            temp['fy'] = '-'
       fygg.append(temp)
    GongShangBeiJing['fygg'] = fygg
       
    ssrxx = []
    for i in range(1,20):       #失信人信息
        temp = {};
        temp['xh'] = i
        temp['larq'] = dom_tree.xpath('//*[@id="_container_dishonest"]/table/tbody/tr[%s]/td[2]/span//text()'%i)
        if not temp['larq']:
            break
        temp['larq'] = temp['larq'][0]
        temp['sxrah'] = dom_tree.xpath('//*[@id="_container_dishonest"]/table/tbody/tr[%s]/td[3]//text()'%i)
        if temp['sxrah']:
            temp['sxrah'] = temp['sxrah'][0]
        elif not temp['sxrah']:
            temp['sxrah'] = '-'
        temp['zxfy'] = dom_tree.xpath('//*[@id="_container_dishonest"]/table/tbody/tr[%s]/td[4]//text()'%i)
        if temp['zxfy']:
            temp['zxfy'] = temp['zxfy'][0]
        elif not temp['zxfy']:
            temp['zxfy'] = '-'
        temp['lxzt']  = dom_tree.xpath('//*[@id="_container_dishonest"]/table/tbody/tr[%s]/td[5]//text()'%i)
        if temp['lxzt']:
            temp['lxzt'] = temp['lxzt'][0]
        elif not temp['lxzt']:
            temp['lxzt'] = '-'
        temp['zxyjwh'] = dom_tree.xpath('//*[@id="_container_dishonest"]/table/tbody/tr[%s]/td[6]//text()'%i)
        if temp['zxyjwh']:
            temp['zxyjwh'] = temp['zxyjwh'][0]
        elif not temp['zxyjwh']:
            temp['zxyjwh'] = '-'
        ssrxx.append(temp)
    GongShangBeiJing['ssrxx'] = ssrxx
        
    bzxr = []
    for i in range(1,20):       #被执行人
        temp = {};
        temp['xh'] = i
        temp['larq'] = dom_tree.xpath('//*[@id="_container_zhixing"]/table/tbody/tr[%s]/td[2]'%i)
        if not temp['larq']:
            break
        temp['larq'] = temp['larq'][0]
        temp['zxbd'] = dom_tree.xpath('//*[@id="_container_zhixing"]/table/tbody/tr[s%]/td[2]//text()'%i)
        if temp['zxbd']:
            temp['zxbd'] = temp['zxbd'][0]
        elif not temp['zxbd']:
            temp['zxbd'] = '-'
        temp['ah'] = dom_tree.xpath('//*[@id="_container_zhixing"]/table/tbody/tr[s%]/td[2]//text()'%i)
        if temp['ah']:
            temp['ah'] = temp['ah'][0]
        elif not temp['ah']:
            temp['ah'] = '-'
        temp['zxfy'] = dom_tree.xpath('//*[@id="_container_zhixing"]/table/tbody/tr[s%]/td[2]//text()'%i)
        if temp['zxfy']:
            temp['zxfy'] = temp['zxfy'][0]
        elif not temp['zxfy']:
            temp['zxfy'] = '-'
        bzxr.append(temp)
    GongShangBeiJing['bzxr'] = bzxr   
    

    jyyc = [] 
    for i in range(1,20):     #经营异常
       temp = {};
       temp['xh'] = i
       temp['lrrq'] = dom_tree.xpath('//*[@id="_container_abnormal"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['lrrq']:
           break
       temp['lrrq'] = temp['lrrq'][0]

       temp['lryy'] = dom_tree.xpath('//*[@id="_container_abnormal"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['lryy']:
            temp['lryy'] = temp['lryy'][0]
       elif not temp['lryy']:
            temp['lryy'] = '-'
       temp['jdjg'] = dom_tree.xpath('//*[@id="_container_abnormal"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['jdjg']:
            temp['jdjg'] = temp['jdjg'][0]
       elif not temp['jdjg']:
            temp['jdjg'] = '-'
       temp['ycrq'] = dom_tree.xpath('//*[@id="_container_abnormal"]/table/tbody/tr[%s]/td[5]//text()'%i)
       if temp['ycrq']:
            temp['ycrq'] = temp['ycrq'][0]
       elif not temp['ycrq']:
            temp['ycrq'] = '-'
       temp['ycyy'] = dom_tree.xpath('//*[@id="_container_abnormal"]/table/tbody/tr[%s]/td[6]//text()'%i)
       if temp['ycyy']:
            temp['ycyy'] = temp['ycyy'][0]
       elif not temp['ycyy']:
            temp['ycyy'] = '-'
       temp['ycjg'] = dom_tree.xpath('//*[@id="_container_abnormal"]/table/tbody/tr[%s]/td[7]//text()'%i)
       jyyc.append(temp)
       if temp['ycjg']:
            temp['ycjg'] = temp['ycjg'][0]
       elif not temp['ycjg']:
            temp['ycjg'] = '-'
    GongShangBeiJing['jyyc'] = jyyc
       
    xzcf = []
    for i in range(1,20):  #行政处罚
       temp = {};
       temp['xh'] = i
       temp['jdrq'] = dom_tree.xpath('//*[@id="_container_abnormal"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['jdrq']:
           break
       temp['jdrq'] = temp['jdrq'][0]

       temp['jdwsh'] = dom_tree.xpath('//*[@id="_container_punish"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['jdwsh']:
            temp['jdwsh'] = temp['jdwsh'][0]
       elif not temp['jdwsh']:
            temp['jdwsh'] = '-'
       temp['lx'] = dom_tree.xpath('//*[@id="_container_punish"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['lx']:
            temp['lx'] = temp['lx'][0]
       elif not temp['lx']:
            temp['lx'] = '-'
       temp['jdjg'] = dom_tree.xpath('//*[@id="_container_punish"]/table/tbody/tr[%s]/td[5]//text()'%i)
       if temp['jdjg']:
            temp['jdjg'] = temp['jdjg'][0]
       elif not temp['jdjg']:
            temp['jdjg'] = '-'
       xzcf.append(temp)
    GongShangBeiJing['xzcf'] = xzcf
    
    yzwf = []
    for i in range(1,20):   #严重违法
       temp = {};
       temp['xh'] = i
       temp['lrrq'] = dom_tree.xpath('//*[@id="_container_illegal"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['lrrq']:
           break
       temp['lrrq'] = temp['lrrq'][0]
       temp['lryy'] = dom_tree.xpath('//*[@id="_container_illegal"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['lryy']:
            temp['lryy'] = temp['lryy'][0]
       elif not temp['lryy']:
            temp['lryy'] = '-'
       temp['jdjg'] = dom_tree.xpath('//*[@id="_container_illegal"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['jdjg']:
            temp['jdjg'] = temp['jdjg'][0]
       elif not temp['jdjg']:
            temp['jdjg'] = '-'
       yzwf.append(temp)
    GongShangBeiJing['yzwf'] = yzwf

    gqcz = [] 
    for i in range(1,20):  #股权出质
        temp = {};
        temp['xh'] = i
        temp['gqcz_ggsj'] = dom_tree.xpath('//*[@id="_container_equity"]/table/tbody/tr[%s]/td[2]//text()'%i)
        if not temp['gqcz_ggsj']:
            break
        else:
            temp['gqcz_ggsj'] = temp['gqcz_ggsj'][0]
        temp['djbh'] = dom_tree.xpath('//*[@id="_container_equity"]/table/tbody/tr[%s]/td[3]//text()'%i)
        if temp['djbh']:
            temp['djbh'] = temp['djbh'][0]
        elif not temp['djbh']:
            temp['djbh'] = '-'
        temp['czr'] = dom_tree.xpath('//*[@id="_container_equity"]/table/tbody/tr[%s]/td[4]//text()'%i)
        if temp['czr']:
            temp['czr'] = temp['czr'][0]
        temp['zqr'] = dom_tree.xpath('//*[@id="_container_equity"]/table/tbody/tr[%s]/td[5]//text()'%i)
        if temp['zqr']:
           temp['zqr'] = temp['zqr'][0]
        elif not temp['zqr']:
            temp['zqr'] = '-'
        temp['gqcz_zt'] = dom_tree.xpath('//*[@id="_container_equity"]/table/tbody/tr[%s]/td[6]//text()'%i)
        if temp['gqcz_zt']:
            temp['gqcz_zt'] = temp['gqcz_zt'][0]
        elif not temp['gqcz_zt']:
            temp['gqcz_zt'] = '-'
        gqcz.append(temp)
    GongShangBeiJing['gqcz'] = gqcz     

    dcdy = []    
    for i in range(1,20):   #动产抵押
       temp = {};
       temp['xh'] = i
       temp['djrq'] = dom_tree.xpath('//*[@id="_container_mortgage"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['djrq']:
           break
       temp['djrq'] = temp['djrq'][0]
       temp['djh'] = dom_tree.xpath('//*[@id="_container_mortgage"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['djh']:
            temp['djh'] = temp['djh'][0]
       elif not temp['djh']:
            temp['djh'] = '-'
       temp['bdbzqlx'] = dom_tree.xpath('//*[@id="_container_mortgage"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['bdbzqlx']:
            temp['bdbzqlx'] = temp['bdbzqlx'][0]
       elif not temp['bdbzqlx']:
            temp['bdbzqlx'] = '-'
       temp['bdbzqse'] = dom_tree.xpath('//*[@id="_container_mortgage"]/table/tbody/tr[%s]/td[5]/span//text()'%i)
       if temp['bdbzqse']:
            temp['bdbzqse'] = temp['bdbzqse'][0]
       elif not temp['bdbzqse']:
            temp['bdbzqse'] = '-'
       temp['dcdy_djjg'] = dom_tree.xpath('//*[@id="_container_mortgage"]/table/tbody/tr[%s]/td[6]//text()'%i)
       if temp['dcdy_djjg']:
            temp['dcdy_djjg'] = temp['dcdy_djjg'][0]
       elif not temp['dcdy_djjg']:
            temp['dcdy_djjg'] = '-'
       temp['dcdy_zt'] = dom_tree.xpath('//*[@id="_container_mortgage"]/table/tbody/tr[%s]/td[7]//text()'%i)
       if temp['dcdy_zt']:
            temp['dcdy_zt'] = temp['dcdy_zt'][0]
       elif not temp['dcdy_zt']:
            temp['dcdy_zt'] = '-'
       dcdy.append(temp)
    GongShangBeiJing['dcdy'] = dcdy

    qsgg = []
    for i in range(1,20):  #欠税公告
        temp = {};
        temp['xh'] = i
        temp['lari'] = dom_tree.xpath('//*[@id="_container_dishonest"]/table/tbody/tr[%s]/td[2]/span//text()'%i)
        if not temp['lari']:
            break
        temp['lari'] = temp['lari'][0]
        temp['anhao'] = dom_tree.xpath('//*[@id="_container_dishonest"]/table/tbody/tr[%s]/td[3]//text()'%i)
        if temp['anhao']:
            temp['anhao'] = temp['anhao'][0]
        elif not temp['anhao']:
            temp['anhao'] = '-'
        temp['zxfy'] = dom_tree.xpath('//*[@id="_container_dishonest"]/table/tbody/tr[%s]/td[4]//text()'%i)
        if temp['zxfy']:
            temp['zxfy'] = temp['zxfy'][0]
        elif not temp['zxfy']:
            temp['zxfy'] = '-'
        temp['lxzt'] = dom_tree.xpath('//*[@id="_container_dishonest"]/table/tbody/tr[%s]/td[5]//text()'%i)
        if temp['lxzt']:
            temp['lxzt'] = temp['lxzt'][0]
        elif not temp['lxzt']:
            temp['lxzt'] = '-'
        temp['zxyjwh'] = dom_tree.xpath('//*[@id="_container_dishonest"]/table/tbody/tr[%s]/td[6]//text()'%i)
        if temp['zxyjwh']:
            temp['zxyjwh'] = temp['zxyjwh'][0]
        elif not temp['zxyjwh']:
            temp['zxyjwh'] = '-'
        temp['xq'] = dom_tree.xpath('//*[@id="_container_dishonest"]/table/tbody/tr[%s]/td[7]//text()'%i)
        if temp['xq']:
            temp['xq'] = temp['xq'][0]
        elif not temp['xq']:
            temp['xq'] = '-'
        qsgg.append(temp)
    GongShangBeiJing['qsgg'] = qsgg

    sfpm = []
    for i in range(1,20):   #司法拍卖
        temp = {};
        temp['xh'] = i
        temp['pmgg'] = dom_tree.xpath('//*[@id="_container_judicialSale"]/table/tbody/tr[%s]/td[2]/a//text()'%i)
        if not temp['pmgg']:
            break
        temp['pmgg'] = temp['pmgg'][0]
        temp['ggrq'] = dom_tree.xpath('//*[@id="_container_judicialSale"]/table/tbody/tr[%s]/td[3]//text()'%i)
        if temp['ggrq']:
            temp['ggrq'] = temp['ggrq'][0]
        elif not temp['ggrq']:
            temp['ggrq'] = '-'
        temp['zxfy'] = dom_tree.xpath('//*[@id="_container_judicialSale"]/table/tbody/tr[%s]/td[4]//text()'%i)
        if temp['zxfy']:
            temp['zxfy'] = temp['zxfy'][0]
        elif not temp['zxfy']:
            temp['zxfy'] = '-'
        temp['pmbd'] = dom_tree.xpath('//*[@id="_container_judicialSale"]/table/tbody/tr[%s]/td[5]//text()'%i)
        if temp['pmbd']:
            temp['pmbd'] = temp['pmbd'][0]
        elif not temp['pmbd']:
            temp['pmbd'] = '-'
        sfpm.append(temp)
    GongShangBeiJing['sfpm'] = sfpm
    
    rzls = []
    for i in range(1,20):   #融资历史
        temp = {};
        temp['xh'] = i
        temp['rzlssj'] = dom_tree.xpath('//*[@id="_container_rongzi"]/table/tbody/tr[%s]/td[2]//text()'%i)
        if not temp['rzlssj']:
            break
        temp['rzlssj'] = temp['rzlssj'][0]
        temp['rzlslc'] = dom_tree.xpath('//*[@id="_container_rongzi"]/table/tbody/tr[%s]/td[3]//text()'%i)
        if temp['rzlslc']:
            temp['rzlslc'] = temp['rzlslc'][0]
        elif not temp['rzlslc']:
            temp['rzlslc'] = '-'
        temp['rzlsgz'] = dom_tree.xpath('//*[@id="_container_rongzi"]/table/tbody/tr[%s]/td[4]//text()'%i)
        if temp['rzlsgz']:
            temp['rzlsgz'] = temp['rzlsgz'][0]
        elif not temp['rzlsgz']:
            temp['rzlsgz'] = '-'
        temp['rzlsje'] = dom_tree.xpath('//*[@id="_container_rongzi"]/table/tbody/tr[%s]/td[5]//text()'%i)
        if temp['rzlsje']:
            temp['rzlsje'] = temp['rzlsje'][0]
        elif not temp['rzlsje']:
            temp['rzlsje'] = '-'
        temp['rzlsbl'] = dom_tree.xpath('//*[@id="_container_rongzi"]/table/tbody/tr[%s]/td[6]//text()'%i)
        if temp['rzlsbl']:
            temp['rzlsbl'] = temp['rzlsbl'][0]
        elif not temp['rzlsbl']:
            temp['rzlsbl'] = '-'
        temp['rzlstzf'] = dom_tree.xpath('//*[@id="_container_rongzi"]/table/tbody/tr[%s]/td[7]//text()'%i)
        if temp['rzlstzf']:
           temp['rzlstzf'] = temp['rzlstzf'][0]
        else:
           temp['rzlstzf'] = '-'
        temp['rzlsxwly'] = dom_tree.xpath('//*[@id="_container_rongzi"]/table/tbody/tr[%s]/td[8]//text()'%i)
        if temp['rzlsxwly']:
            temp['rzlsxwly'] = temp['rzlsxwly'][0]
        elif not temp['rzlsxwly']:
            temp['rzlsxwly'] = '-'
        rzls.append(temp)
    GongShangBeiJing['rzls'] = rzls
    
    hxtd = []
    for i in range(1,20):   #核心团队
       temp = {};
       temp['xh'] = i
       temp['hxtdrymz'] = dom_tree.xpath('//*[@id="_container_teamMember"]/div[1]/div[%s]/div[1]/div[2]/a//text()'%i)
       if not temp['hxtdrymz']:
           break
       temp['hxtdrymz'] = temp['hxtdrymz'][0]
       temp['hxtdryxx'] = dom_tree.xpath('//*[@id="_container_teamMember"]/div[1]/div[%s]/div[2]//text()'%i)
       if temp['hxtdryxx']:
           temp['hxtdryxx'] = temp['hxtdryxx'][0]
       else:
           temp['hxtdryxx'] = '-'
       hxtd.append(temp)
    GongShangBeiJing['hxtd'] = hxtd
    

    
    qyyw = []
    for i in range(1,50):   #企业业务
       temp = {};
       temp['xh'] = i
       temp['qyywmc'] = dom_tree.xpath('//*[@id="_container_firmProduct"]/div/a[%s]/div[2]/div[1]//text()'%i)
       if not temp['qyywmc']:
           break
       temp['qyywmc'] = temp['qyywmc'][0]
       temp['qyyws'] = dom_tree.xpath('//*[@id="_container_firmProduct"]/div/a[%s]/div[2]/div[2]//text()'%i)
       if temp['qyyws']:
           temp['qyyws'] = temp['qyyws'][0]
       else:
           temp['qyyws'] = '-'
       temp['qyywj'] = dom_tree.xpath('//*[@id="_container_firmProduct"]/div/a[%s]/div[2]/div[3]//text()'%i)
       if temp['qyywj']:
           temp['qyywj'] = temp['qyywj'][0]
       else:
           temp['qyywj'] = '-'
       qyyw.append(temp)
    GongShangBeiJing['qyyw'] = qyyw
    
    xzxk = []
    for i in range(1,50):   #行政许可
       temp = {};
       temp['xh'] = i
       temp['wsh'] = dom_tree.xpath('//*[@id="_container_licensingXyzg"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['wsh']:
           break
       temp['wsh'] = temp['wsh'][0]
       temp['xkjdjg'] = dom_tree.xpath('//*[@id="_container_licensingXyzg"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['xkjdjg']:
           temp['xkjdjg'] = temp['xkjdjg'][0]
       else:
           temp['xkjdjg'] = '-'
       temp['xkjdrq'] = dom_tree.xpath('//*[@id="_container_licensingXyzg"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['xkjdrq']:
           temp['xkjdrq'] = temp['xkjdrq'][0]
       else:
           temp['xkjdrq'] = '-'
       xzxk.append(temp)
    GongShangBeiJing['xzxk'] = xzxk
    
    qyyw = []
    for i in range(1,50):   #企业业务
       temp = {};
       temp['xh'] = i
       temp['qyywmc'] = dom_tree.xpath('//*[@id="_container_firmProduct"]/div/a[%s]/div[2]/div[1]//text()'%i)
       if not temp['qyywmc']:
           break
       temp['qyywmc'] = temp['qyywmc'][0]
       temp['qyyws'] = dom_tree.xpath('//*[@id="_container_firmProduct"]/div/a[%s]/div[2]/div[2]//text()'%i)
       if temp['qyyws']:
           temp['qyyws'] = temp['qyyws'][0]
       else:
           temp['qyyws'] = '-'
       temp['qyywj'] = dom_tree.xpath('//*[@id="_container_firmProduct"]/div/a[%s]/div[2]/div[3]//text()'%i)
       if temp['qyywj']:
           temp['qyywj'] = temp['qyywj'][0]
       else:
           temp['qyywj'] = '-'
       qyyw.append(temp)
    GongShangBeiJing['qyyw'] = qyyw
    
    tzsj = []
    for i in range(1,50):   #投资事件
       temp = {};
       temp['xh'] = i
       temp['sj'] = dom_tree.xpath('//*[@id="_container_touzi"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['sj']:
           break
       temp['sj'] = temp['sj'][0]
       temp['lc'] = dom_tree.xpath('//*[@id="_container_touzi"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['lc']:
           temp['lc'] = temp['lc'][0]
       else:
           temp['lc'] = '-'
       temp['je'] = dom_tree.xpath('//*[@id="_container_touzi"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['je']:
           temp['je'] = temp['je'][0]
       else:
           temp['je'] = '-'
       temp['tzf'] = dom_tree.xpath('//*[@id="_container_touzi"]/table/tbody/tr[%s]/td[5]//text()'%i)
       if temp['tzf']:
           temp['tzf'] = temp['tzf'][0]
       else:
           temp['tzf'] = '-'
       temp['cp'] = dom_tree.xpath('//*[@id="_container_touzi"]/table/tbody/tr[%s]/td[6]//text()'%i)
       if temp['cp']:
           temp['cp'] = temp['cp'][0]
       else:
           temp['cp'] = '-'
       temp['dq'] = dom_tree.xpath('//*[@id="_container_touzi"]/table/tbody/tr[%s]/td[7]//text()'%i)
       if temp['dq']:
           temp['dq'] = temp['dq'][0]
       else:
           temp['dq'] = '-'
       temp['hy'] = dom_tree.xpath('//*[@id="_container_touzi"]/table/tbody/tr[%s]/td[8]//text()'%i)
       if temp['hy']:
           temp['hy'] = temp['hy'][0]
       else:
           temp['hy'] = '-'
       temp['yw'] = dom_tree.xpath('//*[@id="_container_touzi"]/table/tbody/tr[%s]/td[9]//text()'%i)
       if temp['yw']:
           temp['yw'] = temp['yw'][0]
       else:
           temp['yw'] = '-'
       tzsj.append(temp)
    GongShangBeiJing['tzsj'] = tzsj
    
    jpxx = []
    for i in range(1,50):   #竞品信息
       temp = {};
       temp['xh'] = i
       temp['cp'] = dom_tree.xpath('//*[@id="_container_jingpin"]/div/table/tbody/tr[%s]/td[2]/table/tbody/tr/td[2]//text()'%i)
       if not temp['cp']:          
           break
       temp['cp'] = temp['cp'][0]
       temp['dq'] = dom_tree.xpath('//*[@id="_container_jingpin"]/div/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['dq']:
           temp['dq'] = temp['dq'][0]
       else:
           temp['dq'] = '-'
       temp['dqlc'] = dom_tree.xpath('//*[@id="_container_jingpin"]/div/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['dqlc']:
           temp['dqlc'] = temp['dqlc'][0]
       else:
           temp['dqlc'] = '-'
       temp['hy'] = dom_tree.xpath('//*[@id="_container_jingpin"]/div/table/tbody/tr[%s]/td[5]//text()'%i)
       if temp['hy']:
           temp['hy'] = temp['hy'][0]
       else:
           temp['hy'] = '-'
       temp['yw'] = dom_tree.xpath('//*[@id="_container_jingpin"]/div/table/tbody/tr[%s]/td[6]//text()'%i)
       if temp['yw']:
           temp['yw'] = temp['yw'][0]
       else:
           temp['yw'] = '-'
       temp['clsj'] = dom_tree.xpath('//*[@id="_container_jingpin"]/div/table/tbody/tr[%s]/td[7]//text()'%i)
       if temp['clsj']:
           temp['clsj'] = temp['clsj'][0]
       else:
           temp['clsj'] = '-'
       temp['gz'] = dom_tree.xpath('//*[@id="_container_jingpin"]/div/table/tbody/tr[%s]/td[8]//text()'%i)
       if temp['gz']:
           temp['gz'] = temp['gz'][0]
       else:
           temp['gz'] = '-'
       jpxx.append(temp)
    GongShangBeiJing['jpxx'] = jpxx
    
    zpxx = []
    for i in range(1,50):   #招聘信息
       temp = {};
       temp['xh'] = i
       temp['fbsj'] = dom_tree.xpath('//*[@id="_container_recruit"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['fbsj']:          
           break
       temp['fbsj'] = temp['fbsj'][0]
       temp['zpzw'] = dom_tree.xpath('//*[@id="_container_recruit"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['zpzw']:
           temp['zpzw'] = temp['zpzw'][0]
       else:
           temp['zpzw'] = '-'
       temp['xz'] = dom_tree.xpath('//*[@id="_container_recruit"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['xz']:
           temp['xz'] = temp['xz'][0]
       else:
           temp['xz'] = '-'
       temp['gzjy'] = dom_tree.xpath('//*[@id="_container_recruit"]/table/tbody/tr[%s]/td[5]//text()'%i)
       if temp['gzjy']:
           temp['gzjy'] = temp['gzjy'][0]
       else:
           temp['gzjy'] = '-'
       temp['zprs'] = dom_tree.xpath('//*[@id="_container_recruit"]/table/tbody/tr[%s]/td[6]//text()'%i)
       if temp['zprs']:
           temp['zprs'] = temp['zprs'][0]
       else:
           temp['zprs'] = '-'
       temp['szcs'] = dom_tree.xpath('//*[@id="_container_recruit"]/table/tbody/tr[%s]/td[7]//text()'%i)
       if temp['szcs']:
           temp['szcs'] = temp['szcs'][0]
       else:
           temp['szcs'] = '-'
       zpxx.append(temp)
    GongShangBeiJing['zpxx'] = zpxx
    
    swpj = []
    for i in range(1,50):   #税务评级
       temp = {};
       temp['xh'] = i
       temp['nf'] = dom_tree.xpath('//*[@id="_container_taxcredit"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['nf']:
           break
       temp['nf'] = temp['nf'][0]
       temp['nspj'] = dom_tree.xpath('//*[@id="_container_taxcredit"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['nspj']:
           temp['nspj'] = temp['nspj'][0]
       else:
           temp['nspj'] = '-'
       temp['lx'] = dom_tree.xpath('//*[@id="_container_taxcredit"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['lx']:
           temp['lx'] = temp['lx'][0]
       else:
           temp['lx'] = '-'
       temp['nsrsbh'] = dom_tree.xpath('//*[@id="_container_taxcredit"]/table/tbody/tr[%s]/td[5]//text()'%i)
       if temp['nsrsbh']:
           temp['nsrsbh'] = temp['nsrsbh'][0]
       else:
           temp['nsrsbh'] = '-'
       temp['pjdw'] = dom_tree.xpath('//*[@id="_container_taxcredit"]/table/tbody/tr[%s]/td[6]//text()'%i)
       if temp['pjdw']:
           temp['pjdw'] = temp['pjdw'][0]
       else:
           temp['pjdw'] = '-'
       swpj.append(temp)
    GongShangBeiJing['swpj'] = swpj
    
    ccjc = []
    for i in range(1,50):   #抽查检查
       temp = {};
       temp['xh'] = i
       temp['rq'] = dom_tree.xpath('//*[@id="_container_check"]/div/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['rq']:
           break
       temp['rq'] = temp['rq'][0]
       temp['jg'] = dom_tree.xpath('//*[@id="_container_check"]/div/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['jg']:
           temp['jg'] = temp['jg'][0]
       else:
           temp['jg'] = '-'
       temp['ssjg'] = dom_tree.xpath('//*[@id="_container_check"]/div/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['ssjg']:
           temp['ssjg'] = temp['ssjg'][0]
       else:
           temp['ssjg'] = '-'
       ccjc.append(temp)
    GongShangBeiJing['ccjc'] = ccjc
    
    zzzs = []
    for i in range(1,50):   #资质证书
       temp = {};
       temp['xh'] = i
       temp['zslx'] = dom_tree.xpath('//*[@id="_container_certificate"]/table/tbody/tr[%s]/td[2]/span//text()'%i)
       if not temp['zslx']:
           break
       temp['zslx'] = temp['zslx'][0]
       temp['zsbh'] = dom_tree.xpath('//*[@id="_container_certificate"]/table/tbody/tr[%s]/td[3]/span//text()'%i)
       if temp['zsbh']:
           temp['zsbh'] = temp['zsbh'][0]
       else:
           temp['zsbh'] = '-'
       temp['fzrq'] = dom_tree.xpath('//*[@id="_container_certificate"]/table/tbody/tr[%s]/td[4]/span//text()'%i)
       if temp['fzrq']:
           temp['fzrq'] = temp['fzrq'][0]
       else:
           temp['fzrq'] = '-'
       temp['jzrq'] = dom_tree.xpath('//*[@id="_container_certificate"]/table/tbody/tr[%s]/td[5]/span//text()'%i)
       if temp['jzrq']:
           temp['jzrq'] = temp['jzrq'][0]
       else:
           temp['jzrq'] = '-'
       zzzs.append(temp)
    GongShangBeiJing['zzzs'] = zzzs
    
    ztbxx = []
    for i in range(1,50):   #招投标信息
       temp = {};
       temp['xh'] = i
       temp['fbsj'] = dom_tree.xpath('//*[@id="_container_bid"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['fbsj']:
           break
       temp['fbsj'] = temp['fbsj'][0]
       temp['bt'] = dom_tree.xpath('//*[@id="_container_bid"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['bt']:
           temp['bt'] = temp['bt'][0]
       else:
           temp['bt'] = '-'
       temp['cgr'] = dom_tree.xpath('//*[@id="_container_bid"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['cgr']:
           temp['cgr'] = temp['cgr'][0]
       else:
           temp['cgr'] = '-'
       ztbxx.append(temp)
    GongShangBeiJing['ztbxx'] = ztbxx
    
    
    cpxx = []
    for i in range(1,50):   #产品信息
       temp = {};
       temp['xh'] = i
       temp['cpmc'] = dom_tree.xpath('//*[@id="_container_product"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['cpmc']:
           break
       temp['cpmc'] = temp['cpmc'][0]
       temp['cpjc'] = dom_tree.xpath('//*[@id="_container_product"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['cpjc']:
           temp['cpjc'] = temp['cpjc'][0]
       else:
           temp['cpjc'] = '-'
       temp['cpfl'] = dom_tree.xpath('//*[@id="_container_product"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['cpfl']:
           temp['cpfl'] = temp['cpfl'][0]
       else:
           temp['cpfl'] = '-'
       temp['ly'] = dom_tree.xpath('//*[@id="_container_product"]/table/tbody/tr[%s]/td[5]//text()'%i)
       if temp['ly']:
           temp['ly'] = temp['ly'][0]
       else:
           temp['ly'] = '-'
       cpxx.append(temp)
    GongShangBeiJing['cpxx'] = cpxx
    
    wxgzh = []
    for i in range(1,50):   #微信公众号
       temp = {};
       temp['xh'] = i
       temp['gsmc'] = dom_tree.xpath('//*[@id="_container_wechat"]/div[1]/div[%s]/div[2]/div[1]//text()'%i)
       if not temp['gsmc']:
           break
       temp['gsmc'] = temp['gsmc'][0]
       temp['wxh'] = dom_tree.xpath('//*[@id="_container_wechat"]/div[1]/div[%s]/div[2]/div[2]//text()'%i)
       if temp['wxh']:
           temp['wxh'] = temp['wxh'][1]
       else:
           temp['wxh'] = '-'
       gnjs = dom_tree.xpath('//*[@id="_container_wechat"]/div[1]/div[%s]/div[2]/div[3]/span[3]/script//text()'%i)
       if gnjs:
           pattern11 = re.compile('"recommend":"([\s\S]*?)"')
           gnjs1 = ''.join(gnjs)
           items11 = re.findall(pattern11,gnjs1)
           temp['gnjs'] = items11
           temp['gnjs'] = temp['gnjs'][0]
       else:
           temp['gnjs'] = '-'
       wxgzh.append(temp)
    GongShangBeiJing['wxgzh'] = wxgzh
    
    
    jckxy = []
    for i in range(1,50):   #进出口信用
       temp = {};
       temp['xh'] = i
       temp['zchg'] = dom_tree.xpath('//*[@id="_container_importAndExport"]/table/tbody/tr[%s]/td[1]//text()'%i)
       if not temp['zchg']:
           break
       temp['zchg'] = temp['zchg'][0]
       temp['hgbm'] = dom_tree.xpath('//*[@id="_container_importAndExport"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if temp['hgbm']:
           temp['hgbm'] = temp['hgbm'][0]
       else:
           temp['hgbm'] = '-'
       temp['jylb'] = dom_tree.xpath('//*[@id="_container_importAndExport"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['jylb']:
           temp['jylb'] = temp['jylb'][0]
       else:
           temp['jylb'] = '-'
       jckxy.append(temp)
    GongShangBeiJing['jckxy'] = jckxy
    
    
    sbxx = []
    for i in range(1,50):   #商标信息
       temp = {};
       temp['xh'] = i
       temp['sqri'] = dom_tree.xpath('//*[@id="_container_tmInfo"]/div[2]/table/tbody/tr[%s]/td[2]/span//text()'%i)
       if not temp['sqri']:
           break
       temp['sqri'] = temp['sqri'][0]
       temp['sbmc'] = dom_tree.xpath('//*[@id="_container_tmInfo"]/div[2]/table/tbody/tr[%s]/td[4]/span//text()'%i)
       if temp['sbmc']:
           temp['sbmc'] = temp['sbmc'][0]
       else:
           temp['sbmc'] = '-'
       temp['zch'] = dom_tree.xpath('//*[@id="_container_tmInfo"]/div[2]/table/tbody/tr[%s]/td[5]/span//text()'%i)
       if temp['zch']:
           temp['zch'] = temp['zch'][0]
       else:
           temp['zch'] = '-'
       temp['lb'] = dom_tree.xpath('//*[@id="_container_tmInfo"]/div[2]/table/tbody/tr[%s]/td[6]/span//text()'%i)
       if temp['lb']:
           temp['lb'] = temp['lb'][0]
       else:
           temp['lb'] = '-'
       temp['lczt'] = dom_tree.xpath('//*[@id="_container_tmInfo"]/div[2]/table/tbody/tr[%s]/td[7]/span//text()'%i)
       if temp['lczt']:
           temp['lczt'] = temp['lczt'][0]
       else:
           temp['lczt'] = '-'
       sbxx.append(temp)
    GongShangBeiJing['sbxx'] = sbxx
    
    zlxx = []
    for i in range(1,50):   #专利信息
       temp = {};
       temp['xh'] = i
       temp['sqgbr'] = dom_tree.xpath('//*[@id="_container_patent"]/table/tbody/tr[%s]/td[2]/span//text()'%i)
       if not temp['sqgbr']:
           break
       temp['sqgbr'] = temp['sqgbr'][0]
       temp['zlmc'] = dom_tree.xpath('//*[@id="_container_patent"]/table/tbody/tr[%s]/td[3]/span//text()'%i)
       if temp['zlmc']:
           temp['zlmc'] = temp['zlmc'][0]
       else:
           temp['zlmc'] = '-'
       temp['sqh'] = dom_tree.xpath('//*[@id="_container_patent"]/table/tbody/tr[%s]/td[4]/span//text()'%i)
       if temp['sqh']:
           temp['sqh'] = temp['sqh'][0]
       else:
           temp['sqh'] = '-'
       temp['sqgbh'] = dom_tree.xpath('//*[@id="_container_patent"]/table/tbody/tr[%s]/td[5]/span//text()'%i)
       if temp['sqgbh']:
           temp['sqgbh'] = temp['sqgbh'][0]
       else:
           temp['sqgbh'] = '-'
       temp['zllx'] = dom_tree.xpath('//*[@id="_container_patent"]/table/tbody/tr[%s]/td[6]/span//text()'%i)
       if temp['zllx']:
           temp['zllx'] = temp['zllx'][0]
       else:
           temp['zllx'] = '-'
       zlxx.append(temp)
    GongShangBeiJing['zlxx'] = zlxx
    
    rjzzq = []
    for i in range(1,50):   #软件著作权
       temp = {};
       temp['xh'] = i
       temp['pzrq'] = dom_tree.xpath('//*[@id="_container_copyright"]/table/tbody/tr[%s]/td[2]/span//text()'%i)
       if not temp['pzrq']:
           break
       temp['pzrq'] = temp['pzrq'][0]
       temp['rjqc'] = dom_tree.xpath('//*[@id="_container_copyright"]/table/tbody/tr[%s]/td[3]/span//text()'%i)
       if temp['rjqc']:
           temp['rjqc'] = temp['rjqc'][0]
       else:
           temp['rjqc'] = '-'
       temp['rjjc'] = dom_tree.xpath('//*[@id="_container_copyright"]/table/tbody/tr[%s]/td[4]/span//text()'%i)
       if temp['rjjc']:
           temp['rjjc'] = temp['rjjc'][0]
       else:
           temp['rjjc'] = '-'
       temp['djh'] = dom_tree.xpath('//*[@id="_container_copyright"]/table/tbody/tr[%s]/td[5]/span//text()'%i)
       if temp['djh']:
           temp['djh'] = temp['djh'][0]
       else:
           temp['djh'] = '-'
       temp['flh'] = dom_tree.xpath('//*[@id="_container_copyright"]/table/tbody/tr[%s]/td[6]/span//text()'%i)
       if temp['flh']:
           temp['flh'] = temp['flh'][0]
       else:
           temp['flh'] = '-'
       temp['bbh'] = dom_tree.xpath('//*[@id="_container_copyright"]/table/tbody/tr[%s]/td[7]/span//text()'%i)
       if temp['bbh']:
           temp['bbh'] = temp['bbh'][0]
       else:
           temp['bbh'] = '-'
       rjzzq.append(temp)
    GongShangBeiJing['rjzzq'] = rjzzq
    
    
    zpzzq = []
    for i in range(1,50):   #作品著作权
       temp = {};
       temp['xh'] = i
       temp['zpmc'] = dom_tree.xpath('//*[@id="_container_copyrightWorks"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['zpmc']:
           break
       temp['zpmc'] = temp['zpmc'][0]
       temp['djh'] = dom_tree.xpath('//*[@id="_container_copyrightWorks"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['djh']:
           temp['djh'] = temp['djh'][0]
       else:
           temp['djh'] = '-'
       temp['lb'] = dom_tree.xpath('//*[@id="_container_copyrightWorks"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['lb']:
           temp['lb'] = temp['lb'][0]
       else:
           temp['lb'] = '-'
       temp['czwcrq'] = dom_tree.xpath('//*[@id="_container_copyrightWorks"]/table/tbody/tr[%s]/td[5]//text()'%i)
       if temp['czwcrq']:
           temp['czwcrq'] = temp['czwcrq'][0]
       else:
           temp['czwcrq'] = '-'
       temp['djrq'] = dom_tree.xpath('//*[@id="_container_copyrightWorks"]/table/tbody/tr[%s]/td[6]//text()'%i)
       if temp['djrq']:
           temp['djrq'] = temp['djrq'][0]
       else:
           temp['djrq'] = '-'
       temp['scfbrq'] = dom_tree.xpath('//*[@id="_container_copyrightWorks"]/table/tbody/tr[%s]/td[7]//text()'%i)
       if temp['scfbrq']:
           temp['scfbrq'] = temp['scfbrq'][0]
       else:
           temp['scfbrq'] = '-'
       zpzzq.append(temp)
    GongShangBeiJing['zpzzq'] = zpzzq
    
    wzba = []
    for i in range(1,50):   #网站备案
       temp = {};
       temp['xh'] = i
       temp['shsj'] = dom_tree.xpath('//*[@id="_container_icp"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['shsj']:
           break
       temp['shsj'] = temp['shsj'][0]
       temp['wzmc'] = dom_tree.xpath('//*[@id="_container_icp"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['wzmc']:
           temp['wzmc'] = temp['wzmc'][0]
       else:
           temp['wzmc'] = '-'
       temp['wzsy'] = dom_tree.xpath('//*[@id="_container_icp"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['wzsy']:
           temp['wzsy'] = temp['wzsy'][0]
       else:
           temp['wzsy'] = '-'
       temp['ym'] = dom_tree.xpath('//*[@id="_container_icp"]/table/tbody/tr[%s]/td[5]//text()'%i)
       if temp['ym']:
           temp['ym'] = temp['ym'][0]
       else:
           temp['ym'] = '-'
       temp['bah'] = dom_tree.xpath('//*[@id="_container_icp"]/table/tbody/tr[%s]/td[6]//text()'%i)
       if temp['bah']:
           temp['bah'] = temp['bah'][0]
       else:
           temp['bah'] = '-'
       temp['zt'] = dom_tree.xpath('//*[@id="_container_icp"]/table/tbody/tr[%s]/td[7]//text()'%i)
       if temp['zt']:
           temp['zt'] = temp['zt'][0]
       else:
           temp['zt'] = '-'
       temp['dwxz'] = dom_tree.xpath('//*[@id="_container_icp"]/table/tbody/tr[%s]/td[8]//text()'%i)
       if temp['dwxz']:
           temp['dwxz'] = temp['dwxz'][0]
       else:
           temp['dwxz'] = '-'
       wzba.append(temp)
    GongShangBeiJing['wzba'] = wzba
    
    
    
#    lsfddbr = []
#    for i in range(1,20):   #历史法定代表人
#       temp = {};
#       temp['xh'] = i
#       temp['zcsj'] = dom_tree.xpath('//*[@id="_container_pastICCount"]/table/tbody/tr[%s]/td[1]//text()'%i)
#       if not temp['zcsj']:
#           break
#       temp['zcsj'] = temp['zcsj'][0]
#       temp['zcdz'] = dom_tree.xpath('//*[@id="_container_pastICCount"]/table/tbody/tr[%s]/td[3]//text()'%i)
#       if temp['zcdz']:
#           temp['zcdz'] = temp['zcdz'][0]
#       else:
#           temp['zcdz'] = '-'
#       lsfddbr.append(temp)
#    GongShangBeiJing['lsfddbr'] = lsfddbr
#    
#    
#    lszcdz = {}
#    pattern10 = re.compile('历史注册地址([\s\S]*?\d')
#    items10 = re.findall(pattern10,response)
#    print(items10)
#    lszcdz['历史注册地址'] = items10
#    
##    for i in range(1,20):   #历史注册地址
##       temp = {};
##       temp['xh'] = i
##       temp['zcsj'] = dom_tree.xpath('//*[@id="_container_pastICCount"]/table/tbody/tr[%s]/td[2]//text()'%i)
##       if not temp['zcsj']:
##           break
##       temp['zcsj'] = temp['zcsj'][0]
##       temp['zcdz'] = dom_tree.xpath('//*[@id="_container_pastICCount"]/table/tbody/tr[%s]/td[3]//text()'%i)
##       if temp['zcdz']:
##           temp['zcdz'] = temp['zcdz'][0]
##       else:
##           temp['zcdz'] = '-'
##       lszcdz.append(temp)
#    GongShangBeiJing['lszcdz'] = lszcdz
    
#    lsgsxx = []
#    for i in range(1,20):   #历史工商信息
#       temp = {};
#       temp['xh'] = i
#       temp['lszyxx'] = dom_tree.xpath('//*[@id="_container_pastICCount"]/table/tbody//text()'%i)
#       if not temp['lszyxx']:
#           break
#       pattern = re.compile('历史营业期限([/s/S*?])历史')
#    GongShangBeiJing['lsgsxx'] = lsgsxx
    
    
    lsgd = []
    for i in range(1,20):   #历史股东
       temp = {};
       temp['xh'] = i
       temp['mz'] = dom_tree.xpath('//*[@id="_container_pastHolderCount"]/table/tbody/tr[%s]/td[2]/div/a//text()'%i)
       if not temp['mz']:
           break
       temp['mz'] = temp['mz'][0]
       temp['gs'] = dom_tree.xpath('//*[@id="_container_pastHolderCount"]/table/tbody/tr[%s]/td[2]/div/div[2]/a//text()'%i)
       if temp['gs']:
           temp['gs'] = temp['gs'][0]
       else:
           temp['gs'] = '-'
       temp['czbl'] = dom_tree.xpath('//*[@id="_container_pastHolderCount"]/table/tbody/tr[%s]/td[3]/div//text()'%i)
       if temp['czbl']:
           temp['czbl'] = temp['czbl'][0]
       else:
           temp['czbl'] = '-'
       temp['rjcz'] = dom_tree.xpath('//*[@id="_container_pastHolderCount"]/table/tbody/tr[%s]/td[4]/div//text()'%i)
       if temp['rjcz']:
           temp['rjcz'] = temp['rjcz'][0]
       else:
           temp['rjcz'] = '-'
       lsgd.append(temp)
    GongShangBeiJing['lsgd'] = lsgd
    
    lsdwtz = []
    for i in range(1,20):   #历史对外投资
       temp = {};
       temp['xh'] = i
       temp['gsmc'] = dom_tree.xpath('//*[@id="_container_pastInverstCount"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['gsmc']:
           break
       temp['gsmc'] = temp['gsmc'][0]
       temp['mz'] = dom_tree.xpath('//*[@id="_container_pastInverstCount"]/table/tbody/tr[%s]/td[3]/span/a//text()'%i)
       if temp['mz']:
           temp['mz'] = temp['mz'][0]
       else:
           temp['mz'] = '-'
       temp['gs'] = dom_tree.xpath('//*[@id="_container_pastInverstCount"]/table/tbody/tr[%s]/td[3]/span/span/a//text()'%i)
       if temp['gs']:
           temp['gs'] = temp['gs'][0]
       else:
           temp['gs'] = '-'
       temp['zczb'] = dom_tree.xpath('//*[@id="_container_pastInverstCount"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['zczb']:
           temp['zczb'] = temp['zczb'][0]
       else:
           temp['zczb'] = '-'
       temp['tzzb'] = dom_tree.xpath('//*[@id="_container_pastInverstCount"]/table/tbody/tr[%s]/td[5]//text()'%i)
       if temp['tzzb']:
           temp['tzzb'] = temp['tzzb'][0]
       else:
           temp['tzzb'] = '-'
       temp['zcsj'] = dom_tree.xpath('//*[@id="_container_pastInverstCount"]/table/tbody/tr[%s]/td[6]//text()'%i)
       if temp['zcsj']:
           temp['zcsj'] = temp['zcsj'][0]
       else:
           temp['zcsj'] = '-'
       temp['zt'] = dom_tree.xpath('//*[@id="_container_pastInverstCount"]/table/tbody/tr[%s]/td[7]//text()'%i)
       if temp['zt']:
           temp['zt'] = temp['zt'][0]
       else:
           temp['zt'] = '-'
       lsdwtz.append(temp)
    GongShangBeiJing['lsdwtz'] = lsdwtz
    


    lsktgg = []
    for i in range(1,20):   #历史开庭公告
       temp = {};
       temp['xh'] = i
       temp['ktrq'] = dom_tree.xpath('//*[@id="_container_pastAnnouncementCount"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['ktrq']:
           break
       temp['ktrq'] = temp['ktrq'][0]
       temp['ay'] = dom_tree.xpath('//*[@id="_container_pastAnnouncementCount"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['ay']:
           temp['ay'] = temp['ay'][0]
       else:
           temp['ay'] = '-'
       temp['ygssr'] = dom_tree.xpath('//*[@id="_container_pastAnnouncementCount"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['ygssr']:
           temp['ygssr'] = temp['ygssr'][0]
       else:
           temp['ygssr'] = '-'
       temp['bgbssr'] = dom_tree.xpath('//*[@id="_container_pastAnnouncementCount"]/table/tbody/tr[%s]/td[5]//text()'%i)
       if temp['bgbssr']:
           temp['bgbssr'] = temp['bgbssr'][0]
       else:
           temp['bgbssr'] = '-'
       lsktgg.append(temp)
    GongShangBeiJing['lsktgg'] = lsktgg
    
    
    lsflss = []
    for i in range(1,20):   #历史法律诉讼
       temp = {};
       temp['xh'] = i
       temp['rq'] = dom_tree.xpath('//*[@id="_container_pastLawsuitCount"]/div/div[1]/table/tbody/tr[%s]/td[2]/span//text()'%i)
       if not temp['rq']:
           break
       temp['rq'] = temp['rq'][0]
       temp['cpws'] = dom_tree.xpath('//*[@id="_container_pastLawsuitCount"]/div/div[1]/table/tbody/tr[%s]/td[3]/a//text()'%i)
       if temp['cpws']:
           temp['cpws'] = temp['cpws'][0]
       else:
           temp['cpws'] = '-'
       temp['ay'] = dom_tree.xpath('//*[@id="_container_pastLawsuitCount"]/div/div[1]/table/tbody/tr[%s]/td[4]/a//text()'%i)
       if temp['ay']:
           temp['ay'] = temp['ay'][0]
       else:
           temp['ay'] = '-'
       temp['ajsf'] = dom_tree.xpath('//*[@id="_container_pastLawsuitCount"]/div/div[1]/table/tbody/tr[%s]/td[5]/a//text()'%i)
       if temp['ajsf']:
           temp['ajsf'] = temp['ajsf'][0]
       else:
           temp['ajsf'] = '-'
       temp['ah'] = dom_tree.xpath('//*[@id="_container_pastLawsuitCount"]/div/div[1]/table/tbody/tr[%s]/td[6]/a//text()'%i)
       if temp['ah']:
           temp['ah'] = temp['ah'][0]
       else:
           temp['ah'] = '-'
       lsflss.append(temp)
    GongShangBeiJing['lsflss'] = lsflss
    
    
    lsfygg = []
    for i in range(1,20):   #历史法院公告
       temp = {};
       temp['xh'] = i
       temp['ggsj'] = dom_tree.xpath('//*[@id="_container_pastCourtCount"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['ggsj']:
           break
       temp['ggsj'] = temp['ggsj'][0]
       temp['ssf'] = dom_tree.xpath('//*[@id="_container_pastCourtCount"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['ssf']:
           temp['ssf'] = temp['ssf'][0]
       else:
           temp['ssf'] = '-'
       temp['bsf'] = dom_tree.xpath('//*[@id="_container_pastCourtCount"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['bsf']:
           temp['bsf'] = temp['bsf'][0]
       else:
           temp['bsf'] = '-'
       temp['gglx'] = dom_tree.xpath('//*[@id="_container_pastCourtCount"]/table/tbody/tr[%s]/td[5]//text()'%i)
       if temp['gglx']:
           temp['gglx'] = temp['gglx'][0]
       else:
           temp['gglx'] = '-'
       temp['fy'] = dom_tree.xpath('//*[@id="_container_pastCourtCount"]/table/tbody/tr[%s]/td[6]//text()'%i)
       if temp['fy']:
           temp['fy'] = temp['fy'][0]
       else:
           temp['fy'] = '-'
       lsfygg.append(temp)
    GongShangBeiJing['lsfygg'] = lsfygg
    
    lssxrxx = []
    for i in range(1,20):   #历史失信人信息
       temp = {};
       temp['xh'] = i
       temp['larq'] = dom_tree.xpath('//*[@id="_container_pastDishonest"]/table/tbody/tr[%s]/td[2]/span//text()'%i)
       if not temp['larq']:
           break
       temp['larq'] = temp['larq'][0]
       temp['ah'] = dom_tree.xpath('//*[@id="_container_pastDishonest"]/table/tbody/tr[%s]/td[3]/span//text()'%i)
       if temp['ah']:
           temp['ah'] = temp['ah'][0]
       else:
           temp['ah'] = '-'
       temp['zxfy'] = dom_tree.xpath('//*[@id="_container_pastDishonest"]/table/tbody/tr[%s]/td[4]/span//text()'%i)
       if temp['zxfy']:
           temp['zxfy'] = temp['zxfy'][0]
       else:
           temp['zxfy'] = '-'
       temp['lxzt'] = dom_tree.xpath('//*[@id="_container_pastDishonest"]/table/tbody/tr[%s]/td[5]/span//text()'%i)
       if temp['lxzt']:
           temp['lxzt'] = temp['lxzt'][0]
       else:
           temp['lxzt'] = '-'
       temp['zxyjwh'] = dom_tree.xpath('//*[@id="_container_pastDishonest"]/table/tbody/tr[%s]/td[6]/span//text()'%i)
       if temp['zxyjwh']:
           temp['zxyjwh'] = temp['zxyjwh'][0]
       else:
           temp['zxyjwh'] = '-'
       lssxrxx.append(temp)
    GongShangBeiJing['lssxrxx'] = lssxrxx
    
    
    lsbzxrxx = []
    for i in range(1,20):   #历史被执行人信息
       temp = {};
       temp['xh'] = i
       temp['larq'] = dom_tree.xpath('//*[@id="_container_pastZhixing"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['larq']:
           break
       temp['larq'] = temp['larq'][0]
       temp['zxbd'] = dom_tree.xpath('//*[@id="_container_pastZhixing"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['zxbd']:
           temp['zxbd'] = temp['zxbd'][0]
       else:
           temp['zxbd'] = '-'
       temp['ah'] = dom_tree.xpath('//*[@id="_container_pastZhixing"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['ah']:
           temp['ah'] = temp['ah'][0]
       else:
           temp['ah'] = '-'
       temp['zxfy'] = dom_tree.xpath('//*[@id="_container_pastZhixing"]/table/tbody/tr[%s]/td[5]//text()'%i)
       if temp['zxfy']:
           temp['zxfy'] = temp['zxfy'][0]
       else:
           temp['zxfy'] = '-'
       lsbzxrxx.append(temp)
    GongShangBeiJing['lsbzxrxx'] = lsbzxrxx
    
    lsxzcf = []
    for i in range(1,20):   #历史行政处罚
       temp = {};
       temp['xh'] = i
       temp['jdrq'] = dom_tree.xpath('//*[@id="_container_pastPunishmentIC"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['jdrq']:
           break
       temp['jdrq'] = temp['jdrq'][0]
       temp['jdswh'] = dom_tree.xpath('//*[@id="_container_pastPunishmentIC"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['jdswh']:
           temp['jdswh'] = temp['jdswh'][0]
       else:
           temp['jdswh'] = '-'
       temp['lx'] = dom_tree.xpath('//*[@id="_container_pastPunishmentIC"]/table/tbody/tr[%s]/td[4]/text()'%i)
       if temp['lx']:
           temp['lx'] = temp['lx'][0]
       else:
           temp['lx'] = '-'
       temp['jdjg'] = dom_tree.xpath('//*[@id="_container_pastPunishmentIC"]/table/tbody/tr[%s]/td[5]//text()'%i)
       if temp['jdjg']:
           temp['jdjg'] = temp['jdjg'][0]
       else:
           temp['jdjg'] = '-'
       lsxzcf.append(temp)
    GongShangBeiJing['lsxzcf'] = lsxzcf
    
    lsgqcz = []
    for i in range(1,20):   #历史股权出质
       temp = {};
       temp['xh'] = i
       temp['ggsj'] = dom_tree.xpath('//*[@id="_container_pastEquityCount"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['ggsj']:
           break
       temp['ggsj'] = temp['ggsj'][0]
       temp['djbh'] = dom_tree.xpath('//*[@id="_container_pastEquityCount"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['djbh']:
           temp['djbh'] = temp['djbh'][0]
       else:
           temp['djbh'] = '-'
       temp['czr'] = dom_tree.xpath('//*[@id="_container_pastEquityCount"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['czr']:
           temp['czr'] = temp['czr'][0]
       else:
           temp['czr'] = '-'
       temp['zqr'] = dom_tree.xpath('//*[@id="_container_pastEquityCount"]/table/tbody/tr[%s]/td[5]//text()'%i)
       if temp['zqr']:
           temp['zqr'] = temp['zqr'][0]
       else:
           temp['zqr'] = '-'

       temp['zt'] = dom_tree.xpath('//*[@id="_container_pastEquityCount"]/table/tbody/tr[%s]/td[6]//text()'%i)
       if temp['zt']:
           temp['zt'] = temp['zt'][0]
       else:
           temp['zt'] = '-'
       lsgqcz.append(temp)
    GongShangBeiJing['lsgqcz'] = lsgqcz
    
    lsxzxk = []
    for i in range(1,20):   #历史行政许可
       temp = {};
       temp['xh'] = i
       temp['xkswh'] = dom_tree.xpath('//*[@id="_container_getPastLicenseCN"]/table/tbody/tr[%s]/td[2]//text()'%i)
       if not temp['xkswh']:
           break
       temp['xkswh'] = temp['xkswh'][0]
       temp['xkjdjg'] = dom_tree.xpath('//*[@id="_container_getPastLicenseCN"]/table/tbody/tr[%s]/td[3]//text()'%i)
       if temp['xkjdjg']:
           temp['xkjdjg'] = temp['xkjdjg'][0]
       else:
           temp['xkjdjg'] = '-'
       temp['xkjdrq'] = dom_tree.xpath('//*[@id="_container_getPastLicenseCN"]/table/tbody/tr[%s]/td[4]//text()'%i)
       if temp['xkjdrq']:
           temp['xkjdrq'] = temp['xkjdrq'][0]
       else:
           temp['xkjdrq'] = '-'

       lsxzxk.append(temp)
    GongShangBeiJing['lsxzxk'] = lsxzxk

    
    
    
    
    
    return GongShangBeiJing
        

        

if __name__ == '__main__':
    app.run(host='192.168.2.200', port=10086)

