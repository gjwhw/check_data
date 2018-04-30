# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import sys
import shutil
import data_path as data
import city
import datetime
import chkdef


starttime= datetime.datetime.now()
print('开始时间')
print(starttime)


#定义参数
# 穿入四个参数 如 python data_chk.py  CDN-PM.txt  CDN-PM  cdn_pm 20180306 LN
file_path = sys.argv[1]       #原始文件路径  CDN-PM.txt
type2 = sys.argv[2]           #指标名称      CDN-PM
func_name  = sys.argv[3]      #调用验证函数名称   cdn-pm
day = sys.argv[4]             #输入日期      20180306
province = sys.argv[5]        #输入省份大写   LN
# file_path = 'STB-PM-VMOS.txt'
# type2 = 'STB-PM-VMOS'
# func_name = 'stb_pm_vmos'
# day = '20180305'
# province = 'HEN'

path_error,path_log,data_type =data.path(type2,day,province)       #返回错误文件路径，正确文件路径，数据类型
p = city.Province()
city_error = getattr(p,province)()                     #地区编号字典     1
city_valid = city_error.copy()

# 路径判断
if not os.path.isdir(path_error):
    os.makedirs(path_error)
if not os.path.isdir(path_log):
    os.makedirs(path_log)


# 调取文件第一行数据，文件命名
with open(file_path) as file_1:
    line = file_1.readline()
    line = line.split('|')
    filename_log = line[1] + '-' + day + '-' + data_type + '.log'       #日志文件名‘省-日期-数据类型,log’
    filename_error = line[1] + '-' + day + '-' + data_type + '.error'   #错误文件名‘省-日期-数据类型.error’





# 主程序开始
# file_valid = {}
# file_error = {}
file_error = open((path_error + filename_error), 'w')
# file_valid = open((file_path+'.valid'), 'w')
with open(file_path) as file_1:
    c = chkdef.Check()
    num_valid,num_error = getattr(c, func_name)(file_1,file_error,city_error,city_valid)

file_error.close()
# file_valid.close()
# 主程序结束


# 省日志功能
file_log = open((path_log+ 'province-'+ filename_log),'w')
# 日志内容“日期|省份|数据类型|正常数据条数|异常数据条数|合计条数”
log = (line[0][:10] + '|' + line[1] + '|'+ data_type + '|' + str(num_valid) + '|'
       + str(num_error) + '|' + str(num_valid+num_error)+'\n')
file_log.write(log) # 写入日志文件
print('省日志')
print('日期|省份|数据类型|正常数据条数|异常数据条数|合计条数')
print(log)
file_log.close()
# 省日志功能结束

# 地区日志功能
file_log = open((path_log + 'city-' + filename_log),'w')
print('地市日志')
print('日期|省份|地区|数据类型|正常数据条数|异常数据条数|合计条数')
for x in city_error.keys():
        num_error = city_error[x]
        num_valid = city_valid[x]
# 日志内容“日期|省份|地区|数据类型|正常数据条数|异常数据条数|合计条数”
        log = (line[0][:10] + '|' + line[1] +'|'+ str(x) + '|' + data_type + '|' + str(num_valid) + '|'
                 + str(num_error) + '|' + str(num_valid + num_error) + '\n')
        file_log.write(log)   # 写入日志文件
        print(log)
        
file_log.close()
# 地区日志生成结束

# 处理后的准确数据覆盖源文件
# os.unlink(file_path+'.valid')
# shutil.move( file_path+'.valid' , file_path)

'''
#判断是否存在错误数据，如无错误数据则删除文件
file_null = open(sys.argv[2], 'r').read()
if len(file_null) == 0:
    os.unlink(sys.argv[2])
'''
endtime = datetime.datetime.now()
print('运行时间')
print(endtime - starttime)








