#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2018/4/17 11:52
# @Auther   :GJW
# @File     :functions.py
# @Software :PyCharm
import pandas as pd
# 老指标校验程序

class Test:
    def epg_pm(self, file_in, file_out):
        # 生成准确性校验字典字典
        dict1 = {'EPG-PM-totalnum': 0, 'EPG-PM-007': 0, 'EPG-PM-008': 0, 'EPG-PM-009': 0, 'EPG-PM-010': 0,
                 'EPG-PM-007<=EPG-PM-008': 0, 'EPG-PM-009<=EPG-PM-010': 0}
        
        # 命名file_in文件的列名
        columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # 读取file_in文件
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        file_chunk['count1'] = 1
        try:
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        except ValueError :
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError :
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n > 0 :
            try:
                # 总行数
                dict1['EPG-PM-totalnum'] = file_chunk['count1'].sum()
                # 判断条件 EPG在线用户数<=100000
                dict1['EPG-PM-007'] = file_chunk.loc[file_chunk[7] > 100000].count1.count()
                # 判断条件 0<服务器能力值<=1000000
                dict1['EPG-PM-008'] = file_chunk.loc[(file_chunk[8] > 1000000) | (file_chunk[8] <= 0)].count1.count()
                # 判断条件 EPG请求成功次数<=10000000
                dict1['EPG-PM-009'] = file_chunk.loc[file_chunk[9] > 10000000].count1.count()
                # 判断条件 EPG请求总次数<=10000000
                dict1['EPG-PM-010'] = file_chunk.loc[file_chunk[10] > 10000000].count1.count()
                # 判断条件 EPG在线用户数<=服务器能力值
                dict1['EPG-PM-007<=EPG-PM-008'] = file_chunk.loc[(file_chunk[7] > file_chunk[8])].count1.count()
                # 判断条件 EPG请求成功次数<=EPG请求总次数
                dict1['EPG-PM-009<=EPG-PM-010'] = file_chunk.loc[file_chunk[9] > file_chunk[10]].count1.count()
                exact = pd.DataFrame([dict1])
                # 写入file_out文件
                exact.T.to_csv(file_out, sep='|', header=None)
                # 符合数值判断条件的行输出
                xx = file_chunk.loc[
                    (file_chunk[7] > 100000) | (file_chunk[8] > 1000000) | (file_chunk[8] <= 0) | (file_chunk[9] > 10000000) | (
                            file_chunk[10] > 10000000), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]].to_csv(file_out + '.value', sep='|',
                                                                                                header=None, index=False)
                # 符合逻辑判断条件的行输出
                yy = file_chunk.loc[
                    (file_chunk[7] > file_chunk[8]) | (file_chunk[9] > file_chunk[10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]].to_csv(
                    file_out + '.logic', sep='|', header=None, index=False)
                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [7, 8, 9, 10]:
                    if file_chunk[x].dtype == 'object' :
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)
                
    
    def cdn_pm(self, file_in, file_out):
        # 生成准确性校验字典字典
        dict1 = {'CDN-PM-totalnum': 0, 'CDN-PM-007': 0, 'CDN-PM-008': 0, 'CDN-PM-009': 0, 'CDN-PM-010': 0,
                 'CDN-PM-007<=CDN-PM-008': 0,
                 'CDN-PM-009<=CDN-PM-010': 0}
        
        # 命名file_in文件的列名
        columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        # 读取file_in文件
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        file_chunk['count1'] = 1
        try:
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        except ValueError :
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError :
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n >0 :
            try:
                # 总行数
                dict1['CDN-PM-totalnum'] = file_chunk['count1'].sum()
                # 判断条件 服务并发数<=10000
                dict1['CDN-PM-007'] = file_chunk.loc[file_chunk[7] > 10000].count1.count()
                # 判断条件 0<CDN节点负载能力<=100000
                dict1['CDN-PM-008'] = file_chunk.loc[(file_chunk[8] > 100000) | (file_chunk[8] <= 0)].count1.count()
                # 判断条件 节点占用存储<=100000
                dict1['CDN-PM-009'] = file_chunk.loc[file_chunk[9] > 100000].count1.count()
                # 判断条件 0<节点存储总容量<=1000000
                dict1['CDN-PM-010'] = file_chunk.loc[(file_chunk[10] > 1000000) | (file_chunk[10] <= 0)].count1.count()
                # 判断条件 服务并发数<=CDN节点负载能力
                dict1['CDN-PM-007<=CDN-PM-008'] = file_chunk.loc[file_chunk[7] > file_chunk[8]].count1.count()
                # 节点占用存储<=节点存储总容量
                dict1['CDN-PM-009<=CDN-PM-010'] = file_chunk.loc[file_chunk[9] > file_chunk[10]].count1.count()
                exact = pd.DataFrame([dict1])
                # 写入file_out文件
                exact.T.to_csv(file_out, sep='|', header=None)
                # 符合数值判断条件的行输出
                xx = file_chunk.loc[
                    (file_chunk[7] > 10000) | (file_chunk[8] > 100000) | (file_chunk[8] <= 0) | (file_chunk[9] > 100000) | (
                            file_chunk[10] > 1000000) | (file_chunk[10] <= 0), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]].to_csv(
                    file_out + '.value', sep='|', header=None, index=False)
                # 符合逻辑判断条件的行输出
                yy = file_chunk.loc[
                    (file_chunk[7] > file_chunk[8]) | (file_chunk[9] > file_chunk[10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                                                                         11]].to_csv(
                    file_out + '.logic', sep='|', header=None, index=False)
                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [7, 8, 9 ,10]:
                    if file_chunk[x].dtype == 'object':
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)
    
    def stb_pm_opers(self, file_in, file_out):
        # 生成准确性校验字典字典
        dict1 = {'STB-PM-OPERS-018': 0, 'STB-PM-OPERS-019': 0, 'STB-PM-OPERS-032': 0, 'STB-PM-OPERS-033': 0, }
        
        # 命名file_in文件的列名
        columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
        # 读取file_in文件
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        file_chunk['count1'] = 1
        try:
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        except ValueError :
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError :
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n>0 :
            try:
                # 总行数
                dict1['STB-PM-OPERS-totalnum'] = file_chunk['count1'].sum()
                # 判断条件 点击直播成功数<=1000
                dict1['STB-PM-OPERS-018'] = file_chunk.loc[file_chunk[18] > 1000].count1.count()
                # 判断条件 点击直播总数<=1000
                dict1['STB-PM-OPERS-019'] = file_chunk.loc[file_chunk[19] > 1000].count1.count()
                # 判断条件 点击点播成功数<=1000
                dict1['STB-PM-OPERS-032'] = file_chunk.loc[file_chunk[32] > 1000].count1.count()
                # 判断条件 点击点播总数<=1000
                dict1['STB-PM-OPERS-033'] = file_chunk.loc[file_chunk[33] > 1000].count1.count()
                # 判断条件 点击直播成功数<=点击直播总数
                dict1['STB-PM-OPERS-018<=STB-PM-OPERS-019'] = file_chunk.loc[file_chunk[18] > file_chunk[19]].count1.count()
                # 判断条件 点击点播成功数<=点击点播总数
                dict1['STB-PM-OPERS-032<=STB-PM-OPERS-033'] = file_chunk.loc[file_chunk[32] > file_chunk[33]].count1.count()
                
                exact = pd.DataFrame([dict1])
                # 写入file_out文件
                exact.T.to_csv(file_out, sep='|', header=None)
                
                # 符合数值判断条件的行输出
                xx = file_chunk.loc[
                    (file_chunk[18] > 1000) | (file_chunk[19] > 1000) | (file_chunk[32] > 1000) |
                    (file_chunk[33] > 1000), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                                              24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]].to_csv(
                    file_out + '.value', sep='|',
                    header=None, index=False)
                # 符合逻辑判断条件的行输出
                yy = file_chunk.loc[
                    (file_chunk[18] > file_chunk[19]) | (file_chunk[32] > file_chunk[33]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                                                                                            12, 13, 14, 15, 16, 17, 18, 19, 20,
                                                                                            21, 22, 23, 24, 25, 26, 27, 28, 29,
                                                                                            30, 31, 32, 33, 34, 35, 36, 37, 38,
                                                                                            39]].to_csv(
                    file_out + '.logic', sep='|', header=None, index=False)
                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [18, 19, 32, 33]:
                    if file_chunk[x].dtype == 'object' :
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)
    
    def stb_pm_vmos(self, file_in, file_out):
        # 生成准确性校验字典字典
        dict1 = {'STB-PM-VMOS-totalnum': 0, 'STB-PM-VMOS-008': 0, 'STB-PM-VMOS-009': 0, 'STB-PM-VMOS-010': 0,
                 'STB-PM-VMOS-014': 0, 'STB-PM-VMOS-015': 0, 'STB-PM-VMOS-016': 0, 'STB-PM-VMOS-017': 0,
                 'STB-PM-VMOS-018': 0,
                 'STB-PM-VMOS-014<=STB-PM-VMOS-015': 0, 'STB-PM-VMOS-017<=STB-PM-VMOS-016': 0}
        
        # 命名file_in文件的列名
        columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        # 读取file_in文件
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        file_chunk['count1'] = 1
        try:
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        except ValueError :
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError :
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n > 0 :
            try:
                # 总行数
                dict1['STB-PM-VMOS-totalnum'] = file_chunk['count1'].sum()
                # MDI-DF平均值<=1000
                dict1['STB-PM-VMOS-008'] = file_chunk.loc[file_chunk[8] > 1000].count1.count()
                # MDI-MLR平均值<=100
                dict1['STB-PM-VMOS-009'] = file_chunk.loc[file_chunk[9] > 100].count1.count()
                # RTP丢包率平均值<=100
                dict1['STB-PM-VMOS-010'] = file_chunk.loc[file_chunk[10] > 100].count1.count()
                # 卡顿总时长<=900
                dict1['STB-PM-VMOS-014'] = file_chunk.loc[file_chunk[14] > 900].count1.count()
                # 收视总时长<=900
                dict1['STB-PM-VMOS-015'] = file_chunk.loc[file_chunk[15] > 900].count1.count()
                # 卡顿总次数<=1000000
                dict1['STB-PM-VMOS-016'] = file_chunk.loc[file_chunk[16] > 1000000].count1.count()
                # 卡顿超过10秒的总次数<=90
                dict1['STB-PM-VMOS-017'] = file_chunk.loc[file_chunk[17] > 90].count1.count()
                # 0<收视vmos<=5
                dict1['STB-PM-VMOS-018'] = file_chunk.loc[(file_chunk[18] > 5) ].count1.count()
                # 卡顿总时长<=收视总时长
                dict1['STB-PM-VMOS-014<=STB-PM-VMOS-015'] = file_chunk.loc[file_chunk[14] > file_chunk[15]].count1.count()
                # 卡顿超过10秒的总次数<=卡顿总次数
                dict1['STB-PM-VMOS-017<=STB-PM-VMOS-016'] = file_chunk.loc[file_chunk[17] > file_chunk[16]].count1.count()
                exact = pd.DataFrame([dict1])
                # 写入file_out文件
                exact.T.to_csv(file_out, sep='|', header=None)
                # 符合数值判断条件的行输出
                xx = file_chunk.loc[
                    (file_chunk[8] > 1000) | (file_chunk[9] > 100) | (file_chunk[10] > 100) |
                    (file_chunk[14] > 900) | (file_chunk[15] > 900) | (file_chunk[16] > 900) | (file_chunk[17] > 900) | (
                                file_chunk[18] > 5) ,
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]].to_csv(file_out + '.value', sep='|',
                                                                                            header=None, index=False)
                # 符合逻辑判断条件的行输出
                yy = file_chunk.loc[
                    (file_chunk[14] > file_chunk[15]) | (file_chunk[17] > file_chunk[16]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                                                                                            12, 13, 14, 15, 16, 17, 18]].to_csv(
                    file_out + '.logic', sep='|', header=None, index=False)

                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [8, 9, 10, 14, 15, 16, 17,18]:
                    if file_chunk[x].dtype == 'object':
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)

