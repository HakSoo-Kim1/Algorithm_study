# https://leetcode.com/problems/longest-palindromic-substring/
# Hak Soo Kim
# 1/3/2022

class Solution(object):
    def longestPalindrome(self, s):
        arr = [[False]*len(s) for i in range(len(s))]
        startIndex = 0
        maxLen = 0
        for i in reversed(range(len(s))):
            j = i
            while(j < len(s)):
                if ((s[i] == s[j] and j - i < 3) or (s[i] == s[j] and arr[i + 1][j - 1])):
                    arr[i][j] = True
                    if (j - i + 1 > maxLen):
                        maxLen = j - i + 1
                        startIndex = i
                j += 1
        return s[startIndex: startIndex + maxLen]

# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
