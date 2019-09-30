#!/usr/bin/env python
# -*- coding: gb18030 -*-
# *****author:   zhoujing07  ***********
# *****date:     20150908    ***********

import os
import sys
import getopt
import logging
import ConfigParser
import time
import datetime
# **********************  template function **************
# now time if neaded
# now = datetime.datetime.now()
# date = now.strftime("%Y%m%d%H%M%S")


# baselog if needed
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s \
# %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',\
# datefmt='%a, %d %b %Y %H:%M:%S', \
# filename='./(log_dir)/(log_name)',filemode='w')
reload(sys)
sys.setdefaultencoding('gb18030')

def get_now_day_time():
    now = datetime.datetime.now()
    date = now.strftime("%Y_%m_%d:%H_%M_%S")
    return date

def Usage():
    print 'Usage:%s -h help\t here is param' %sys.argv[0]

def read_conf(conf_file):
    conf_dict = {}
    cf = ConfigParser.ConfigParser()
    cf.read(conf_file)
    for section in cf.sections():
        section_dict = {}
        for option in cf.options(section):
            section_dict[option] = cf.get(str(section), str(option))
        conf_dict[section] = section_dict
    return conf_dict


# python.py  -a -b b_value --c_str --d_str d_value
def get_opt():
    try:
        opts,args = getopt.getopt(sys.argv[1:], 'hab:', ["c_str", "d_str="])
        for op, value in opts:
            if op in '-a':
                print 'option a'
            if op in '-b':
                global __b
                __b = value
            if op in '--c_str':
                print 'option c_str'
            if op in '--d_str':
                global __d_str
                __d_str = value
            if op in '-h':
                Usage()
                sys.exit()
    except getopt.GetoptError:
        Usage()
        sys.exit()
# *********************************************************************************************
#question url https://leetcode-cn.com/problems/two-sum/
def main_run(argv):
    for line in open(argv):
        line = line.strip('\n')
        line_arr = line.split('\t')
    return 0
class Solution(object):
    def twoSum(self, nums, target):
        for n in range(0, len(nums)):
            for m in range(n + 1, len(nums)):
                if nums[n] + nums[m] == target:
                    return [n, m]
    def twoSum2(self, nums, target):
        d = {}
        for i in range(0, len(nums)):
            d[nums[i]] = i
        for g in range(0, len(nums)):
            if target - nums[g] in d and not g == d[target - nums[g]]:
                return [g, d[target - nums[g]]]


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print s.twoSum2(nums, target)

    # print sys.argv[0]+' this program has finnished....takes %d'%((end - start).total_seconds())

