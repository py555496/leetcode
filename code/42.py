#!/usr/bin/env python
# -*- coding: gb18030 -*-
"""
# *****File Name: 42.py
# *****author: zhoujing07  ***********
# *****Created Time: 2019-09-24 15:28:56
"""
import os
import sys
import getopt
import logging
import ConfigParser
import time
import datetime
import argparse
# *********************************************************************************************
#question url:https://leetcode-cn.com/problems/trapping-rain-water/
def find_op_f(b):
    if len(b) < 2:
        return 0,[]
    else:
        m = -1
        index = -1
        for i, v in enumerate(b[1:]):
            #longest
            if m <= v:
                m = v
                index = i
        high = min(b[0], m)
        out = 0
        for i in range(0, index + 1):
            out += max(high - b[i], 0)
        return out, b[index + 1:]

def cal(c):
    v_add = 0
    while len(c) > 0:
        out, c = find_op_f(c)
        v_add += out
    return v_add

def main_run():
    """主函数"""
    c = [5,4,1,1,2,3,1,3]
    c = [0,1,0,2,1,0,1,3,2,1,2,1]
    m = -1
    index = -1
    for i, v in enumerate(c):
        if m <= v:
            m = v
            index = i
    left_c = c[:index + 1]
    right_c = c[index:]
    print cal(left_c[::-1]) + cal(right_c)

        
    exit()
    m_n = -1
    m_index = -1
    out = []
    for i in range(a):
        if a[i] > m_n:
            m_n = a[i]
            m_index = i

    for line in open(argv[1]):
        line = line.strip('\n')
        line_arr = line.split('\t')
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

