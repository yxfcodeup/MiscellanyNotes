#_______________________getQuestions.py_____________________
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------
# Name          : getQuestions
# Version       : 1.0.0
# Author        : yxf
# Language      : Python 2.7    
# Start time    : 2016-04-22 16:15
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
import ConfigParser
import getopt
import logging
import logging.config
import logging.handlers
import urllib
import urllib2
import codecs


os.environ["NLS_LANG"] = "SIMPLIFIED CHINESE_CHINA.UTF8"
script_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
print("---> Path of " + str(sys.argv[0].split("/")[-1]) + ": " + str(script_path))
logging.config.fileConfig(str(script_path) + "/config/logging.conf")
logger = logging.getLogger("root")
conf_file = str(script_path) + "/config/main.conf"
main_conf = ConfigParser.ConfigParser()
main_conf.read(conf_file)


def reverseResult(page) :
    return "{0},{1},{2},{3}".format(int(page[0]) , page[1] , int(page[2]) , int(page[3]))


def getOneWebPage(url , num) :
    enable_proxy = True
    proxy_handler = urllib2.ProxyHandler({"http":"58.222.254.11:3128" , "http":"61.185.219.126:3128" , "http":"218.247.161.37:80"})
    null_proxy_handler = urllib2.ProxyHandler({})
    user_agent = "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
    headers = {'User-Agent':user_agent}
    values = {'username':'cqc' , 'password':'x1x'}
    question_id = int(num)
    question_name = ""
    focus = 0
    answer = 0
    web_page_file = ""
    name_rex = "<h2 class=\"zm-item-title zm-editable-content\">(\s*)(.+)(\s*)</h2>"
    focus_rex = "</button>(\s*)(\d+)(\s*)人关注该问题"
    answer_rex = "<h3 data-num=\"(\d+)\" id=\"zh-question-answer-num\">(\d+)(\s*)个回答</h3>"
    request = urllib2.Request(url)
    try :
        response = urllib2.urlopen(request , timeout=600)
        web_page_file = response.read()
    except Exception , e :
        #logger.error("--------------------Error--------------------")
        #logger.error("---> Error url: " + url)
        #logger.error("---> " + str(e))
        #logger.error("--------------------Error--------------------")
        a = 1
    finally :
        a = 0
    if ""==web_page_file or None==web_page_file :
        return False
    is_exist_rex_1 = re.search(re.compile("你似乎来到了没有知识存在的荒原...") , web_page_file)
    is_exist_rex_2 = re.search(re.compile("来源链接是否正确？用户、话题或问题是否存在？") , web_page_file)
    if None!=is_exist_rex_1 and None!=is_exist_rex_2 :
        return False
    name_match = re.findall(re.compile(name_rex) , web_page_file)
    #logger.info("---> " + str(name_match))
    if 1 != len(name_match) :
        return False
    if len(name_match[0]) < 2 :
        return False
    question_name = name_match[0][1]
    #print(question_name)
    focus_match = re.findall(re.compile(focus_rex) , web_page_file)
    #logger.info("---> " + str(focus_match))
    if 1 != len(focus_match) :
        return False
    if len(focus_match[0]) < 2 :
        return False
    focus = str(focus_match[0][1])
    answer_match = re.findall(re.compile(answer_rex)  , web_page_file)
    #logger.info("---> " + str(answer_match))
    if 1 != len(answer_match) :
        return False
    if len(answer_match[0]) < 2 :
        return False
    answer = str(answer_match[0][1])
    #with open(script_path + "/dataResults/test.txt" , 'w') as f :
    #    f.write(web_page_file)
    return [question_id , question_name , focus , answer]


def getMoreWebPages(start_num , end_num , thread_id) :
    origin_url = "https://www.zhihu.com/question/"
    results = []
    for i in xrange(start_num , end_num) :
        time.sleep(0.01)
        url = origin_url + str(i)
        #logger.info("---> Url: " + url)
        res = getOneWebPage(url , i)
        if False == res :
            continue
        results.append(res)
        if 0 == len(results)%1000 :
            with open(script_path + "/dataResults/thread" + str(thread_id) , 'w') as f :
                for r in results :
                    r = reverseResult(r)
                    f.write(r)
                    f.write("\n")
                results = []


def mainRun(all_start , all_end) :
    #getMoreWebPages(27000000 , 27850629 , 1)
    #getOneWebPage("https://www.zhihu.com/question/27850529" , 27850529)
    #all_start = 27000000
    #all_end = 28000000
    num_thread = 10
    threads = []
    start_list = []
    end_list = []
    single_numbers = (all_end - all_start) / num_thread
    for x in range(num_thread) :
        start = single_numbers * x + all_start
        end = single_numbers * (x + 1) + all_start
        start_list.append(start)
        end_list.append(end)
    logger.info("---> Start_list: " + str(start_list))
    logger.info("---> End_list: " + str(end_list))
    for i in range(num_thread) :
        t_name = "_thread_" + str(i)
        threads.append(threading.Thread(target=getMoreWebPages , name=t_name , args=(start_list[i] , end_list[i] , i)))
    logger.info("---> Threads: " + str(threads))
    for t in threads :
        t.setDaemon(True)
        t.start()
    for t in threads :
        t.join()


def optMain() :
    #logger.info("---> Catch command line argument...")
    logger.info("-----------------Get Questions from Zhihu------------------------")
    logger.info("---> Catch command line arguments...")
    if len(sys.argv) < 2 :
        logger.error("---> Program needs two arguments.\nExit...")
        sys.exit(1)
    opts , args = getopt.getopt(sys.argv[1:] , "s:e:")
    all_start = 0
    all_end = 0
    for opt,value in opts :
        if "-s" == opt :
            all_start = int(value)
        elif "-e" == opt :
            all_end = int(value)
        else :
            print(value)
    mainRun(all_start , all_end)


if __name__ == "__main__" :
    logger.info("---> Start...")
    optMain()
