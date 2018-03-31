#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2018/3/27 8:52
# @Auther   :GJW
# @File     :weixin.py
# @Software :PyCharm
# 123

import itchat
import matplotlib.pyplot as plt
import datetime
import pygal

# 变量定义
today = datetime.date.today()

# today = time.strftime("%Y-%m-%d", time.localtime()) + '.png'
yesterday = today - datetime.timedelta(days=1)
filename = 'finishing_rate.txt'

province = {125:['河南',96,96,1,1,1,96,96,1,1,96,96],101:['北京',192,192,1,1,1,96,96,1,1,96,96],115:['黑龙江',96,96,1,1,1,96,96,1,1,96,96],
            113:['天津',96,96,1,1,1,96,96,1,1,96,96],128:['山西',192,192,1,1,1,96,96,1,1,96,96],104:['重庆',96,96,1,1,1,96,96,1,1,96,96],
            122:['山东',96,96,1,1,1,96,96,1,1,96,96],112:['江西',96,96,1,1,1,96,96,1,1,96,96],114:['吉林',96,96,1,1,1,96,96,1,1,96,96],
            127:['河北',96,96,1,1,1,96,96,1,1,96,96],124:['内蒙',96,96,1,1,1,96,96,1,1,96,96],116:['辽宁',96,96,1,1,1,96,96,1,1,96,96]}
result = {'河南':0,'北京':0,'黑龙江':0,'天津':0,'山西':0,'重庆':0,'山东':0,'江西':0,'吉林':0,'河北':0,'内蒙':0,'辽宁':0}
with open('finishing_rate.txt') as file_rate:
    for everyline in file_rate:
        result2 = []
        line = everyline.split('|')
        code = int(line[2])
        province1 = province[code][0]
        n = 0
        while n <= 10:
            right = province[code][1+n]
            now = int(line[4+n])
            result1 = round(now/right * 100,2)

            n += 1
            result2.append(result1)
            result[province1] = sum(result2)/len(result2)


# 可视化图像生成部分

plt.rcParams['font.sans-serif'] = ['SimHei'] #正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False   #正常显示负号
# 读取文件，得到省份以及完成率
province = []
finishing_rate = []
for key,value in result.items():
    province.append(key)
    finishing_rate.append(value)
        
plt.style.use("ggplot")
# 生成柱状图
plt.bar(province, finishing_rate, facecolor = '#00bff3', edgecolor = 'white')
#使用text显示数值
for a,b in zip(province,finishing_rate):
    plt.text(a, b, '%.2f' % b, ha='center', va= 'bottom',fontsize=11)
# x轴纵向显示
plt.xticks(rotation=90)
# 各种标题命名
plt.title(u"数据上报完整性日报(算法解释：sum(单个指标完整率)/指标数量)", fontsize=10)
plt.xlabel(str(yesterday), fontsize=10)
plt.ylabel(u"完整率(%)", fontsize=15)
plt.tick_params(labelsize=10)
# 自动设置图片大小，让标签在画布内
plt.tight_layout()
# 保存文件
plt.savefig(str(today))

png = str(today)+'.png'

# 微信发送部分
def lc():
    print("Finash Login!")
def ec():
    print("exit")
itchat.auto_login(hotReload=True,loginCallback=lc, exitCallback=ec)

to_someone = ['中原妙笔作文','肖项杰']
for people in to_someone:
    users = itchat.search_friends(name=people)
    usersName = users[0]['UserName']
    itchat.send_image(png,toUserName=usersName)
