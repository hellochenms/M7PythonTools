#!/usr/bin/python
# -*- coding:utf-8 -*-

### m7_rename_ios_png.py
### 1.0.0
### 2014-10-16
### chenms

## png文件批量重命名为iOS需要的名字
## 1.只识别png
## 2.默认将非@2x~iphone.png结尾的图片修改为该结尾
## 2.1.可以识别@2x.png，不会出现@2x@2x~iphone.png的情况
## 3. 第一个参数是目录路径，该参数不允许以'-'符号开始
## 4. 输入-pad参数，结尾中的iphone会替换为ipad
## 5. 输入-3x参数，结尾中的@2x会替换为@3x

import sys
import os

ext = 'png'

isPad = False
is3x = False
for arg in sys.argv:
    if arg == '-pad':
        isPad = True  
    elif arg == '-3x':
        is3x = True

scale = '@2x'
if is3x:
    scale = '@3x'

short_suffix = '~iphone'
if isPad:
    short_suffix = '~ipad' 
suffix = scale + short_suffix
    
if len(sys.argv) >= 2 and not sys.argv[1].startswith('-'):
    dirName = sys.argv[1]
    for path, subdirs, files in os.walk(dirName):
        for fileName in files:
            if not fileName.startswith('.'):
                fileNameParts = fileName.split('.')
                if (not fileNameParts[0].endswith(suffix)) and (fileNameParts[1] == ext):
                    if fileNameParts[0].endswith(scale):
                        renameFileName = fileNameParts[0] + short_suffix + '.' + fileNameParts[1]
                    else:
                        renameFileName = fileNameParts[0] + suffix + '.' + fileNameParts[1]
                    #print renameFileName
                    os.rename(os.path.join(path, fileName), os.path.join(path, renameFileName))
