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
# file_in = sys.argv[1]
# file_out = sys.argv[2]
# func_name = sys.argv[3]
# file_in = 'STB-PM-VMOS'
# file_out = 'STB-PM-VMOS.txt'
# func_name = 'stb_pm_vmos'
file_in = '1234.txt'
file_out = 'EPG-PM.txt'
func_name = 'cdn_pm'

c = func.Test()
try:
    getattr(c, func_name)(file_in,file_out)
except FileNotFoundError:
    print(func_name+"指标未采集到")


print('运行时间')
endtime = datetime.datetime.now()
print(endtime - starttime)
