#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2018/3/21 14:57
# @Auther   :GJW
# @File     :report_hour_datatype_HEN.py
# @Software :PyCharm
# import functions as fun
import datetime
import data_integrity as func
import sys



starttime = datetime.datetime.now()
print('开始时间')
print(starttime)
file_in = sys.argv[1]
file_out = sys.argv[2]
datatype = sys.argv[3]
# file_in = '123.txt'
# file_out = '1234.txt'
# datatype = 'epg_pm'
func_name = 'wanzheng'

c = func.Test()
getattr(c, func_name)(file_in,file_out, datatype)

# c = fun.Treating()
# getattr(c, func_name)(file_in,file_out)
# 重命名文件
# os.unlink(filename)
# shutil.move('temporary_file', filename)

print('运行时间')
endtime = datetime.datetime.now()
print(endtime - starttime)
