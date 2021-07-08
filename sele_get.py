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



driver = webdriver.Chrome()
driver.get("http://www.imxingzhe.com/user/login")

#程序打开网页后20秒内手动登陆账户
time.sleep(50)

with open('cookies.txt','w') as cookief:
    #将cookies保存为json格式
    cookief.write(json.dumps(driver.get_cookies()))

driver.close()
