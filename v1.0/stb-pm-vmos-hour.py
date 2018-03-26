#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2018/3/21 14:57
# @Auther   :GJW
# @File     :report_hour_stb_pm_vmos_HEN.py
# @Software :PyCharm
import os
import sys
import shutil
import datetime
import pandas as pd
starttime = datetime.datetime.now()
print('开始时间')
print(starttime)

# 传入文件地址路径
# filename = sys.argv[1]
# filename = sys.argv[2]
filename = '321.txt'
filename2 = '1122.txt'
# 定义列名的列表
name1 = ['TIMESTAMP', '省地区代码', '市地区代码', 'STB_ID', '机顶盒IP', '业务帐号', '机顶盒SN',
        'MDI-DF平均值', 'MDI-MLR平均值', 'RTP丢包率平均值', 'MDI-DF劣化百分比', 'MDI-MLR劣化百分比',
        'RTP丢包率劣化百分比', '卡顿总时长', '收视总时长', '卡顿总次数', '卡顿超过10秒的总次数', '收视vmos']
# 通过DataFrame函数导入文件，iterator=True 用迭代的方式
stb_pm_vmos = pd.read_csv(filename, iterator=True, names=name1, sep='|', header=None)
stb_pm_vmos_chunk = stb_pm_vmos.get_chunk()
# 定义列名的列表
name2 = ['TIMESTAMP', '省地区代码', '市地区代码', 'STB_ID', '机顶盒IP', '业务账号', '接入方式', '机顶盒SN序列号',
		 '机顶盒MAC', '厂商名称', '机顶盒型号', '机顶盒软件版本号', '机顶盒硬件版本号',]
stb_cm = pd.read_csv(filename2,iterator=True, names=name2, sep='|', header=None)
stb_cm_chunk = stb_cm.get_chunk()
# 提取需要的3列数据
stb_cm_chunk = stb_cm_chunk.loc[:,['STB_ID','厂商名称', '机顶盒型号']]

# 第一列时间格式为：‘2018-03-22 00:00：00’，取前13位进行分割，后面实现按小时分组：‘2018-03-22 00’
stb_pm_vmos_chunk['TIMESTAMP'] = stb_pm_vmos_chunk['TIMESTAMP'].astype('str').str[:13]
# 按照STB_ID进行拼接
chunk = pd.merge(stb_pm_vmos_chunk, stb_cm_chunk, on=['STB_ID'])

# 求平均数的指标
avg = chunk.groupby(['TIMESTAMP', '省地区代码', '市地区代码','厂商名称', '机顶盒型号'], as_index=False)['MDI-DF平均值',
				'MDI-MLR平均值', 'RTP丢包率平均值', 'MDI-DF劣化百分比', 'MDI-MLR劣化百分比', 'RTP丢包率劣化百分比', '收视vmos'].mean()
# 小数点保留6位
avg = avg.round(6)
# 求和
sum = chunk.groupby(['TIMESTAMP', '省地区代码', '市地区代码','厂商名称', '机顶盒型号'], as_index=False)['卡顿总时长',
				'收视总时长', '卡顿总次数', '卡顿超过10秒的总次数'].sum()
sum = sum.round(6)
# 按照3列进行拼接
print("Iteration is stopped.")
# 按照3列进行拼接
file_out = pd.merge(avg, sum, on=['TIMESTAMP', '省地区代码', '市地区代码','厂商名称', '机顶盒型号'])

# 导出文件，去掉索引，去掉列名
file_out.to_csv('temporary_file', index=False, sep='|', header=0)
stb_pm_vmos.close()
stb_cm.close()
# 重命名文件
# os.unlink(filename)
# shutil.move('temporary_file', filename)

print('运行时间')
endtime = datetime.datetime.now()
print(endtime - starttime)
