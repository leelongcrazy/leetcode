# --*--coding:utf-8--*--
"""
__title__ = ''
__author__ = 'LongLee'
__date__ = ''

"""
def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = [nums]
    for i in range(len(nums)-1):
        for one in result[:]:
            for j in range(i+1, len(nums)):
                result.append(one[:i] + one[j:] + one[i:j])
    print(result)

permute(self=(), nums=[1, 2, 3])
