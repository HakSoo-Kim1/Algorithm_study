# https://leetcode.com/problems/reverse-string/
# Hak Soo Kim
# 2/6/2022

class Solution(object):
    def reverseString(self, s):
        for i in range(len(s) / 2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
        return (s)
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

# Write a function that reverses a string. The input string is given as an array of characters s.
#
# You must do this by modifying the input array in-place with O(1) extra memory.
#
# Example
# 1:
#
# Input: s = ["h", "e", "l", "l", "o"]
# Output: ["o", "l", "l", "e", "h"]
# Example
# 2:
#
# Input: s = ["H", "a", "n", "n", "a", "h"]
# Output: ["h", "a", "n", "n", "a", "H"]
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is a printable ascii character.