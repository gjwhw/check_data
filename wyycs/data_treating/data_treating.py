#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2018/3/21 14:57
# @Auther   :GJW
# @File     :report_hour_datatype_HEN.py
# @Software :PyCharm
# import functions as fun
import datetime
import functions as func
import sys



starttime = datetime.datetime.now()
print('开始时间')
print(starttime)

# 传入文件地址路径
file_in = sys.argv[1]
file_out = sys.argv[2]
func_name = sys.argv[3]
#file_in = 'epg.txt'
#file_out = 'epg11.txt'
#func_name = 'packet1'
c = func.Treating()
getattr(c, func_name)(file_in,file_out)
# c = fun.Treating()
# getattr(c, func_name)(file_in,file_out)
# 重命名文件
# os.unlink(filename)
# shutil.move('temporary_file', filename)

print('运行时间')
endtime = datetime.datetime.now()
print(endtime - starttime)
