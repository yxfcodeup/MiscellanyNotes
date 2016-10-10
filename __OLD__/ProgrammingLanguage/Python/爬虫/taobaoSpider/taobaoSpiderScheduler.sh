#!/bin/bash

source ~/.bashrc
#source /etc/profile
workdir=`pwd`
hdfsdir="hdfs://192.168.1.130:8020/user/bp"
xdrdir="hdfs://192.168.1.130:8020/user/xdr"
outdir=${workdir}/out
logfile="${workdir}/logs/scheduler.log"
ip="192.168.1.130"
symbol=0

log()
{
	echo `date '+%Y-%m-%d %H:%M:%S'` $*
	echo `date '+%Y-%m-%d %H:%M:%S'` $* >> $logfile
}
log "log begin ================================================"
cd ${workdir}

nowtime=`date '+%S'`
datatime=`date +%Y%m%d%H -d '-4 hours'`
deletetime=`date +%Y%m%d%H -d '-30 days'`
dirtime=`date +%Y%m%d -d '-4 hours'`
datatime=2015060418
dirtime=20150604
hdfsfiles="${xdrdir}/${dirtime}/"
log "datatime:${datatime}"
log "dirtime:${dirtime}"
log "hdfsfiles:${hdfsfiles}"
log "spark-submit ${workdir}/src/userTags.py -p ${hdfsfiles} -t ${datatime}"

#spark-submit ${workdir}/src/userLabel.py -p ${hdfsfiles} -t ${dirtime}
spark-submit ${workdir}/src/test_userLabel.py -p ${hdfsfiles} -t ${dirtime}
log "monitor complete! -p ${hdfsfiles} -t ${datatime}"
mkdir -p ${workdir}/dataResults/${dirtime}
hdfs dfs -get ${hdfsdir}/${dirtime}/part-00000 ${workdir}/dataResults/${dirtime}
hdfs dfs -rm -r ${hdfsdir}/${dirtime}

