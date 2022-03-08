# https://leetcode.com/problems/generate-parentheses/
# Hak Soo Kim
# 2/8/2022

class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        self.generate(ans, 0, 0, 0, n, "")
        return (ans)
        """
        :type n: int
        :rtype: List[str]
        """

    def generate(self, ans, openCounter, closeCounter, counter, n, string):
        if (counter == 2 * n):
            ans.append(string)
            return
        if (openCounter < n):
            self.generate(ans, openCounter + 1, closeCounter, counter + 1, n, string + "(")
        if (closeCounter < openCounter):
            self.generate(ans, openCounter, closeCounter + 1, counter + 1, n, string + ")")

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
#
# Input: n = 1
# Output: ["()"]
#
# Constraints:
#
# 1 <= n <= 8