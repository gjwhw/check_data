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
datatype="packet2"

for  firmname in xtjc
do
cp $bakfilepath/$firmname/$datatype/$fileday/*$filemin*.txt .

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
tablename1="report_other"
tablename2="other"
databasename="iptv_test"
python3 ${pythonpath}/data_treating.py ${basepath}${datatype}.txt ${basepath}${datatype}_out.txt $datatype
#插入数据库
hostname="111.203.211.16"
port="3306"
username="hnxtjc"
password="hnxtjc@123."
#插入数据库
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
        videoSourceURL,
        videomediaType,
        codedFormat,
        coderateMode,
        InputvideoresolutionWidth,
        InputvideoresolutionHeight,
        OutputvideoresolutionWidth,
        OutputvideoresolutionHeight,
        Totallengthofscreendamage,
        ScreendamageNum,
        ScreendamageRate,
        videoplayedTime,
        InitialbufferTtime,
        frameRate,
        AveragecodeRate,
        cutofftimeStamp,
        VODstate,
        catonNum,
        FlowersScreenNum,
        stbdownbandwidth,
        stbupbandwidth,
        TCPRetransferRate,
        TCPDerangementRate,
        TCPRepetitiveRate,
        videoTransmissionRate,
        RTPPacketLossNum,
        RTPJitter,
        RTPPacketLossRate,
        MDIDF,
        MDIMLR,
        liveRequestNum,
        liveRequestSuccessNum,
        liveRequestAvgTime,
        vodRequsetNum,
        vodRequestSuccessNum,
        vodrequestAvgTime,
        indexedFileServerIp,
        indexedFileRequest,
        TSFileServerIP,
        TSFileRequestNum,
        TSFileREquestSuccessNum,
        TSFileRequest,
        MOS
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
        videoSourceURL,
        indexedFileServerIp,
        TSFileServer,
        startTime,
        endTime,
        videomediaType,
        codedFormat,
        coderateMode,
        InputvideoresolutionWidth,
        InputvideoresolutionHeight,
        OutputvideoresolutionWidth,
        OutputvideoresolutionHeight,
        Totallengthofscreendamage,
        ScreendamageNum,
        ScreendamageRate,
        videoplayedTime,
        InitialbufferTtime,
        frameRate,
        AveragecodeRate,
        catonNum,
        FlowersScreenNum,
        stbdownbandwidthAvg,
        stbdownbandwidthMax,
        stbupbandwidthAvg,
        stbupbandwidthMax,
        TCPRetransferRateAvg,
        TCPRetransferRateMax,
        TCPDerangementRateAvg,
        TCPDerangementRateMax,
        TCPRepetitiveRateAvg,
        VideoTransmissionRate,
        RTPPacketLossNum,
        RTPJitter,
        RTPpacketlossAvg,
        RTPpacketlossMax,
        MDIDFAvg,
        MDIDFMax,
        MDIMLRAvg,
        MDIMLRMax,
        liveRequestNum,
        liveRequestSuccessNum,
        liveRequestAvgTime,
        vodRequsetNum,
        vodRequestSuccessNum,
        vodrequestAvgTime,
        indexedFileRequestMaxTime,
        indexedFileRequestAvgTime,
        TSFileRequestNum,
        TSFileREquestSuccessNum,
        TSFileRequestAvgTime,
        TSFileRequestMaxTime,
        MOS

);
EOF
rm -rf ${basepath}${datatype}.txt
rm -rf ${basepath}${datatype}_out.txt
echo "数据备份结束！$(date)"
                                                    
