#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-19 15:02:00
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import sys
import shutil
import datetime
import city
import chkdef

starttime = datetime.datetime.now()
print '开始时间'
print starttime

file_path = sys.argv[1]

file_valid = open((file_path+'.valid'), 'w')
with open(file_path) as file_1:
    for allline in file_1:
        line = allline.split('|')
        stb_id = line[3]
        if len(stb_id) > 5:
            file_valid.write(allline)
file_valid.close()

os.unlink(file_path)
shutil.move(file_path+'.valid', file_path)

endtime = datetime.datetime.now()
print '运行时间'
print(endtime - starttime)