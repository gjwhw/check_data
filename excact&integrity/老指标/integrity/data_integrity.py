#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2018/4/17 11:52
# @Auther   :GJW
# @File     :functions.py
# @Software :PyCharm
import pandas as pd
class Test:
    def dict_data(self, datatype):
        # 各个指标对应大写指标以及含有指标项的个数的字典如：{'epg_pm': ['EPG-PM', 10]}
        dict_data = {'epg_pm': ['EPG-PM', 10], 'cdn_pm': ['CDN-PM', 11], 'stb_cm': ['STB-CM', 13],'stb_pm_opers': ['STB-PM-OPERS', 39],
                     'stb_pm_vmos': ['STB-PM-VMOS', 18], 'users_info': ['USERS-INFO', 5], 'nsccs_pm': ['NSCCS-PM', 6],'csss_pm1': ['CSSS-PM1', 7],
                     'csss_pm2': ['CSSS-PM2', 6], 'cdn_link_pm': ['CDN-LINK-PM', 7], 'iptv_link_pm': ['IPTV-LINK-PM', 7]}
        # 指标对应大写 EPG-PM'
        type_name = dict_data[datatype][0]
        # 指标含指标项个数 10
        type_num = dict_data[datatype][1]
        # 指标项后缀
        list_num = ['-001', '-002', '-003', '-004', '-005', '-006', '-007', '-008', '-009', '-010', '-011', '-012', '-013','-014', '-015', '-016', '-017',
                    '-018', '-019', '-020', '-021', '-022', '-023', '-024', '-025', '-026', '-027', '-028', '-029', '-030', '-031', '-032', '-033', '-034',
                    '-035', '-036', '-037', '-038', '-039']
        # 建立空列表，合成后使用
        list_type = []
        n = 1
        for x in list_num:
            if n <= type_num:
                list_type.append(type_name + x)
            n += 1
        return list_type
        
        
    def wanzheng(self, file_in, file_out, datatype ):
        # 读取对应指标的命名列表[EPG-PM-001,EPG-PM-002,EPG-PM-003.....]
        list_type = Test.dict_data(self,datatype)
        dict1 = dict.fromkeys(list_type,0)
        file = pd.read_csv(file_in, iterator=True, names=list_type, sep='|', header=None)
        # 转化成DF格式
        file_chunk = file.get_chunk()
        # 迭代判断每一列非空的值，如果大于0则赋值1，其他赋值0
        for x in list_type:
            dict1[x] = 1 if file_chunk[x].count() > 0 else 0
        # 将字典写入DF格式
        df = pd.DataFrame([dict1])
        # 转置导出
        # df.T.to_csv(file_out, sep='|', header=None, index=False)
        df.T.to_csv(file_out, sep='|', header=None)






