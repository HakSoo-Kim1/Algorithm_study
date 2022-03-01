# https://leetcode.com/problems/fizz-buzz/
# Hak Soo Kim
# 2/1/2022

class Solution(object):
    def fizzBuzz(self, n):
        ans = []
        for i in range(n):
            temp = i + 1
            if (temp % 3 == 0 and temp % 5 == 0):
                ans.append("FizzBuzz")
            elif (temp % 3 == 0):
                ans.append("Fizz")
            elif (temp % 5 == 0):
                ans.append("Buzz")
            else:
                ans.append(str(temp))
        print(ans)
        return ans
        """
        :type n: int
        :rtype: List[str]
        """

# Given an integer n, return a string array answer (1-indexed) where:
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
#
# Example
# 1:
#
# Input: n = 3
# Output: ["1", "2", "Fizz"]
# Example
# 2:
#
# Input: n = 5
# Output: ["1", "2", "Fizz", "4", "Buzz"]
# Example
# 3:
#
# Input: n = 15
# Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
#
# Constraints:
#
# 1 <= n <= 104
