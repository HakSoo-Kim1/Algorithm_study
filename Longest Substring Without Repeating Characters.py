# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Hak Soo Kim
# 12/29/2021

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        indexHash = {}
        ans = 0
        left = 0
        for right in range(len(s)):
            if s[right] in indexHash:
                # left = indexHash[s[r]]   # wrong ex) "abba"
                left = max(indexHash[s[right]],left)
            indexHash[s[right]] = right + 1
            ans = max(ans,right - left + 1)
        return ans

# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.