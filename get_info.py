#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
File Name:
Author: wudi
Mail: programmerwudi@gmail.com
Created Time: 2021-07-07 23:41:12
"""

import json
import time
from urllib.request import Request, urlopen
from selenium import webdriver


# 配置下载路径
options = webdriver.ChromeOptions()
path = '' # 写入你需要下载的目录 /Users/xxxx/github/xinzhe/download
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': path }
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=options)
#driver.get("http://www.imxingzhe.com/user/login")
driver.get("http://www.imxingzhe.com")

driver.delete_all_cookies()
#程序打开网页后20秒内手动登陆账户
time.sleep(2)

#首先清除由于浏览器打开已有的cookies

with open('cookies.txt','r') as cookief:
    #使用json读取cookies 注意读取的是文件 所以用load而不是loads
    cookieslist = json.load(cookief)
    for cookie in cookieslist:
        driver.add_cookie(cookie)


try:
    driver.refresh() # 刷新方法 refresh
    print ('test pass: refresh successful')
except Exception as e:
    print ("Exception found", format(e))

f = open("./list.txt","r")
lines = f.readlines()      #读取全部内容 ，并以列表方式返回
for line in lines:
    print(line)
    #driver.get("https://www.imxingzhe.com/xing/100438865/gpx/")
    driver.get(line)
    try:
        driver.refresh() # 刷新方法 refresh
        print ('test pass: refresh successful')
    except Exception as e:
        print ("Exception found", format(e))



driver.close()
