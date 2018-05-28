#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2018/3/21 14:57
# @Auther   :GJW
# @File     :report_hour_datatype_HEN.py
# @Software :PyCharm

import datetime
import sys

import exact as func

starttime = datetime.datetime.now()
print('开始时间')
print(starttime)
# file_in = sys.argv[1]
# file_out = sys.argv[2]
# func_name = sys.argv[3]
# file_in = 'IPTV-LINK-PM.txt'
# file_out = 'IPTV-LINK-PM-OUT.txt'
# func_name = 'iptv_link_pm'
file_in = '1234.txt'
file_out = 'STB-TRANS-OUT.txt'
func_name = 'cdn_pm'
c = func.Test()
try:
    getattr(c, func_name)(file_in,file_out)
except FileNotFoundError:
    print(func_name+"指标未采集到")

print('运行时间')
endtime = datetime.datetime.now()
print(endtime - starttime)
