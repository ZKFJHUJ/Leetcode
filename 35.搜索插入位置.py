#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while(i <= j):
            k = i + (j - i) // 2
            if nums[k] == target:
                return k
            elif nums[k] > target:
                j = k - 1
            elif nums[i] < target:
                i = k + 1
        return i
# @lc code=end

