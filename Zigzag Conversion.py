# https://leetcode.com/problems/zigzag-conversion/
# Hak Soo Kim
# 12/27/2021

class Solution(object):
    def convert(self, s, numRows):
        if (numRows == 1):
            return s
        ans = ""
        numCounter = 0
        leftIndent = numRows + numRows - 2
        rightIndent = 0
        while (numCounter != numRows):
            index = numCounter
            if (numCounter == numRows - 1):
                switch = False
            else:
                switch = True
            while (index < len(s)):
                ans += s[index]
                if (switch):
                    index += leftIndent
                else:
                    index += rightIndent
                if (numCounter != 0 and numCounter != (numRows - 1)):
                    switch = not switch
            leftIndent -= 2
            rightIndent += 2
            numCounter += 1
        return ans

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
#
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:
#
# Input: s = "A", numRows = 1
# Output: "A"
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000



