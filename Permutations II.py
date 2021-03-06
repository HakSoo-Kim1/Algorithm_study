# https://leetcode.com/problems/permutations-ii/
# Hak Soo Kim
# 3/31/2022

class Solution(object):
    def permuteUnique(self, nums):
        ans = []
        nums.sort()
        self.dfs(nums, [], ans)

        print(ans)
        return ans
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

    def dfs(self, nums, path, ans):
        if (not nums):
            ans.append(path)
        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], ans)


# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
#
# Example 1:
#
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Constraints:
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10