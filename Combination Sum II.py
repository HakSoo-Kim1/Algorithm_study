# https://leetcode.com/problems/combination-sum-ii/
# Hak Soo Kim
# 1/21/2022

class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        temp = []
        self.backtrack(ans,temp,candidates,target, 0)
        return ans
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    def backtrack(self, ans, temp, candidates, target, index):
        if (target < 0):
            return
        elif (target == 0):
            ans.append(temp)
            return
        else:
            for start in range(index, len(candidates)):
                if (start > index) and (candidates[start] == candidates[start - 1]):
                    continue
                self.backtrack(ans, temp + [candidates[start]], candidates, target - candidates[start], start + 1)

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.
#
# Example 1:
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]
#
# Constraints:
#
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30