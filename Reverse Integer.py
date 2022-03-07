# https://leetcode.com/problems/reverse-integer/
# Hak Soo Kim
# 2/7/2022

class Solution(object):
    def reverse(self, x):
        negative = False
        if (x < 0):
            negative = True
            x *= -1
        ans = 0
        while (x > 0):
            ans *= 10
            ans += x % 10
            x /= 10
            if ans < (-2 ** 31) or ans > (2 ** 31 - 1):
                return 0
        if (negative):
            ans *= -1
        return ans
        """
        :type x: int
        :rtype: int
        """

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# Example 1:
#
# Input: x = 123
# Output: 321
# Example 2:
#
# Input: x = -123
# Output: -321
# Example 3:
#
# Input: x = 120
# Output: 21
#
# Constraints:
#
# -231 <= x <= 231 - 1