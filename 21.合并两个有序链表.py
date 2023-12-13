#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        res = ListNode(0)
        head = res
        while p1 and p2:
            if p1.val <= p2.val:
                res.next = p1
                p1 = p1.next
                res = res.next
            else:
                res.next = p2
                p2 = p2.next
                res = res.next
        res.next = p1 or p2
        return head.next
# @lc code=end

