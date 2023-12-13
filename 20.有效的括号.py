#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        for i in s:
            if i == "(" or i == "[" or i == '{':
                a.append(i)
            elif len(a) == 0:
                return False
            elif i == ")" and a.pop() != "(":
                return False
            elif i == "]" and a.pop() != "[":
                return False            
            elif i == "}" and a.pop() != "{":
                return False
        return len(a) == 0
                
# @lc code=end

