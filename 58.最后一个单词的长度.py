#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start = 0
        end = 0
        flag = 0
        for i in range(len(s)):
            if s[i] == " ":
                if flag == 0:
                    end = i
                flag = 1
            else:
                if flag == 1:
                    start = i
                    flag = 0
        if end <= start:
            end = len(s)
        return end - start
# @lc code=end

