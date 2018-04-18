# --*--coding:utf-8--*--
"""
__title__ = ''
__author__ = 'LongLee'
__date__ = ''

"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buffer_dict = {}
        for i in range(len(nums)):
            if nums[i] in buffer_dict:
                return [buffer_dict[nums[i]], i]
            else:
                buffer_dict[target - nums[i]] = i

if __name__ == "__main__":
    s = Solution.twoSum(self = Solution, nums=[3, 3, 9], target=12)
    print(s)
