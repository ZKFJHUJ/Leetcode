#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        a = 1
        b = 2

        while b < len(nums):
            if nums[a] > nums[a - 1]:
                a += 1
                if a == b:
                    b += 1

            elif nums[b] == nums[b - 1]:
                b += 1
            else:
                nums[a] = nums[b] 
                a += 1
                b += 1
        if nums[a] > nums[a - 1]:
            return a + 1
        else:
            return a
# @lc code=end

