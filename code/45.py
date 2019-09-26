#!/usr/bin/env python
# -*- coding: gb18030 -*-
import os
import sys
import datetime
import argparse
reload(sys) #Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('gb18030')

# *********************************************************************************************
class Solution(object):
    def jump(self, nums):
        jump_num = 0
        if max(nums) == 1:
            return len(nums) - 1
        while len(nums) > 1:
            b = nums.pop(0)
            #last step
            if b + 1 > len(nums):
                jump_num += 1
                break
            #Greedy:find max step
            max_step = -1
            max_index = -1
            for g in range(1, b + 1):
                step = g + nums[g - 1]
                if step > max_step:
                    max_step = step
                    max_index = g
            # do one step
            nums = nums[max_index - 1:]
            jump_num += 1
        return jump_num


def main_run():
    """主函数"""
    a = [1, 1, 1,1,1,1,1]
    a = [6,2,6,1,7,9,3,5,3,7,2,8,9,4,7,7,2,2,8,4,6,6,1,3]
    a = [1, 2, 3]
    a = [2, 3, 1, 1, 4, 1, 4, 2, 3, 1, 2]
    solu = Solution()
    print solu.jump(a)

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

