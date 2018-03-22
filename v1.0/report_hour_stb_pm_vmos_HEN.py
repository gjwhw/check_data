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

# 传入文件地址路径
filename = sys.argv[1]
# 定义列名的列表
name = ['TIMESTAMP', '省地区代码', '市地区代码', 'STB_ID', '机顶盒IP', '业务帐号', '机顶盒SN',
        'MDI-DF平均值', 'MDI-MLR平均值', 'RTP丢包率平均值', 'MDI-DF劣化百分比', 'MDI-MLR劣化百分比',
        'RTP丢包率劣化百分比', '卡顿总时长', '收视总时长', '卡顿总次数', '卡顿超过10秒的总次数', '收视vmos']
# 通过DataFrame函数导入文件，iterator=True 用迭代的方式
x = pd.read_csv(filename, iterator=True, names=name, sep='|', header=None)
# 大文件分割处理，一次取10万行
loop = True
chunkSize = 100000
chunks = []
# g = 0
while loop:
    try:
        chunk = x.get_chunk(chunkSize)
        # 第一列时间格式为：‘2018-03-22 00:00：00’，取前13位进行分割，后面实现按小时分组：‘2018-03-22 00’
        chunk['TIMESTAMP'] = chunk['TIMESTAMP'].astype('str').str[:13]
        # 求平均数的指标
        y = chunk.groupby(['TIMESTAMP', '省地区代码', '市地区代码'], as_index=False)['MDI-DF平均值', \
                                                                           'MDI-MLR平均值', 'RTP丢包率平均值', 'MDI-DF劣化百分比', 'MDI-MLR劣化百分比', 'RTP丢包率劣化百分比', '收视vmos'].mean()
        # 小数点保留6位
        y = y.round(6)
        # 求和
        n = chunk.groupby(['TIMESTAMP', '省地区代码', '市地区代码'], as_index=False)['卡顿总时长', '收视总时长', '卡顿总次数', \
                                                                           '卡顿超过10秒的总次数'].sum()
        n = n.round(6)
        # 按照3列进行拼接
        z = pd.merge(y, n, on=['TIMESTAMP', '省地区代码', '市地区代码'])

        chunks.append(z)
        starttime3 = datetime.datetime.now()
        # g += 1
        # print g
    except StopIteration:
        loop = False
        print "Iteration is stopped."
# 将分割的块文件进行拼接，忽略列名
df = pd.concat(chunks, ignore_index=True)
# 再次求平均值
y = df.groupby(['TIMESTAMP', '省地区代码', '市地区代码'], as_index=False)['MDI-DF平均值', \
                                                                'MDI-MLR平均值', 'RTP丢包率平均值', 'MDI-DF劣化百分比', 'MDI-MLR劣化百分比', 'RTP丢包率劣化百分比', '收视vmos'].mean()
y = y.round(6)
# 再次求和
n = df.groupby(['TIMESTAMP', '省地区代码', '市地区代码'], as_index=False)['卡顿总时长', '收视总时长', '卡顿总次数', \
                                                                '卡顿超过10秒的总次数'].sum()
n = n.round(6)
# 按照3列进行拼接
z = pd.merge(y, n, on=['TIMESTAMP', '省地区代码', '市地区代码'])
# 导出文件，去掉索引，去掉列名
z.to_csv('temporary_file', index=False, sep='|', header=0)
# 重命名文件
os.unlink(filename)
shutil.move('temporary_file', filename)

print '运行时间'
endtime = datetime.datetime.now()
print(endtime - starttime)
