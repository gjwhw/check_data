#!/bin/bash
source /home/aiuap_cj/conf/ftp.conf
#指标数据备份 每天定时备份前一天上报的指标数据
echo "数据备份开始！$(date)"
basepath="$(cd `dirname $0`;pwd)/"
echo $basepath

#province="HEN"
#firmname="LTXTJC"
#fileday="`date -d '1 day ago' '+%Y%m%d'`"
fileday="20180316"
#datatype="STB-EPG"
bakfilepath="/home/aiuap_cj/iptv"
pythonpath="home/aiuap_cj/data_treating"
#mkdir -p $bakfilepath
#HUAWEI厂家指标数据备份
for datatype in STB-EPG STB-TRANS STB-RTSP STB-HTTP VIDEO-BASE VIDEO-FPS VIDEO-QLT
do
for  firmname in HUAWEI ZTE CERTUS XTJC
do
        for stbmodel in `ls $bakfilepath/$firmname -1`
                do
                cp $bakfilepath/$firmname/$stbmodel/$datatype/$fileday/*$fileday*.tar.gz .
        done

done
for file in `ls -l|grep $fileday`
do
if [ -f $file ];then
        filename=`tar tvf $file|awk '{print $6}'`
        tar -zxvf $file
        cat $filename >>${basepath}${datatype}.txt
        rm -rf $filename
        rm -rf $file
fi
done


#添加python处理脚本

datatype_p=$(echo $datatype |tr '[A-Z]''[a-z]'|awk 'gsub(/-/,"_")')
echo $datatype_p

/home/aiuap_cj/python36/bin/python3.6 ${pythonpath}/data_treating.py ${basepath}${datatype}.txt ${basepath}${datatype}_out.txt $datatype_p
#插入数据库
mysql -h$hostname -P$port -u$username -vv -p$password <<EOF

use $databasename
LOAD DATA local INFILE "${log_province}"
IGNORE INTO TABLE $tablename_province 
CHARACTER SET utf8
FIELDS TERMINATED BY "|" 
LINES TERMINATED BY "\\n"
(
        reportTime,
        provinceCode,
        indexName,
        successCount,
        errorCount,
        totalCount,     
        dataType
);
EOF
done
echo "数据备份结束！$(date)"
                                                    