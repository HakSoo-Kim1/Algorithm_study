# https://leetcode.com/problems/subsets/
# Hak Soo Kim
# 1/25/2022

class Solution(object):
    def subsets(self, nums):
        ans = []
        temp = []
        self.backtrack(ans, temp, nums)
        return(ans)
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    def backtrack(self, ans, temp, nums):
        ans.append(temp)
        for i in range(len(nums)):
            self.backtrack(ans, temp + [nums[i]], nums[i+1:])

# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:
#
# Input: nums = [0]
# Output: [[],[0]]
#
# Constraints:
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
