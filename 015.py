# /usr/bin/env python
# --*-- coding:utf-8 --*--
"""
___title__ : 015.py
__author__ : LongLee
___date___ : 2017/3/3 18:29
__Software : PyCharm
"""


def threesum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    for i in nums:
        for j in nums:
            for k in nums:
                if i+j+k == 0:
                    res.append([i,j,k])
    print(res)
threesum(self=(),nums=[-1, 0, 1, 2, 3, 4])

