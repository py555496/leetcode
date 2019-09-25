#!/usr/bin/env python
# -*- coding: gb18030 -*-
"""
# *****File Name: linknode_sort.py
# *****author: zhoujing07  ***********
# *****Created Time: 2019-09-26 01:27:17
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
import random
class LinkNode(object):
    def __init__(self):
        self.value = -1
        self.next = None

def create_link(num):
    head = LinkNode()
    n = LinkNode()
    head.next = n
    head.value = -1
    a = random.randint(1, 20)
    n.value = a
    for i in range(num - 1):
        c = LinkNode()
        a = random.randint(1, 20)
        c.value = a
        n.next = c
        n = c
    return head

def swap(a, b):
    a.value, b.value = b.value, a.value

def sorted_link(head):
    length = 0
    p = head.next
    length += 1
    while p.next:
        length += 1
        p = p.next
    print length
    for i in range(length - 1):
        p = head.next
        for j in range(length - i - 1):
            if p.value > p.next.value:
                swap(p, p.next)
            p = p.next
        print_link(head)
    return head

def print_link(head):
    out = []
    n = head
    while n.next != None:
        out += [n.next.value]
        if n.next:
            n = n.next
        else:
            break
    print out 
    return head
    

def main_run(argv):
    """主函数"""
    head = create_link(10)
    print_link(head)
    head = sorted_link(head) 
    print_link(head)
    return 0

if __name__ == '__main__':
    start = datetime.datetime.now()
    #parser = argparse.ArgumentParser()
    #parser.add_argument("--option", required = True, help="readme txt")
    #args = parser.parse_args()
    #main_run(args)
    main_run(sys.argv)
    end = datetime.datetime.now()
    # print sys.argv[0]+' this program has finnished....takes %d'%((end - start).total_seconds())

