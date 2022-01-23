# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Hak Soo Kim
# 1/22/2022

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        ans = []
        self.dfs(root, 0, ans)
        return ans
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

    def dfs(self, root, k, ans):
        if (not root):
            return
        if (len(ans) == k):
            ans.append([])
        ans[k].append(root.val)
        if (root.left):
            self.dfs(root.left, k + 1, ans)
        if (root.right):
            self.dfs(root.right, k + 1, ans)

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:
#
# Input: root = [1]
# Output: [[1]]
# Example 3:
#
# Input: root = []
# Output: []
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000