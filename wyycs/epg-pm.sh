#!/bin/bash
# source /home/aiuap_cj/wyycs/conf/ftp.conf
# source /home/aiuap_cj/wyycs/conf/db.conf
#指标数据备份 每天定时备份前一天上报的指标数据
echo "数据备份开始！$(date)"
basepath="$(cd `dirname $0`;pwd)/"
echo $basepath

fileday="`date -d '5 min ago' '+%Y%m%d'`"
filemin="`date -d '5 min ago' '+%Y%m%d%H%M'`"
# fileday="20180503"
# filemin="20180503"
bakfilepath="/opt/ftp"
pythonpath="/home/hnxtjc/wyycs/data_treating"
datatype="packet1"

for  firmname in xtjc 
do

cp $bakfilepath/$firmname/$datatype/$fileday/*$filemin*.txt .
# u='IPTV_CDN_STORAGE_INFO'
# p='IPTV_CDN_STORAGE_INFO$#@0801'

# echo $fileday
# ftp -n <<- EOF
# open 10.254.203.198 9021
# user $u $p 

# bin
# prompt off
# mget *$filehuor*.txt
# bye
# EOF

done
for file in `ls -l|grep $filemin`
do
if [ -f $file ];then
cat $file >> ${basepath}${datatype}.txt
rm -rf $file
fi
done


#添加python处理脚本

# datatype_p=$(echo $datatype |tr '[A-Z]''[a-z]'|awk 'gsub(/-/,"_")')
# echo $datatype_p
tablename1="report_epg"
tablename2="epg"
databasename="iptv_test"
python3 ${pythonpath}/data_treating.py ${basepath}${datatype}.txt ${basepath}${datatype}_out.txt $datatype
#插入数据库
hostname="111.203.211.16"
port="3306"
username="hnxtjc"
password="hnxtjc@123."
mysql -h$hostname -P$port -u$username -vv -p$password <<EOF

use $databasename
LOAD DATA local INFILE "${basepath}${datatype}.txt"
IGNORE INTO TABLE $tablename1 
CHARACTER SET utf8
FIELDS TERMINATED BY "|" 
LINES TERMINATED BY "\\n"
(
        reportTime,
        firmName,
        stbType,
        stbID,
        epgServerIp,
        requestStartTime,     
        requestEndTime,
        requesSuccessSign
);
LOAD DATA local INFILE "${basepath}${datatype}_out.txt"
IGNORE INTO TABLE $tablename2 
CHARACTER SET utf8
FIELDS TERMINATED BY "|" 
LINES TERMINATED BY "\\n"
(
        firmName,
        stbType,
        stbID,
        epgServerIp,
        startTime,
        endTime,
        EPGResquestAvgTime,     
        EPGRequestMaxTime,
        EPGRequestTotal,
        EPGRequestSuccssNum
);
EOF
rm -rf ${basepath}${datatype}.txt
rm -rf ${basepath}${datatype}_out.txt
echo "数据备份结束！$(date)"
                                                    
