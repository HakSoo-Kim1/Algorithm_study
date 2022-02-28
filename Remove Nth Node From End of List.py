# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Hak Soo Kim
# 2/27/2022

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        tempHead = ListNode(0,head)
        runner = slow = tempHead
        for i in range(n):
            runner = runner.next
        while(runner.next != None):
            runner = runner.next
            slow = slow.next
        slow.next = slow.next.next
        return tempHead.next
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
#
# Input: head = [1], n = 1
# Output: []
# Example 3:
#
# Input: head = [1,2], n = 1
# Output: [1]
#
# Constraints:
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz