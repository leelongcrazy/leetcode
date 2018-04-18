# /usr/bin/env python
# --*-- coding:utf-8 --*--
"""
___title__ : 202.py
__author__ : LongLee
___date___ : 2017/3/18 14:58
__Software : PyCharm
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        p = []
        while True:
            l = [x for x in str(n)]
            n = 0
            for i in l:
                n += (int(i) ** 2)
            p.append(n)
            if n == 1:
                return True
            elif p.count(n) >= 2:
                return False

if __name__ == "__main__":
    s = Solution()
    print(s.isHappy(10))

