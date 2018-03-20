# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import sys
import shutil
import datetime
import city
import chkdef

starttime= datetime.datetime.now()
print '开始时间'
print starttime


#定义参数  python CDN-PM.txt cdn_pm
file_path = sys.argv[1]
func_name  = sys.argv[2]
province = sys.argv[3]
p = city.Province()
city_error = getattr(p,province)()
# path_error,path_log,data_type =data.path(type2)   #返回错误文件路径，正确文件路径，数据类型
# city_error = city.LN.copy()                     #地区编号字典     1
# city_valid = city.LN.copy()

# 路径判断
# if not os.path.isdir(path_error):
#     os.makedirs(path_error)
# if not os.path.isdir(path_log):
#     os.makedirs(path_log)


# 调取文件第一行数据，文件命名
# with open(file_path) as file_1:
#     line = file_1.readline()
#     line = line.split('|')
    # filename_log = line[1] + '-' + line[0][:10] + '-' + data_type + '.log'       #日志文件名‘省-日期-数据类型,log’
    # filename_error = line[1] + '-' + line[0][:10] + '-' + data_type + '.error'   #错误文件名‘省-日期-数据类型.error’





# 主程序开始
# file_valid = {}
# file_error = {}
# file_error = open((path_error + filename_error), 'w')
file_valid = open((file_path+'.valid'), 'w')
with open(file_path) as file_1:
    c = chkdef.Check()
    num_valid , num_error = getattr(c, func_name)(file_1,file_valid,city_error)

# file_error.close()
file_valid.close()
# 主程序结束


# 省日志功能
# file_log = open((path_log + filename_log),'w')
# 日志内容“日期|省份|数据类型|正常数据条数|异常数据条数|合计条数”
log = ('正确：'+ str(num_valid) + '\n'+'错误：'+ str(num_error) + '\n'+'合计：'+ str(num_valid+num_error))
print log
# file_log.write(log)                            # 写入日志文件
# file_log.close()
# 省日志功能结束
'''
# 地区日志功能
file_log = open((path_log + 'city-' + filename_log),'a')
for x in city_error.keys():
        num_error = city_error[x]
        num_valid = city_valid[x]
# 日志内容“日期|省份|地区|数据类型|正常数据条数|异常数据条数|合计条数”
        log = (line[0][:10] + '|' + line[1] +'|'+ str(x) + '|' + data_type + '|' + str(num_valid) + '|'
                 + str(num_error) + '|' + str(num_valid + num_error) + '\n')
        file_log.write(log)                            # 写入日志文件
file_log.close()
# 地区日志生成结束
'''
# 处理后的准确数据覆盖源文件
os.unlink(file_path)
shutil.move( file_path+'.valid' , file_path)

'''
#判断是否存在错误数据，如无错误数据则删除文件
file_null = open(sys.argv[2], 'r').read()
if len(file_null) == 0:
    os.unlink(sys.argv[2])
'''
endtime = datetime.datetime.now()
print '运行时间'
print(endtime - starttime)








