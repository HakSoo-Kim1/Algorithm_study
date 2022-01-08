# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Hak Soo Kim
# 1/7/2022

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        ans = []
        self.inorder(root, ans)
        return ans
        """
        :type root: TreeNode
        :rtype: List[int]
        """

    def inorder(self, root, ans):
        if (not root):
            return
        if (root.left):
            self.inorder(root.left, ans)

        ans.append(root.val)

        if (root.right):
            self.inorder(root.right, ans)

# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [1]
# Output: [1]
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100




