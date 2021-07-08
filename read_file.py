#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
File Name:
Author: wudi
Mail: programmerwudi@gmail.com
Created Time: 2021-07-08 00:35:29
"""

f = open("./list.txt","r") 
lines = f.readlines()      #读取全部内容 ，并以列表方式返回
for line in lines:
    print(line) 

