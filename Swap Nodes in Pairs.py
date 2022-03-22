# https://leetcode.com/problems/swap-nodes-in-pairs/
# Hak Soo Kim
# 3/21/2021

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if (head == None or head.next == None):
            return head

        nextNode = head.next
        head.next = self.swapPairs(nextNode.next)
        nextNode.next = head
        return nextNode

        """
        :type head: ListNode
        :rtype: ListNode
        """

# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:
#
# Input: head = []
# Output: []
# Example 3:
#
# Input: head = [1]
# Output: [1]
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100