#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs:
                if i == len(s) or s[i] != c:
                    return strs[0][:i]
        return strs[0]
# @lc code=end

