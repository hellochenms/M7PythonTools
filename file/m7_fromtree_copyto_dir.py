#!/usr/bin/python
# -*- coding: utf-8 -*-
# _m7_file_fromtree_copyto_dir.py
# chenms
# 2014-07-09

# 将多层目录中的文件复制到一个目录中
# 需求场景是将多层目录的照片复制到一个目录，便于全选上传网盘

import os
from shutil import copyfile  

dest_dir = 'dest_dir'
if not (os.path.exists(dest_dir)):
    os.mkdir(dest_dir)

srcDir = 'src_dir'
for path, subdir, files in os.walk(srcDir):
    for fileName in files:
        copyfile(os.path.join(path, fileName), os.path.join(dest_dir, fileName))
