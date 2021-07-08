#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
File Name:
Author: wudi
Mail: programmerwudi@gmail.com
Created Time: 2021-07-08 01:04:54
"""

import re
import os
rootPath = r"/Users/xxxx/github/xinzhe/download"
fileList = os.listdir(rootPath)
for fileName in fileList:
    filePath = os.path.join(rootPath,fileName)

    lines = open(filePath, errors='ignore',encoding='utf-8').readlines()
    fp = open(filePath, 'w', errors='ignore',encoding='utf-8')
    newlines = []
    for line in lines:
        pattern = r'xmlns="http://www.topografix.com/GPX/1/0"'
        rep = r'xmlns="http://www.topografix.com/GPX/1/1"'
        line = re.sub(pattern,rep,line)
        newlines.append(line)
    fp.writelines(newlines)
    fp.close()
