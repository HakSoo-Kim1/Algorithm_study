# https://leetcode.com/problems/search-a-2d-matrix/
# Hak Soo Kim
# 3/23/2022

class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        possibleRow = -1
        for i in range(m):
            if (matrix[i][-1] >= target):
                possibleRow = i
                break
        if (possibleRow == -1):
            return False
        else:
            for j in range(n):
                if (matrix[possibleRow][j] == target):
                    return True
            return False
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
#
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104