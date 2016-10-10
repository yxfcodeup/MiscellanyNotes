#_______________________taobao.py_____________________
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------
# Name          : 
# Version       : 1.0.0
# Author        : yxf
# Language      : Python 2.7    
# Start time    : 2016-04-27 22:39
# End time      :
# Function      : 
# Operation     :
#-----------------------------------------------------------------------------------


import os
import sys
import time
import datetime
import thread
import threading
import re
import getopt
import ConfigParser
import logging
import logging.config
import logging.handlers
import urllib2
from urlparse import urlparse
from bs4 import *


os.environ["NLS_LANG"] = "SIMPLIFIED CHINESE_CHINA.UTF8"
script_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
print("---> Path of " + str(sys.argv[0].split("/")[-1]) + ": " + str(script_path))
logging.config.fileConfig(str(script_path) + "/config/logging.conf")
logger = logging.getLogger("root")
conf_file = str(script_path) + "/config/main.conf"
main_conf = ConfigParser.ConfigParser()
main_conf.read(conf_file)

time_stamp = datetime.datetime.now().strftime("%Y-%m-%d")
path = os.getcwd()
keywords = []
keyword = ""


#Receiving storage paths and keywords
if len(argv) > 2 :
    path = argv[1]
    keywords = argv[2:]



def mainRun() :
    return


def optMain() :
    #logger.info("---> Catch command line argument...")
    logger.info("-----------------taobao------------------------")
    mainRun()


if __name__ == "__main__" :
    logger.info("---> Start...")
    optMain()
