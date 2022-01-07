# https://leetcode.com/problems/binary-tree-right-side-view/
# Hak Soo Kim
# 1/7/2022

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        ans = []
        self.rightSideTraversalDFS(root, ans, 0)
        return ans
        """
        :type root: TreeNode
        :rtype: List[int]
        """

    def rightSideTraversalDFS(self, root, ans, depth):
        if (not root):
            return
        if (depth == len(ans)):
            ans.append(root.val)
        if (root.right):
            self.rightSideTraversalDFS(root.right, ans, depth + 1)
        if (root.left):
            self.rightSideTraversalDFS(root.left, ans, depth + 1)

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# Example 1:
#
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
#
# Example 2:
#
# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:
#
# Input: root = []
# Output: []
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
