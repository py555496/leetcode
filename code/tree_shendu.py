#!/usr/bin/env python
# -*- coding: gb18030 -*-
"""
# *****File Name: tree_shendu.py
# *****author: zhoujing07  ***********
# *****Created Time: 2019-09-25 23:20:35
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
class treeNode(object):
    def __init__(self):
        self.value = -1
        self.left_node = None
        self.right_node = None

def creat_test_tree():
    """test"""
    n = treeNode()
    n.value = 1
    n1 = treeNode()
    n1.value = 2
    n.left_node = n1
    n2 = treeNode()
    n2.value = 3
    n.right_node = n2
    n3 = treeNode()
    n3.value = 4
    n1.left_node = n3
    n4 = treeNode()
    n4.value = 5
    n3.left_node = n4
    n5 = treeNode()
    n5.value = 6
    n2.right_node = n5
    return n

def guangdu(a):
    b = []
    b.append(a)
    while len(b) > 0:
        out = b.pop(0)
        if out.left_node != None:
            b.append(out.left_node)
        if out.right_node != None:
            b.append(out.right_node)
        print out.value

def shendu(a):
    b = []
    b.append(a)
    while len(b) > 0:
        out = b.pop(0)
        print out.value
        if out.right_node != None:
            b = [out.right_node] + b
        if out.left_node != None:
            b = [out.left_node] + b

def main_run():
    """主函数"""
    a = creat_test_tree()
    guangdu(a)
    print ""
    shendu(a)


    return 0

if __name__ == '__main__':
    start = datetime.datetime.now()
    #parser = argparse.ArgumentParser()
    #parser.add_argument("--option", required = True, help="readme txt")
    #args = parser.parse_args()
    #main_run(args)
    main_run()
    end = datetime.datetime.now()
    # print sys.argv[0]+' this program has finnished....takes %d'%((end - start).total_seconds())

