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

python ${workdir}/src/getQuestions.py -s 0 -e 10000000
