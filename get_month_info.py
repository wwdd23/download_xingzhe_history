#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
File Name:
Author: wudi
Mail: programmerwudi@gmail.com
Created Time: 2021-07-07 19:29:44
"""
import json
import time
from urllib.request import Request, urlopen
from selenium import webdriver


import wget
import ssl


def write_url(year, month, user_id):
    url = "https://www.imxingzhe.com/api/v4/user_month_info/?user_id="+ str(user_id) + "&year="+ str(year) + "&month=" + str(month)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    request = Request( url, headers=headers)
    html = urlopen( request )
    data = html.read()
    #print(data)
    #strs = str(data)
    raw_json = json.loads(data)
    #print(raw_json)
    #print(strs)
    
    print("Get %s %s gpx:" % (year, month))
    
    for i in raw_json['data']['wo_info']:
        g_id = i['id']
        print(g_id)
        # create gpx url
        gpx_url = "https://www.imxingzhe.com/xing/" + str(g_id) +"/gpx/"
        print(gpx_url)
        d_name = str(g_id) + "_" + i["title"]
        with open('list.txt','a') as cookief:
            #将cookies保存为json格式
            cookief.write(gpx_url)
            cookief.write('\n')

def year_month(start_year, end_year):
    date_list = []
    years = range(start_year, end_year+1)
    months = range(1, 13)
    for y in years:
        for m in months:
            date_list.append([y,m])
    return date_list

def add_month():
    date_list = []
    years = range(2011, 2022)
    for y in years:
        date_list.append([y,12])
    months = range(1, 13)
    for m in months:
        date_list.append([2021,m])
    return date_list



if __name__ == '__main__':
    y_m = year_month(2018, 2022)
    #y_m = add_month()
    user_id = 5064
    for i in y_m:
        write_url(i[0], i[1], user_id)
    

