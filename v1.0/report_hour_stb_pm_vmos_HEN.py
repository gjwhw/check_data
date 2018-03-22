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
print '开始时间'
print starttime
name = ['TIMESTAMP', '省地区代码', '市地区代码', 'STB_ID', '机顶盒IP', '业务帐号', '机顶盒SN', \
        'MDI-DF平均值', 'MDI-MLR平均值', 'RTP丢包率平均值', 'MDI-DF劣化百分比', 'MDI-MLR劣化百分比', \
        'RTP丢包率劣化百分比', '卡顿总时长', '收视总时长', '卡顿总次数', '卡顿超过10秒的总次数', '收视vmos']
x = pd.read_csv('123.txt', iterator=True, names=name, sep='|', header=None)

loop = True
chunkSize = 100000
chunks = []
g = 0
while loop:
    try:
        chunk = x.get_chunk(chunkSize)
        chunk['TIMESTAMP'] = chunk['TIMESTAMP'].astype('str').str[:13]

        y = chunk.groupby(['TIMESTAMP', '省地区代码', '市地区代码'], as_index=False)['MDI-DF平均值', \
                                                                           'MDI-MLR平均值', 'RTP丢包率平均值', 'MDI-DF劣化百分比', 'MDI-MLR劣化百分比', 'RTP丢包率劣化百分比', '收视vmos'].mean()
        y = y.round(6)
        n = chunk.groupby(['TIMESTAMP', '省地区代码', '市地区代码'], as_index=False)['卡顿总时长', '收视总时长', '卡顿总次数', \
                                                                           '卡顿超过10秒的总次数'].sum()
        n = n.round(6)

        z = pd.merge(y, n, on=['TIMESTAMP', '省地区代码', '市地区代码'])

        chunks.append(z)
        starttime3 = datetime.datetime.now()
        g += 1
        print g
    except StopIteration:
        loop = False
        print "Iteration is stopped."

df = pd.concat(chunks, ignore_index=True)

y = df.groupby(['TIMESTAMP', '省地区代码', '市地区代码'], as_index=False)['MDI-DF平均值', \
                                                                'MDI-MLR平均值', 'RTP丢包率平均值', 'MDI-DF劣化百分比', 'MDI-MLR劣化百分比', 'RTP丢包率劣化百分比', '收视vmos'].mean()
y = y.round(6)

n = df.groupby(['TIMESTAMP', '省地区代码', '市地区代码'], as_index=False)['卡顿总时长', '收视总时长', '卡顿总次数', \
                                                                '卡顿超过10秒的总次数'].sum()
n = n.round(6)

z = pd.merge(y, n, on=['TIMESTAMP', '省地区代码', '市地区代码'])

z.to_csv('32111.txt', index=False, sep='|', header=0)

print '运行时间'
endtime = datetime.datetime.now()
print(endtime - starttime)
