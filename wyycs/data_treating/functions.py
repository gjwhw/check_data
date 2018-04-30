#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2018/4/17 11:52
# @Auther   :GJW
# @File     :functions.py
# @Software :PyCharm
import pandas as pd
class Treating:
    def packet2(self,file_in, file_out):
        columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18','19',
                   '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36','37',
                   '38', '39', '40', '41', '42', '43', '44', '45', '46']
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        file_chunk = file.get_chunk()
        file_chunk = file_chunk.fillna({'2': 0, '3': 0, '4': 0, '5': 0, '41': 0, '43': 0})
        grouped = file_chunk.groupby(['2', '3', '4', '5', '41', '43'])
        # file_chunk['1'] = file_chunk['1'].astype('str').str[:11]
        func = {'1':['min','max'], '6':'max','7':'max','8':'max','9':'max','10':'max','11':'max','12':'max','13': 'sum', '14': 'sum', '15': 'mean',
                '16': 'max', '17': 'sum', '18': 'mean', '19': 'mean','22': 'sum','23': 'sum', '24': ['mean', 'max'],
                '25': ['mean', 'max'], '26': ['mean', 'max'], '27': ['mean', 'max'], '28': 'mean', '29': 'mean','30': 'sum',
                '31': 'sum', '32': ['mean', 'max'],'33': ['mean', 'max'], '34': ['mean', 'max'], '35': 'sum', '36': 'sum',
                '37': 'sum', '38': 'sum','39': 'sum', '40': 'sum', '42': ['max', 'mean'],'44': 'sum', '45': 'sum', '46': ['mean', 'max']}
        # func = {'32': ['mean','max']}
        x = grouped.agg(func)
        x.to_csv(file_out, sep='|', header=None, float_format='%.6f')
        
    def packet1(self,file_in, file_out):
        columns = ['1', '2', '3', '4', '5', '6', '7', '8']
        file = pd.read_csv(file_in, iterator=True, names=columns, sep='|', header=None)
        file_chunk = file.get_chunk()
        file_chunk = file_chunk.fillna({'2': 0, '3': 0, '4': 0, '5': 0})
        grouped = file_chunk.groupby(['2', '3', '4', '5'])
        # file_chunk['1'] = file_chunk['1'].astype('str').str[:11]
        file_chunk['timeout'] = file_chunk['7'] - file_chunk['6']
        # file_chunk['mun'] = file_chunk['8'].count()
        func = {'1':['min','max'], 'timeout':['mean', 'max'], '8':['count','sum']}
        x = grouped.agg(func)
        x.to_csv(file_out, sep='|', header=None, float_format='%.6f')