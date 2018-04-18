# /usr/bin/env python
# --*-- coding:utf-8 --*--
"""
___title__ : 005a.py
__author__ : LongLee
___date___ : 2017/3/12 11:07
__Software : PyCharm
"""


def longestPalindrome(self, s):
    if len(s) == 0:
        return 0
    maxLen = 1
    start = 0
    for i in range(len(s)):
        if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
            start = i - maxLen - 1
            maxLen += 2
            continue

        if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
            start = i - maxLen
            maxLen += 1
    return s[start:start + maxLen]

# if __name__ == '__main_':
st = longestPalindrome(self='', s='abacaac')
print(st)
