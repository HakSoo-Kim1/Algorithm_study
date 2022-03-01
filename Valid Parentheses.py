# https://leetcode.com/problems/valid-parentheses/
# Hak Soo Kim
# 2/28/2021

class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if (i == '(' or i == '{' or i == '['):
                stack.append(i)
            elif (i == ')'):
                if (stack == [] or stack.pop() != '('):
                    return False
            elif (i == '}'):
                if (stack == [] or stack.pop() != '{'):
                    return False
            elif (i == ']'):
                if (stack == [] or stack.pop() != '['):
                    return False
        if (stack == []):
            return True
        return False
        """
        :type s: str
        :rtype: bool
        """

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.