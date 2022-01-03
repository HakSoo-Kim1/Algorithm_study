# https://leetcode.com/problems/find-the-duplicate-number/
# Hak Soo Kim
# 12/27/2021

class Solution(object):
    def findDuplicate(self, nums):
        numSet = set()
        for num in nums:
            if (num in numSet):
                return num
            else:
                numSet.add(num)
        """
        :type nums: List[int]
        :rtype: int
        """

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums and uses only constant extra space.
# Example 1:
#
# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:
#
# Input: nums = [3,1,3,4,2]
# Output: 3
# Constraints:
#
# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.