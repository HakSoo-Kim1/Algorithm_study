# https://leetcode.com/problems/pascals-triangle/
# Hak Soo Kim
# 3/22/2022

class Solution(object):
    def generate(self, numRows):
        ans = []
        if (numRows == 0):
            return ans
        ans = [[1]]

        for i in range(1, numRows):
            temp = []
            for j in range(i + 1):
                if (j == 0 or j == i):
                    temp.append(1)
                else:
                    temp.append(ans[i - 1][j - 1] + ans[i - 1][j])
            ans.append(temp)
        return (ans)
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
# Example 1:
#
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
#
# Input: numRows = 1
# Output: [[1]]
#
# Constraints:
#
# 1 <= numRows <= 30
