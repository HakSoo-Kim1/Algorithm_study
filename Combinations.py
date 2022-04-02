# https://leetcode.com/problems/combinations/
# Hak Soo Kim
# 4/1/2022

class Solution(object):
    def combine(self, n, k):
        arr = [n for n in range(1, n + 1)]
        ans = []
        self.backtracking(ans, [], arr, k)
        return (ans)
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

    def backtracking(self, ans, path, arr, k):
        if (k == len(path)):
            ans.append(path)
            return
        for i in range(len(arr)):
            self.backtracking(ans, path + [arr[i]], arr[i + 1:], k)

# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
#
# You may return the answer in any order.
#
# Example 1:
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# Example 2:
#
# Input: n = 1, k = 1
# Output: [[1]]
#
# Constraints:
#
# 1 <= n <= 20
# 1 <= k <= n
