#!/usr/bin/python
# -*- coding: utf-8 -*-
# _m7_file_regex_rmtree.py
# chenms
# 2014-07-09

# 删除iOS工程中build生成的DerivedData文件夹

import os
import re
import shutil

for path, subdir, files in os.walk('.'):
    match = re.search(r'.*DerivedData$', path)
    if match:
        print path
        shutil.rmtree(path)        
