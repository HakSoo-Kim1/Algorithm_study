# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Hak Soo Kim
# 1/23/2022

class Solution(object):
    def letterCombinations(self, digits):
        digitLetters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        combinations = []

        for i, digit in enumerate(digits):
            if (len(combinations) == 0):
                for j, letter in enumerate(digitLetters[int(digit)]):
                    combinations.append(letter)
            else:
                temp = []
                for combination in combinations:
                    for j, letter in enumerate(digitLetters[int(digit)]):
                        temp.append(combination + letter)
                combinations = temp
        return combinations
        """
        :type digits: str
        :rtype: List[str]
        """

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
# Example
# 1:
#
# Input: digits = "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# Example
# 2:
#
# Input: digits = ""
# Output: []
# Example
# 3:
#
# Input: digits = "2"
# Output: ["a", "b", "c"]
#
# Constraints:
#
# 0 <= digits.length <= 4
# digits[i] is a
# digit in the
# range['2', '9'].