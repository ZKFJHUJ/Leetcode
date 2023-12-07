#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        a = []
        b = []
        while x != 0:
            a.append(x % 10)
            b.insert(0, x % 10)
            x //= 10
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True

if __name__ == '__main__':
    Solution().isPalindrome(121)
# @lc code=end

