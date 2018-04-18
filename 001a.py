# /usr/bin/env python
# --*-- coding:utf-8 --*--
"""
___title__ : 001a.py
__author__ :  LongLee
___date___ : 2017/3/3 12:16
__Software : PyCharm
"""

class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
