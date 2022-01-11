# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Hak Soo Kim
# 1/10/2022

class Solution(object):
    def permute(self, nums):
        ans = []
        tempList = []
        self.backtrack(ans, nums, tempList)
        return ans
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

    def backtrack(self, ans, nums, tempList):
        if (len(nums) == 0):
            ans.append(tempList)
            return
        for i in range(len(nums)):
            self.backtrack(ans, nums[:i] + nums[i + 1:], tempList + [nums[i]])

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
#
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
#
# Input: nums = [1]
# Output: [[1]]
#
# Constraints:
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
