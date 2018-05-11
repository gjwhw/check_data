#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2018/3/21 14:57
# @Auther   :GJW
# @File     :report_hour_datatype_HEN.py
# @Software :PyCharm
# import functions as fun
import datetime
import exact as func
import sys



starttime = datetime.datetime.now()
print('开始时间')
print(starttime)
file_in = sys.argv[1]
file_out = sys.argv[2]
func_name = sys.argv[3]
# file_in = 'STB-PM-OPERS.txt'
# file_out = 'STB-PM-OPERS-OUT.txt'
# func_name = 'stb_pm_opers'

c = func.Test()
getattr(c, func_name)(file_in,file_out)


print('运行时间')
endtime = datetime.datetime.now()
print(endtime - starttime)
