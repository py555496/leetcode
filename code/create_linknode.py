#!/usr/bin/env python
# -*- coding: gb18030 -*-
"""
# *****File Name: tree_shendu.py
# *****author: zhoujing07  ***********
# *****Created Time: 2019-09-25 22:33:20
"""
import os
import sys
import getopt
import logging
import ConfigParser
import time
import datetime
import argparse
"""
# **********************  template function **************
# now time if neaded
# now = datetime.datetime.now()
# date = now.strftime("%Y%m%d%H%M%S")

# baselog if needed
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s \
# %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',\
# datefmt='%a, %d %b %Y %H:%M:%S', \
# filename='./(log_dir)/(log_name)',filemode='w')
"""
reload(sys) #Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('gb18030')

def read_conf(conf_file):
    """get conf file"""
    conf_dict = {}
    cf = ConfigParser.ConfigParser()
    cf.read(conf_file)
    for section in cf.sections():
        section_dict = {}
        for option in cf.options(section):
            section_dict[option] = cf.get(str(section), str(option))
        conf_dict[section] = section_dict
    return conf_dict
# *********************************************************************************************
class Node(object):
    def __init__(self):
        self.next = None
        self.value = 0

def creat_rear_link(a):
    head = Node()
    head.value = -1
    head.next = None
    n = Node()
    n.value = a.pop(0)
    head.next = n
    while len(a) > 0:
        p = Node()
        p.value = a.pop(0)
        n.next = p
        n = p
    return head

def creat_head_link(a):
    a = a[::-1]
    n = Node()
    n.value = a.pop(0)
    while len(a) > 0:
        p = Node()
        p.value = a.pop(0)
        p.next = n
        n = p
    return n

def main_run():
    """主函数"""
    a = [5, 4, 1, 3, 8, 6]
    head = creat_rear_link(a)
    while head.next:
        print head.next.value
        head = head.next
    print ""
    a = [5, 4, 1, 3, 8, 6]
    n = creat_head_link(a)
    #just  next of (n - 1)
    while n.next:
        print n.value
        n = n.next
    print n.value


        

if __name__ == '__main__':
    start = datetime.datetime.now()
    #parser = argparse.ArgumentParser()
    #parser.add_argument("--option", required = True, help="readme txt")
    #args = parser.parse_args()
    #main_run(args)
    main_run()
    end = datetime.datetime.now()
    # print sys.argv[0]+' this program has finnished....takes %d'%((end - start).total_seconds())

