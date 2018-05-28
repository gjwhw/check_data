#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2018/4/17 11:52
# @Auther   :GJW
# @File     :functions.py
# @Software :PyCharm
import pandas as pd
# 新指标校验

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
        except ValueError:
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError:
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n > 0:
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
                    (file_chunk[7] > 100000) | (file_chunk[8] > 1000000) | (file_chunk[8] <= 0) | (
                                file_chunk[9] > 10000000) | (
                            file_chunk[10] > 10000000), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]].to_csv(file_out + '.value',
                                                                                                sep='|',
                                                                                                header=None,
                                                                                                index=False)
                # 符合逻辑判断条件的行输出
                yy = file_chunk.loc[
                    (file_chunk[7] > file_chunk[8]) | (file_chunk[9] > file_chunk[10]), [1, 2, 3, 4, 5, 6, 7, 8, 9,
                                                                                         10]].to_csv(
                    file_out + '.logic', sep='|', header=None, index=False)
                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [7, 8, 9, 10]:
                    if file_chunk[x].dtype == 'object':
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)
    
    def cdn_pm(self, file_in, file_out):
        # 生成准确性校验字典字典
        dict1 = {'CDN-PM-totalnum': 0, 'CDN-PM-007': 0, 'CDN-PM-008': 0, 'CDN-PM-009': 0, 'CDN-PM-010': 0,
                 'CDN-PM-011': 0, 'CDN-PM-012': 0, 'CDN-PM-013': 0, 'CDN-PM-015': 0, 'CDN-PM-016': 0, 'CDN-PM-017': 0,
                 'CDN-PM-008<=CDN-PM-007': 0,
                 'CDN-PM-0010<=CDN-PM-011': 0, 'CDN-PM-0012<=CDN-PM-013': 0, 'CDN-PM-0016<=CDN-PM-017': 0}
        
        # 命名file_in文件的列名
        columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        # 读取file_in文件
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        file_chunk['count1'] = 1
        try:
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        except ValueError:
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError:
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n > 0:
            try:
                # 总行数
                dict1['CDN-PM-totalnum'] = file_chunk['count1'].sum()
                # 判断条件 0<CDN节点并发负载能力<=100000
                dict1['CDN-PM-007'] = file_chunk.loc[(file_chunk[7] > 100000) | (file_chunk[7] <= 0)].count1.count()
                # 判断条件 CDN节点并发负载<=10000
                dict1['CDN-PM-008'] = file_chunk.loc[(file_chunk[8] > 10000)].count1.count()
                # 判断条件 0<CDN节点上联带宽(Gbit/s)<=1000000
                dict1['CDN-PM-009'] = file_chunk.loc[(file_chunk[9] > 1000000) | (file_chunk[9] <= 0)].count1.count()
                # 判断条件 CDN节点实时出口流量(Gbit/s)<=1000000
                dict1['CDN-PM-010'] = file_chunk.loc[(file_chunk[10] > 1000000)].count1.count()
                # 判断条件 CDN节点设计吞吐量(Gbit/s)<=1000000
                dict1['CDN-PM-011'] = file_chunk.loc[(file_chunk[11] > 1000000) | (file_chunk[11] <= 0)].count1.count()
                # 判断条件 节点占用存储(TB)<=100000
                dict1['CDN-PM-012'] = file_chunk.loc[(file_chunk[12] > 100000)].count1.count()
                # 判断条件 节点存储总容量(TB)<=1000000
                dict1['CDN-PM-013'] = file_chunk.loc[(file_chunk[13] > 1000000) | (file_chunk[13] <= 0)].count1.count()
                # 判断条件 CDN节点归属用户数<=1000000
                dict1['CDN-PM-015'] = file_chunk.loc[(file_chunk[15] > 1000000)].count1.count()
                # 判断条件 CDN命中服务次数<=1000000
                dict1['CDN-PM-016'] = file_chunk.loc[(file_chunk[16] > 1000000)].count1.count()
                # 判断条件 CDN节点归属用户请求总次数<=1000000
                dict1['CDN-PM-017'] = file_chunk.loc[(file_chunk[17] > 1000000)].count1.count()
                # 判断条件 CDN节点并发负载<=CDN节点并发负载能力
                dict1['CDN-PM-008<=CDN-PM-007'] = file_chunk.loc[(file_chunk[8] > file_chunk[7])].count1.count()
                # CDN节点实时出口流量(Gbit/s)<=节CDN节点设计吞吐量(Gbit/s)
                dict1['CDN-PM-0010<=CDN-PM-011'] = file_chunk.loc[(file_chunk[10] > file_chunk[11])].count1.count()
                # 节点占用存储(TB)<=节点存储总容量(TB)
                dict1['CDN-PM-0012<=CDN-PM-013'] = file_chunk.loc[(file_chunk[12] > file_chunk[13])].count1.count()
                # CDN命中服务次数<=CDN节点归属用户请求总次数
                dict1['CDN-PM-0016<=CDN-PM-017'] = file_chunk.loc[(file_chunk[16] > file_chunk[17])].count1.count()
                
                exact = pd.DataFrame([dict1])
                # 写入file_out文件
                exact.T.to_csv(file_out, sep='|', header=None)
                # 符合数值判断条件的行输出
                xx = file_chunk.loc[
                    (file_chunk[7] > 100000) | (file_chunk[7] <= 0) | (file_chunk[8] > 10000) | (
                                file_chunk[9] > 1000000) | (
                            file_chunk[9] <= 0) |
                    (file_chunk[10] > 1000000) | (file_chunk[11] > 1000000) | (file_chunk[11] <= 0) | (
                            file_chunk[12] > 100000) |
                    (file_chunk[13] > 1000000) | (file_chunk[13] <= 0) | (file_chunk[15] > 1000000) | (
                            file_chunk[16] > 1000000) |
                    (file_chunk[17] > 1000000), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]].to_csv(
                    file_out + '.value', sep='|', header=None, index=False)
                # 符合逻辑判断条件的行输出
                yy = file_chunk.loc[
                    (file_chunk[8] > file_chunk[7]) | (file_chunk[10] > file_chunk[11]) | (
                                file_chunk[12] > file_chunk[13]) |
                    (file_chunk[16] > file_chunk[17]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                                                        17]].to_csv(
                    file_out + '.logic', sep='|', header=None, index=False)
                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [7, 8, 9, 10, 11, 12, 13, 15, 16, 17]:
                    if file_chunk[x].dtype == 'object':
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)
    
    def stb_inserv_rtsp(self, file_in, file_out):
        # 生成准确性校验字典字典
        dict1 = {'STB-INSERV-RTSP-totalnum': 0, 'STB-INSERV-RTSP-007': 0, 'STB-INSERV-RTSP-008': 0,
                 'STB-INSERV-RTSP-009': 0, 'STB-INSERV-RTSP-010': 0,
                 'STB-INSERV-RTSP-011': 0, 'STB-INSERV-RTSP-012': 0, 'STB-INSERV-RTSP-013': 0, 'STB-INSERV-RTSP-014': 0,
                 'STB-INSERV-RTSP-015': 0,
                 'STB-INSERV-RTSP-016': 0, 'STB-INSERV-RTSP-021': 0, 'STB-INSERV-RTSP-022': 0, 'STB-INSERV-RTSP-023': 0,
                 'STB-INSERV-RTSP-007<=STB-INSERV-RTSP-008': 0, 'STB-INSERV-RTSP-010<=STB-INSERV-RTSP-009': 0,
                 'STB-INSERV-RTSP-012<=STB-INSERV-RTSP-011': 0,
                 'STB-INSERV-RTSP-015<=STB-INSERV-RTSP-014': 0, 'STB-INSERV-RTSP-022<=STB-INSERV-RTSP-021': 0}
        
        # 命名file_in文件的列名
        columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        # 读取file_in文件
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        file_chunk['count1'] = 1
        try:
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        except ValueError:
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError:
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n > 0:
            try:
                # 总行数
                dict1['STB-INSERV-RTSP-totalnum'] = file_chunk['count1'].sum()
                # 判断条件 EPG请求时延均值(s)<=900
                dict1['STB-INSERV-RTSP-007'] = file_chunk.loc[(file_chunk[7] > 900)].count1.count()
                # 判断条件 EPG请求时延最大值(s)<=900
                dict1['STB-INSERV-RTSP-008'] = file_chunk.loc[(file_chunk[8] > 900)].count1.count()
                # 判断条件 EPG请求总次数<=1000000
                dict1['STB-INSERV-RTSP-009'] = file_chunk.loc[(file_chunk[9] > 1000000)].count1.count()
                # 判断条件 EPG请求成功次数<=1000000
                dict1['STB-INSERV-RTSP-010'] = file_chunk.loc[(file_chunk[10] > 1000000)].count1.count()
                # 判断条件 组播请求次数<=1000000
                dict1['STB-INSERV-RTSP-011'] = file_chunk.loc[(file_chunk[11] > 1000000)].count1.count()
                # 判断条件 组播请求成功次数<=1000000
                dict1['STB-INSERV-RTSP-012'] = file_chunk.loc[(file_chunk[12] > 1000000)].count1.count()
                # 判断条件 组播请求时延(s)<=900
                dict1['STB-INSERV-RTSP-013'] = file_chunk.loc[(file_chunk[13] > 900)].count1.count()
                # 判断条件 单播请求次数<=1000000
                dict1['STB-INSERV-RTSP-014'] = file_chunk.loc[(file_chunk[14] > 1000000)].count1.count()
                # 判断条件 单播请求成功次数<=1000000
                dict1['STB-INSERV-RTSP-015'] = file_chunk.loc[(file_chunk[15] > 1000000)].count1.count()
                # 判断条件 单播请求时延(s)<=900
                dict1['STB-INSERV-RTSP-016'] = file_chunk.loc[(file_chunk[16] > 900)].count1.count()
                # 判断条件 组播频道切换次数<=1000000
                dict1['STB-INSERV-RTSP-021'] = file_chunk.loc[(file_chunk[21] > 1000000)].count1.count()
                # 判断条件 组播频道切换成功次数<=1000000
                dict1['STB-INSERV-RTSP-022'] = file_chunk.loc[(file_chunk[22] > 1000000)].count1.count()
                # 判断条件 组播频道切换请求时延(s)<=1000000
                dict1['STB-INSERV-RTSP-023'] = file_chunk.loc[(file_chunk[23] > 1000000)].count1.count()
                # 判断条件 EPG请求时延均值(s)<=EPG请求时延最大值(s)
                dict1['STB-INSERV-RTSP-007<=STB-INSERV-RTSP-008'] = file_chunk.loc[
                    (file_chunk[7] > file_chunk[8])].count1.count()
                # EPG请求成功次数<=EPG请求总次数
                dict1['STB-INSERV-RTSP-010<=STB-INSERV-RTSP-009'] = file_chunk.loc[
                    (file_chunk[10] > file_chunk[9])].count1.count()
                # 组播请求成功次数<=组播请求次数
                dict1['STB-INSERV-RTSP-012<=STB-INSERV-RTSP-011'] = file_chunk.loc[
                    (file_chunk[12] > file_chunk[11])].count1.count()
                # 单播请求成功次数<=单播请求次数
                dict1['STB-INSERV-RTSP-015<=STB-INSERV-RTSP-014'] = file_chunk.loc[
                    (file_chunk[15] > file_chunk[14])].count1.count()
                # 组播频道切换成功次数<=组播频道切换次数
                dict1['STB-INSERV-RTSP-022<=STB-INSERV-RTSP-021'] = file_chunk.loc[
                    (file_chunk[22] > file_chunk[21])].count1.count()
                
                exact = pd.DataFrame([dict1])
                # 写入file_out文件
                exact.T.to_csv(file_out, sep='|', header=None)
                # 符合数值判断条件的行输出
                xx = file_chunk.loc[
                    (file_chunk[7] > 900) | (file_chunk[8] > 900) | (file_chunk[9] > 1000000) | (
                                file_chunk[10] > 1000000) |
                    (file_chunk[11] > 900) | (file_chunk[12] > 100000) | (file_chunk[13] > 900) | (
                                file_chunk[14] > 1000000) |
                    (file_chunk[15] > 1000000) | (file_chunk[16] > 900) | (file_chunk[21] > 1000000) | (
                            file_chunk[22] > 1000000) |
                    (file_chunk[23] > 1000000), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                                 21, 22,
                                                 23]].to_csv(
                    file_out + '.value', sep='|', header=None, index=False)
                # 符合逻辑判断条件的行输出
                yy = file_chunk.loc[
                    (file_chunk[7] > file_chunk[8]) | (file_chunk[10] > file_chunk[9]) | (
                                file_chunk[12] > file_chunk[11]) |
                    (file_chunk[15] > file_chunk[14]) | (file_chunk[22] > file_chunk[21]), [1, 2, 3, 4, 5, 6, 7, 8, 9,
                                                                                            10, 11,
                                                                                            12, 13, 14, 15, 16, 17, 18,
                                                                                            19, 20,
                                                                                            21, 22, 23]].to_csv(
                    file_out + '.logic', sep='|', header=None, index=False)
                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 21, 22, 23]:
                    if file_chunk[x].dtype == 'object':
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)
    
    def stb_trans(self, file_in, file_out):
        # 生成准确性校验字典字典
        dict1 = {'STB-TRANS-totalnum': 0, 'STB-TRANS-007': 0, 'STB-TRANS-008': 0, 'STB-TRANS-009': 0,
                 'STB-TRANS-010': 0,
                 'STB-TRANS-011': 0, 'STB-TRANS-012': 0, 'STB-TRANS-013': 0, 'STB-TRANS-014': 0,
                 'STB-TRANS-015': 0, 'STB-TRANS-018': 0, 'STB-TRANS-019': 0, 'STB-TRANS-020': 0, 'STB-TRANS-021': 0,
                 'STB-TRANS-022': 0, 'STB-TRANS-023': 0, 'STB-TRANS-026': 0, 'STB-TRANS-027': 0, 'STB-TRANS-028': 0,
                 'STB-TRANS-029': 0,
                 'STB-TRANS-007<=STB-TRANS-008': 0, 'STB-TRANS-009<=STB-TRANS-010': 0,
                 'STB-TRANS-011<=STB-TRANS-012': 0,
                 'STB-TRANS-013<=STB-TRANS-014': 0, 'STB-TRANS-018<=STB-TRANS-019': 0,
                 'STB-TRANS-020<=STB-TRANS-021': 0,
                 'STB-TRANS-022<=STB-TRANS-023': 0}
        
        # 命名file_in文件的列名
        columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29]
        # 读取file_in文件
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None, low_memory=False)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        file_chunk['count1'] = 1
        try:
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        except ValueError:
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError:
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n > 0:
            try:
                # 总行数
                dict1['STB-TRANS-totalnum'] = file_chunk['count1'].sum()
                # 判断条件 机顶盒下行带宽平均值(Mbps)<=1000000
                dict1['STB-TRANS-007'] = file_chunk.loc[(file_chunk[7] > 1000000)].count1.count()
                # 判断条件 机顶盒下行带宽最大值(Mbps)<=1000000
                dict1['STB-TRANS-008'] = file_chunk.loc[(file_chunk[8] > 1000000)].count1.count()
                # 判断条件 机顶盒上行带宽平均值(Mbps)<=1000000
                dict1['STB-TRANS-009'] = file_chunk.loc[file_chunk[9] > 1000000].count1.count()
                # 判断条件 机顶盒上行带宽最大值(Mbps)<=1000000
                dict1['STB-TRANS-010'] = file_chunk.loc[(file_chunk[10] > 1000000)].count1.count()
                # 判断条件 TCP重传率平均值<=100
                dict1['STB-TRANS-011'] = file_chunk.loc[(file_chunk[11] > 100)].count1.count()
                # 判断条件 TCP重传率最大值<=100
                dict1['STB-TRANS-012'] = file_chunk.loc[(file_chunk[12] > 100)].count1.count()
                # 判断条件 TCP乱序率平均值<=100
                dict1['STB-TRANS-013'] = file_chunk.loc[(file_chunk[13] > 100)].count1.count()
                # 判断条件 TCP乱序率最大值<=100
                dict1['STB-TRANS-014'] = file_chunk.loc[(file_chunk[14] > 100)].count1.count()
                # 判断条件 视频传输速率(KB/S)<=1000000
                dict1['STB-TRANS-015'] = file_chunk.loc[(file_chunk[15] > 1000000)].count1.count()
                # 判断条件 RTP丢包率平均值（RTSP UDP）<=100
                dict1['STB-TRANS-018'] = file_chunk.loc[(file_chunk[18] > 100)].count1.count()
                # 判断条件 RTP丢包率最大值（RTSP UDP）<=100
                dict1['STB-TRANS-019'] = file_chunk.loc[(file_chunk[19] > 100)].count1.count()
                # 判断条件 MDI-DF平均值（RTSP UDP）<=1000
                dict1['STB-TRANS-020'] = file_chunk.loc[(file_chunk[20] > 1000)].count1.count()
                # 判断条件 MDI-DF最大值（RTSP UDP）<=1000
                dict1['STB-TRANS-021'] = file_chunk.loc[(file_chunk[21] > 1000)].count1.count()
                # 判断条件 MDI-MLR平均值（RTSP UDP）<=100
                dict1['STB-TRANS-022'] = file_chunk.loc[(file_chunk[22] > 100)].count1.count()
                # 判断条件 MDI-MLR最大值（RTSP UDP）<=100
                dict1['STB-TRANS-023'] = file_chunk.loc[(file_chunk[23] > 100)].count1.count()
                # 判断条件 机顶盒内存占用率<=100
                dict1['STB-TRANS-026'] = file_chunk.loc[(file_chunk[26] > 100)].count1.count()
                # 判断条件 机顶盒CPU利用率峰值时长(s)<=900
                dict1['STB-TRANS-027'] = file_chunk.loc[(file_chunk[27] > 900)].count1.count()
                # 判断条件 软探针进程使用CPU利用率<=100
                dict1['STB-TRANS-028'] = file_chunk.loc[(file_chunk[28] > 100)].count1.count()
                # 判断条件 软探针进程使用内存占用率<=100
                dict1['STB-TRANS-029'] = file_chunk.loc[(file_chunk[29] > 100)].count1.count()
                # 判断条件 机顶盒下行带宽平均值(Mbps)<=机顶盒下行带宽最大值(Mbps)
                dict1['STB-TRANS-007<=STB-TRANS-008'] = file_chunk.loc[
                    (file_chunk[7] > file_chunk[8])].count1.count()
                # 机顶盒上行带宽平均值(Mbps)<=机顶盒上行带宽最大值(Mbps)
                dict1['STB-TRANS-009<=STB-TRANS-010'] = file_chunk.loc[
                    (file_chunk[9] > file_chunk[10])].count1.count()
                # TCP重传率平均值<=TCP重传率最大值
                dict1['STB-TRANS-011<=STB-TRANS-012'] = file_chunk.loc[
                    (file_chunk[11] > file_chunk[12])].count1.count()
                # TCP乱序率平均值<=TCP乱序率最大值
                dict1['STB-TRANS-013<=STB-TRANS-014'] = file_chunk.loc[
                    (file_chunk[13] > file_chunk[14])].count1.count()
                # RTP丢包率平均值（RTSP UDP）<=RTP丢包率最大值（RTSP UDP）
                dict1['STB-TRANS-018<=STB-TRANS-019'] = file_chunk.loc[
                    (file_chunk[18] > file_chunk[19])].count1.count()
                # MDI-DF平均值（RTSP UDP）<=MDI-DF最大值（RTSP UDP）
                dict1['STB-TRANS-020<=STB-TRANS-021'] = file_chunk.loc[
                    (file_chunk[20] > file_chunk[21])].count1.count()
                # MDI-MLR平均值（RTSP UDP）<=MDI-MLR最大值（RTSP UDP）
                dict1['STB-TRANS-022<=STB-TRANS-023'] = file_chunk.loc[
                    (file_chunk[22] > file_chunk[23])].count1.count()
                
                exact = pd.DataFrame([dict1])
                # 写入file_out文件
                exact.T.to_csv(file_out, sep='|', header=None)
                # 符合数值判断条件的行输出
                xx = file_chunk.loc[
                    (file_chunk[7] > 1000000) | (file_chunk[8] > 1000000) | (file_chunk[9] > 1000000) | (
                            file_chunk[10] > 1000000) | (file_chunk[11] > 100) | (file_chunk[12] > 100) | (
                            file_chunk[13] > 100) | (file_chunk[14] > 100) | (file_chunk[15] > 1000000) | (
                            file_chunk[18] > 100) | (file_chunk[19] > 100) | (file_chunk[20] > 1000) | (
                            file_chunk[21] > 1000) | (file_chunk[22] > 100) | (file_chunk[23] > 100) | (
                            file_chunk[26] > 100) | (file_chunk[27] > 900) | (file_chunk[28] > 100) | (
                            file_chunk[29] > 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                                                    17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]].to_csv(
                    file_out + '.value', sep='|', header=None, index=False)
                # 符合逻辑判断条件的行输出
                yy = file_chunk.loc[
                    (file_chunk[7] > file_chunk[8]) | (file_chunk[9] > file_chunk[10]) | (
                                file_chunk[11] > file_chunk[12]) |
                    (file_chunk[13] > file_chunk[14]) | (file_chunk[18] > file_chunk[19]) | (
                                file_chunk[20] > file_chunk[21]) |
                    (file_chunk[22] > file_chunk[23]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                                                        19, 20,
                                                        21, 22, 23, 24, 25, 26, 27, 28, 29]].to_csv(
                    file_out + '.logic', sep='|', header=None, index=False)
                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]:
                    if file_chunk[x].dtype == 'object':
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)
    
    def stb_pmview(self, file_in, file_out):
        # 生成准确性校验字典字典
        dict1 = {'STB-PMVIEW-totalnum': 0, 'STB-PMVIEW-010': 0}
        
        # 命名file_in文件的列名
        columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # 读取file_in文件
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        file_chunk['count1'] = 1
        try:
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        except ValueError:
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError:
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n > 0:
            try:
                # 总行数
                dict1['STB-PMVIEW-totalnum'] = file_chunk['count1'].sum()
                # 判断条件 观看时长(s)<=1000000
                dict1['STB-PMVIEW-010'] = file_chunk.loc[(file_chunk[10] > 900)].count1.count()
                
                exact = pd.DataFrame([dict1])
                # 写入file_out文件
                exact.T.to_csv(file_out, sep='|', header=None)
                # 符合数值判断条件的行输出
                xx = file_chunk.loc[(file_chunk[10] > 900), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]].to_csv(
                    file_out + '.value', sep='|', header=None, index=False)
                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [10]:
                    if file_chunk[x].dtype == 'object':
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)
    
    def vsource_qlt(self, file_in, file_out):
        # 生成准确性校验字典字典
        dict1 = {'VSOURCE-QLT-totalnum': 0, 'VSOURCE-QLT-007': 0, 'VSOURCE-QLT-008': 0,
                 'VSOURCE-QLT-011': 0, 'VSOURCE-QLT-012': 0, 'VSOURCE-QLT-024': 0, 'VSOURCE-QLT-025': 0,
                 'VSOURCE-QLT-026': 0,
                 'VSOURCE-QLT-027': 0, 'VSOURCE-QLT-028': 0, 'VSOURCE-QLT-029': 0, 'VSOURCE-QLT-030': 0,
                 'VSOURCE-QLT-032': 0}
        
        # 命名file_in文件的列名
        columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31, 32]
        # 读取file_in文件
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        file_chunk['count1'] = 1
        try:
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        except ValueError:
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError:
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n > 0:
            try:
                # 总行数
                dict1['VSOURCE-QLT-totalnum'] = file_chunk['count1'].sum()
                # 判断条件 视频质量（MOS值）<=5
                dict1['VSOURCE-QLT-007'] = file_chunk.loc[(file_chunk[7] > 5)].count1.count()
                # 判断条件 码率<=100
                dict1['VSOURCE-QLT-008'] = file_chunk.loc[(file_chunk[8] > 100)].count1.count()
                # 判断条件 MDI-DF<=1000
                dict1['VSOURCE-QLT-011'] = file_chunk.loc[(file_chunk[11] > 1000)].count1.count()
                # 判断条件 MDI-MLR<=100
                dict1['VSOURCE-QLT-012'] = file_chunk.loc[(file_chunk[12] > 100)].count1.count()
                # 判断条件 TS同步字节错误数<=1000000
                dict1['VSOURCE-QLT-024'] = file_chunk.loc[(file_chunk[24] > 1000000)].count1.count()
                # 判断条件 TS同步丢失错误数<=1000000
                dict1['VSOURCE-QLT-025'] = file_chunk.loc[(file_chunk[25] > 1000000)].count1.count()
                # 判断条件 传输错误数<=100
                dict1['VSOURCE-QLT-026'] = file_chunk.loc[(file_chunk[26] > 1000000)].count1.count()
                # 判断条件 CC(连续性计数)错误个数<=1000000
                dict1['VSOURCE-QLT-027'] = file_chunk.loc[(file_chunk[27] > 1000000)].count1.count()
                # 判断条件 PAT错误数<=1000000
                dict1['VSOURCE-QLT-028'] = file_chunk.loc[(file_chunk[28] > 1000000)].count1.count()
                # 判断条件 PMT错误数<=1000000
                dict1['VSOURCE-QLT-029'] = file_chunk.loc[(file_chunk[29] > 1000000)].count1.count()
                # 判断条件 PID丢失错误数<=1000000
                dict1['VSOURCE-QLT-030'] = file_chunk.loc[(file_chunk[30] > 1000000)].count1.count()
                # 判断条件 PTS错误数<=1000000
                dict1['VSOURCE-QLT-032'] = file_chunk.loc[(file_chunk[32] > 1000000)].count1.count()
                
                exact = pd.DataFrame([dict1])
                # 写入file_out文件
                exact.T.to_csv(file_out, sep='|', header=None)
                # 符合数值判断条件的行输出
                xx = file_chunk.loc[
                    (file_chunk[7] > 5) | (file_chunk[8] > 100) | (file_chunk[11] > 1000) | (file_chunk[12] > 100) | (
                            file_chunk[24] > 1000000) | (file_chunk[25] > 1000000) | (file_chunk[26] > 1000000) | (
                            file_chunk[27] > 1000000) | (file_chunk[28] > 1000000) | (file_chunk[29] > 1000000) | (
                            file_chunk[30] > 1000000) | (file_chunk[32] > 1000000), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                                                                                     12,
                                                                                     13, 14, 15, 16, 17, 18, 19, 20, 21,
                                                                                     22, 23,
                                                                                     24, 25, 26, 27,
                                                                                     28, 29, 30, 31, 32]].to_csv(
                    file_out + '.value', sep='|', header=None, index=False)
                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [7, 8, 11, 12, 24, 25, 26, 27, 28, 29, 30, 32]:
                    if file_chunk[x].dtype == 'object':
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)
    
    def iptv_link_pm(self, file_in, file_out):
        # 生成准确性校验字典字典
        dict1 = {'IPTV-LINK-PM-totalnum': 0, 'IPTV-LINK-PM-004': 0, 'IPTV-LINK-PM-005': 0,
                 'IPTV-LINK-PM-004<=IPTV-LINK-PM-005': 0}
        
        # 命名file_in文件的列名
        columns = [1, 2, 3, 4, 5]
        # 读取file_in文件
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        file_chunk['count1'] = 1
        try:
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        except ValueError:
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError:
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n > 0:
            try:
                # 总行数
                dict1['IPTV-LINK-PM-totalnum'] = file_chunk['count1'].sum()
                # 判断条件 业务平台出口流量（GB/s）<=1000000
                dict1['IPTV-LINK-PM-004'] = file_chunk.loc[(file_chunk[4] > 1000000)].count1.count()
                # 判断条件 业务平台出口配置带宽(GB)<=1000000
                dict1['IPTV-LINK-PM-005'] = file_chunk.loc[
                    (file_chunk[5] > 1000000) | (file_chunk[5] <= 0)].count1.count()
                
                # 判断条件 业务平台出口流量<=业务平台出口配置带宽
                dict1['IPTV-LINK-PM-004<=IPTV-LINK-PM-005'] = file_chunk.loc[
                    (file_chunk[4] > file_chunk[5])].count1.count()
                
                exact = pd.DataFrame([dict1])
                # 写入file_out文件
                exact.T.to_csv(file_out, sep='|', header=None)
                # 符合数值判断条件的行输出
                xx = file_chunk.loc[
                    (file_chunk[4] > 1000000) | (file_chunk[5] > 1000000) | (file_chunk[5] <= 0), [1, 2, 3, 4,
                                                                                                   5]].to_csv(
                    file_out + '.value', sep='|', header=None, index=False)
                # 符合逻辑判断条件的行输出
                yy = file_chunk.loc[
                    (file_chunk[4] > file_chunk[5]), [1, 2, 3, 4, 5]].to_csv(
                    file_out + '.logic', sep='|', header=None, index=False)
                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [4, 5]:
                    if file_chunk[x].dtype == 'object':
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)
    
    def iptv_view_pm(self, file_in, file_out):
        # 生成准确性校验字典字典
        dict1 = {'IPTV-VIEW-PM-totalnum': 0, 'IPTV-VIEW-PM-004': 0, 'IPTV-VIEW-PM-005': 0, 'IPTV-VIEW-PM-006': 0,
                 'IPTV-VIEW-PM-007': 0}
        
        # 命名file_in文件的列名
        columns = [1, 2, 3, 4, 5, 6, 7]
        # 读取file_in文件
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        file_chunk['count1'] = 1
        try:
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        except ValueError:
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError:
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n > 0:
            try:
                # 总行数
                dict1['IPTV-VIEW-PM-totalnum'] = file_chunk['count1'].sum()
                # 判断条件 用户观看总时长<=100000000
                dict1['IPTV-VIEW-PM-004'] = file_chunk.loc[(file_chunk[4] > 100000000)].count1.count()
                # 判断条件 直播观看总次数<=100000000
                dict1['IPTV-VIEW-PM-005'] = file_chunk.loc[(file_chunk[5] > 100000000)].count1.count()
                # 判断条件 点播观看总次数<=100000000
                dict1['IPTV-VIEW-PM-006'] = file_chunk.loc[(file_chunk[6] > 100000000)].count1.count()
                # 判断条件 回看观看总次数<=100000000
                dict1['IPTV-VIEW-PM-007'] = file_chunk.loc[(file_chunk[7] > 100000000)].count1.count()
                
                exact = pd.DataFrame([dict1])
                # 写入file_out文件
                exact.T.to_csv(file_out, sep='|', header=None)
                # 符合数值判断条件的行输出
                xx = file_chunk.loc[
                    (file_chunk[4] > 1000) | (file_chunk[5] > 1000000) | (file_chunk[6] > 1000000) | (
                            file_chunk[7] > 1000000), [1, 2, 3, 4, 5, 6, 7]].to_csv(
                    file_out + '.value', sep='|', header=None, index=False)
                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [4, 5, 6, 7]:
                    if file_chunk[x].dtype == 'object':
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)
    
    def iptv_user_pm(self, file_in, file_out):
        # 生成准确性校验字典字典
        dict1 = {'IPTV-USER-PM-totalnum': 0, 'IPTV-USER-PM-004': 0, 'IPTV-USER-PM-005': 0, 'IPTV-USER-PM-006': 0,
                 'IPTV-USER-PM-007': 0, 'IPTV-USER-PM-004<=IPTV-USER-PM-007': 0, 'IPTV-USER-PM-005<=IPTV-USER-PM-007': 0
            , 'IPTV-USER-PM-006<=IPTV-USER-PM-007': 0}
        
        # 命名file_in文件的列名
        columns = [1, 2, 3, 4, 5, 6, 7]
        # 读取file_in文件
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        file_chunk['count1'] = 1
        try:
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        except ValueError:
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError:
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n > 0:
            try:
                # 总行数
                dict1['IPTV-USER-PM-totalnum'] = file_chunk['count1'].sum()
                # 判断条件 实装用户<=1000000
                dict1['IPTV-USER-PM-004'] = file_chunk.loc[(file_chunk[4] > 1000000)].count1.count()
                # 判断条件 开户用户数<=1000000
                dict1['IPTV-USER-PM-005'] = file_chunk.loc[(file_chunk[5] > 1000000)].count1.count()
                # 判断条件 退网用户数<=1000000
                dict1['IPTV-USER-PM-006'] = file_chunk.loc[(file_chunk[6] > 1000000)].count1.count()
                # 判断条件 0<开户用户数总数<=1000000
                dict1['IPTV-USER-PM-007'] = file_chunk.loc[
                    (file_chunk[7] > 1000000) | (file_chunk[7] <= 0)].count1.count()
                # 判断条件 实装用户<=开户用户数总数
                dict1['IPTV-USER-PM-004<=IPTV-USER-PM-007'] = file_chunk.loc[
                    (file_chunk[4] > file_chunk[7])].count1.count()
                # 判断条件 开户用户数<=开户用户数总数
                dict1['IPTV-USER-PM-005<=IPTV-USER-PM-007'] = file_chunk.loc[
                    (file_chunk[5] > file_chunk[7])].count1.count()
                # 判断条件 退网用户数<=开户用户数总数
                dict1['IPTV-USER-PM-006<=IPTV-USER-PM-007'] = file_chunk.loc[
                    (file_chunk[6] > file_chunk[7])].count1.count()
                exact = pd.DataFrame([dict1])
                # 写入file_out文件
                exact.T.to_csv(file_out, sep='|', header=None)
                # 符合数值判断条件的行输出
                xx = file_chunk.loc[
                    (file_chunk[4] > 1000000) | (file_chunk[5] > 1000000) | (file_chunk[6] > 1000000) | (
                            file_chunk[7] > 1000000) | (file_chunk[7] <= 0), [1, 2, 3, 4, 5, 6, 7]].to_csv(
                    file_out + '.value', sep='|', header=None, index=False)
                yy = file_chunk.loc[
                    (file_chunk[4] > file_chunk[7]) | (file_chunk[5] > file_chunk[7]) | (
                                file_chunk[6] > file_chunk[7]), [1, 2,
                                                                 3, 4,
                                                                 5, 6,
                                                                 7]].to_csv(
                    file_out + '.logic', sep='|', header=None, index=False)
                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [4, 5, 6, 7]:
                    if file_chunk[x].dtype == 'object':
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)
    
    def user_vtime(self, file_in, file_out):
        # 生成准确性校验字典字典
        dict1 = {'USER-VTIME-totalnum': 0, 'USER-VTIME-004': 0, 'USER-VTIME-005': 0, 'USER-VTIME-006': 0,
                 'USER-VTIME-005<=USER-VTIME-004': 0, 'USER-VTIME-006<=USER-VTIME-004': 0}
        
        # 命名file_in文件的列名
        columns = [1, 2, 3, 4, 5, 6]
        # 读取file_in文件
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        file_chunk['count1'] = 1
        try:
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        except ValueError:
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError:
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n > 0:
            try:
                # 总行数
                dict1['USER-VTIME-totalnum'] = file_chunk['count1'].sum()
                # 判断条件 监控总数<=1000000
                dict1['USER-VTIME-004'] = file_chunk.loc[
                    (file_chunk[4] > 1000000) | (file_chunk[4] <= 0)].count1.count()
                # 判断条件 当日/月登陆用户数<=1000000
                dict1['USER-VTIME-005'] = file_chunk.loc[(file_chunk[5] > 1000000)].count1.count()
                # 判断条件 当日/月活跃用户数<=1000000
                dict1['USER-VTIME-006'] = file_chunk.loc[(file_chunk[6] > 1000000)].count1.count()
                # 判断条件 开户用户数<=开户用户数总数
                dict1['USER-VTIME-005<=USER-VTIME-004'] = file_chunk.loc[
                    (file_chunk[5] > file_chunk[4])].count1.count()
                # 判断条件 退网用户数<=开户用户数总数
                dict1['USER-VTIME-006<=USER-VTIME-004'] = file_chunk.loc[
                    (file_chunk[6] > file_chunk[4])].count1.count()
                exact = pd.DataFrame([dict1])
                # 写入file_out文件
                exact.T.to_csv(file_out, sep='|', header=None)
                # 符合数值判断条件的行输出
                xx = file_chunk.loc[
                    (file_chunk[4] > 1000000) | (file_chunk[5] > 1000000) | (file_chunk[6] > 1000000) | (
                                file_chunk[4] <= 0), [
                        1, 2, 3, 4, 5, 6]].to_csv(
                    file_out + '.value', sep='|', header=None, index=False)
                yy = file_chunk.loc[
                    (file_chunk[5] > file_chunk[4]) | (file_chunk[6] > file_chunk[4]), [1, 2,
                                                                                        3, 4,
                                                                                        5, 6]].to_csv(
                    file_out + '.logic', sep='|', header=None, index=False)
                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [4, 5, 6]:
                    if file_chunk[x].dtype == 'object':
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)

    def stb_pm_vmos(self, file_in, file_out):
        # 生成准确性校验字典字典
        dict1 = {'STB-PM-VMOS-totalnum': 0, 'STB-PM-VMOS-006': 0, 'STB-PM-VMOS-007': 0}
    
        # 命名file_in文件的列名
        columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # 读取file_in文件
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        file_chunk['count1'] = 1
        try:
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        except ValueError:
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError:
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n > 0:
            try:
                # 总行数
                dict1['STB-PM-VMOS-totalnum'] = file_chunk['count1'].sum()

                dict1['STB-PM-VMOS-006'] = file_chunk.loc[(file_chunk[6] > 1000000)].count1.count()

                dict1['STB-PM-VMOS-007'] = file_chunk.loc[(file_chunk[7] > 900)].count1.count()


                exact = pd.DataFrame([dict1])
                # 写入file_out文件
                exact.T.to_csv(file_out, sep='|', header=None)
                # 符合数值判断条件的行输出
                xx = file_chunk.loc[
                    (file_chunk[6] > 1000000) | (file_chunk[7] > 900), [
                        1, 2, 3, 4, 5, 6, 7, 8, 9, 10]].to_csv(
                    file_out + '.value', sep='|', header=None, index=False)
                
                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [6, 7]:
                    if file_chunk[x].dtype == 'object':
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)

    def stb_inserv_http(self, file_in, file_out):
        # 生成准确性校验字典字典
        dict1 = {'STB-INSERV-HTTP-totalnum': 0, 'STB-INSERV-HTTP-011': 0, 'STB-INSERV-HTTP-012': 0,
                 'STB-INSERV-HTTP-014': 0, 'STB-INSERV-HTTP-015': 0, 'STB-INSERV-HTTP-016': 0, 'STB-INSERV-HTTP-017': 0,
                 'STB-INSERV-HTTP-012<=STB-INSERV-HTTP-011': 0, 'STB-INSERV-HTTP-015<=STB-INSERV-HTTP-014': 0,
                 'STB-INSERV-HTTP-016<=STB-INSERV-HTTP-017': 0}
    
        # 命名file_in文件的列名
        columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        # 读取file_in文件
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        file_chunk['count1'] = 1
        try:
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        except ValueError:
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError:
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n > 0:
            try:
                # 总行数
                dict1['STB-INSERV-HTTP-totalnum'] = file_chunk['count1'].sum()
                # 判断条件 监控总数<=1000000
                dict1['STB-INSERV-HTTP-011'] = file_chunk.loc[(file_chunk[11] > 900)].count1.count()
                # 判断条件 当日/月登陆用户数<=1000000
                dict1['STB-INSERV-HTTP-012'] = file_chunk.loc[(file_chunk[12] > 900)].count1.count()
                # 判断条件 当日/月活跃用户数<=1000000
                dict1['STB-INSERV-HTTP-014'] = file_chunk.loc[(file_chunk[14] > 1000000)].count1.count()
                dict1['STB-INSERV-HTTP-015'] = file_chunk.loc[(file_chunk[15] > 1000000)].count1.count()
                dict1['STB-INSERV-HTTP-016'] = file_chunk.loc[(file_chunk[16] > 900)].count1.count()
                dict1['STB-INSERV-HTTP-017'] = file_chunk.loc[(file_chunk[17] > 900)].count1.count()
                # 判断条件 开户用户数<=开户用户数总数
                dict1['STB-INSERV-HTTP-015<=STB-INSERV-HTTP-014'] = file_chunk.loc[
                    (file_chunk[15] > file_chunk[14])].count1.count()
                # 判断条件 退网用户数<=开户用户数总数
                dict1['STB-INSERV-HTTP-016<=STB-INSERV-HTTP-017'] = file_chunk.loc[
                    (file_chunk[16] > file_chunk[17])].count1.count()
                dict1['STB-INSERV-HTTP-012<=STB-INSERV-HTTP-011'] = file_chunk.loc[
                    (file_chunk[12] > file_chunk[11])].count1.count()
                exact = pd.DataFrame([dict1])
                # 写入file_out文件
                exact.T.to_csv(file_out, sep='|', header=None)
                # 符合数值判断条件的行输出
                xx = file_chunk.loc[
                    (file_chunk[11] > 900) | (file_chunk[12] > 900) | (file_chunk[14] > 1000000) | (
                                file_chunk[15] > 1000000) | (file_chunk[16] > 900) | (file_chunk[17] > 900)
                    , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]].to_csv(
                    file_out + '.value', sep='|', header=None, index=False)
                yy = file_chunk.loc[
                    (file_chunk[15] > file_chunk[14]) | (file_chunk[16] > file_chunk[17]) | (
                                file_chunk[12] > file_chunk[11]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                                                                   16, 17]].to_csv(
                    file_out + '.logic', sep='|', header=None, index=False)
                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [11, 12, 14, 15, 16, 17]:
                    if file_chunk[x].dtype == 'object':
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)

    def stb_mos(self, file_in, file_out):
        # 生成准确性校验字典字典
        # dict1 = {'STB-MOS-totalnum': 0, 'STB-MOS-006': 0, 'STB-MOS-007': 0,
        #          'STB-MOS-008': 0, 'STB-MOS-009': 0, 'STB-MOS-010': 0, 'STB-MOS-011': 0,'STB-MOS-012': 0,
        #          'STB-MOS-006<=STB-MOS-007': 0, 'STB-MOS-008<=STB-MOS-006': 0,
        #          'STB-MOS-009<=STB-MOS-010': 0, 'STB-MOS-011<=STB-MOS-009': 0}
        dict1 = {'STB-MOS-totalnum': 0, 'STB-MOS-006': 0, 'STB-MOS-007': 0,
                          'STB-MOS-008': 0, 'STB-MOS-009': 0, 'STB-MOS-010': 0, 'STB-MOS-011': 0,'STB-MOS-012': 0,}
        
        # 命名file_in文件的列名
        columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        # 读取file_in文件
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        file_chunk['count1'] = 1
        try:
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        except ValueError:
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError:
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n > 0:
            try:
                # 总行数
                dict1['STB-MOS-totalnum'] = file_chunk['count1'].sum()
                # 判断条件 监控总数<=1000000
                dict1['STB-MOS-006'] = file_chunk.loc[(file_chunk[6] > 5)].count1.count()
                # 判断条件 当日/月登陆用户数<=1000000
                dict1['STB-MOS-007'] = file_chunk.loc[(file_chunk[7] > 5)].count1.count()
                # 判断条件 当日/月活跃用户数<=1000000
                dict1['STB-MOS-008'] = file_chunk.loc[(file_chunk[8] > 5)].count1.count()
                dict1['STB-MOS-009'] = file_chunk.loc[(file_chunk[9] > 5)].count1.count()
                dict1['STB-MOS-010'] = file_chunk.loc[(file_chunk[10] > 5)].count1.count()
                dict1['STB-MOS-011'] = file_chunk.loc[(file_chunk[11] > 5)].count1.count()
                dict1['STB-MOS-012'] = file_chunk.loc[(file_chunk[12] > 900)].count1.count()
                # 判断条件 开户用户数<=开户用户数总数
                # dict1['STB-MOS-006<=STB-MOS-007'] = file_chunk.loc[
                #     (file_chunk[6] > file_chunk[7])].count1.count()
                # 判断条件 退网用户数<=开户用户数总数
                # dict1['STB-MOS-008<=STB-MOS-006'] = file_chunk.loc[
                #     (file_chunk[8] > file_chunk[6])].count1.count()
                # dict1['STB-MOS-009<=STB-MOS-010'] = file_chunk.loc[
                #     (file_chunk[9] > file_chunk[10])].count1.count()
                # dict1['STB-MOS-011<=STB-MOS-009'] = file_chunk.loc[
                #     (file_chunk[11] > file_chunk[9])].count1.count()
                exact = pd.DataFrame([dict1])
                # 写入file_out文件
                exact.T.to_csv(file_out, sep='|', header=None)
                # 符合数值判断条件的行输出
                xx = file_chunk.loc[
                    (file_chunk[6] > 5) | (file_chunk[7] > 5) |(file_chunk[8] > 5) | (file_chunk[9] > 5) | (file_chunk[10] > 5) | (file_chunk[11] > 5)
                    |(file_chunk[12] > 900), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]].to_csv(
                    file_out + '.value', sep='|', header=None, index=False)
                # yy = file_chunk.loc[
                #     (file_chunk[6] > file_chunk[7]) | (file_chunk[8] > file_chunk[6]) | (file_chunk[9] > file_chunk[10])|
                #     (file_chunk[11] > file_chunk[9]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]].to_csv(
                #     file_out + '.logic', sep='|', header=None, index=False)
                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [6, 7, 8, 9, 10, 11, 12]:
                    if file_chunk[x].dtype == 'object':
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)

    def iptv_liveava(self, file_in, file_out):
        # 生成准确性校验字典字典
        dict1 = {'IPTV-LIVEAVA-totalnum': 0, 'IPTV-LIVEAVA-004': 0, 'IPTV-LIVEAVA-005': 0,
                 'IPTV-LIVEAVA-006': 0,'IPTV-LIVEAVA-005<=IPTV-LIVEAVA-004': 0, 'IPTV-LIVEAVA-006<=IPTV-LIVEAVA-004': 0}
    
        # 命名file_in文件的列名
        columns = [1, 2, 3, 4, 5, 6]
        # 读取file_in文件
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        file_chunk['count1'] = 1
        try:
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        except ValueError:
            file_chunk[2] = file_chunk[2].str.replace("[^\d]+", "0")
            file_chunk[2] = file_chunk[2].astype(int)
            file_chunk[2] = file_chunk[2].fillna(0).astype(int)
        try:
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        except ValueError:
            file_chunk[3] = file_chunk[3].str.replace("[^\d]+", "0")
            file_chunk[3] = file_chunk[3].astype(int)
            file_chunk[3] = file_chunk[3].fillna(0).astype(int)
        n = 2
        while n > 0:
            try:
                # 总行数
                dict1['IPTV-LIVEAVA-totalnum'] = file_chunk['count1'].sum()
                # 判断条件 监控总数<=1000000
                dict1['IPTV-LIVEAVA-004'] = file_chunk.loc[(file_chunk[4] > 1000000)].count1.count()
                # 判断条件 当日/月登陆用户数<=1000000
                dict1['IPTV-LIVEAVA-005'] = file_chunk.loc[(file_chunk[5] > 1000000)].count1.count()
                # 判断条件 当日/月活跃用户数<=1000000
                dict1['IPTV-LIVEAVA-006'] = file_chunk.loc[(file_chunk[6] > 1000000)].count1.count()
            
                # 判断条件 开户用户数<=开户用户数总数
                dict1['IPTV-LIVEAVA-005<=IPTV-LIVEAVA-004'] = file_chunk.loc[
                    (file_chunk[5] > file_chunk[4])].count1.count()
                # 判断条件 退网用户数<=开户用户数总数
                dict1['IPTV-LIVEAVA-006<=IPTV-LIVEAVA-004'] = file_chunk.loc[
                    (file_chunk[6] > file_chunk[4])].count1.count()
                
                exact = pd.DataFrame([dict1])
                # 写入file_out文件
                exact.T.to_csv(file_out, sep='|', header=None)
                # 符合数值判断条件的行输出
                xx = file_chunk.loc[
                    (file_chunk[4] > 1000000)|(file_chunk[5] > 1000000)|(file_chunk[6] > 1000000), [1, 2, 3, 4, 5, 6]].to_csv(
                    file_out + '.value', sep='|', header=None, index=False)
                yy = file_chunk.loc[
                    (file_chunk[5] > file_chunk[4]) | (file_chunk[6] > file_chunk[4]), [1, 2, 3, 4, 5, 6]].to_csv(
                    file_out + '.logic', sep='|', header=None, index=False)
                n -= 2
            except TypeError:
                n -= 1
                print('程序报错，进行数据清洗')
                for x in [4, 5, 6]:
                    if file_chunk[x].dtype == 'object':
                        file_chunk[x] = file_chunk[x].str.replace("[^\d.]+", "0")
                        file_chunk[x] = file_chunk[x].str.replace("^\.+", "0")
                        file_chunk[x] = file_chunk[x].astype(float)
