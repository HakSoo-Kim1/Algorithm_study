# https://leetcode.com/problems/climbing-stairs/
# Hak Soo Kim
# 2/28/2022

class Solution(object):
    def climbStairs(self, n):
        if (n <= 0):
            return 0
        elif (n == 1):
            return 1
        elif (n == 2):
            return 2
        previousTwoStep = 1
        previousOneStep = 2
        for i in range(2, n):
            nStep = previousTwoStep + previousOneStep
            previousTwoStep = previousOneStep
            previousOneStep = nStep
        return nStep

        """
        :type n: int
        :rtype: int
        """

# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example 1:
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
# Constraints:
#
# 1 <= n <= 45