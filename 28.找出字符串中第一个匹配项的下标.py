#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        first = 0
        second = 0
        # for i in range(len(haystack)):
        while 1:
            if second == len(needle):
                return first - second
            if len(haystack) - first < len(needle) - second:
                return -1
            # if first == len(haystack):
            #     return -1
            if haystack[first] == needle[second]:
                second += 1
                first += 1
            else:
                first = first - second + 1
                second = 0

# @lc code=end

