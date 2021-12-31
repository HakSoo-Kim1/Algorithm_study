# https://leetcode.com/problems/integer-to-roman/
# Hak Soo Kim
# 12/27/2021

class Solution(object):
    def intToRoman(self, num):
        ans = ""
        if (num >= 1000):
            while(num >= 1000):
                num = num - 1000
                ans += "M"
        if(num >= 500):
            if (num // 100 == 9):
                ans += "CM"
                num -= 900
            else:
                while(num >= 500):
                    ans += "D"
                    num -= 500
        if(num >= 100):
            if (num // 100 == 4):
                ans += "CD"
                num -= 400
            else:
                while(num >= 100):
                    ans += "C"
                    num -= 100
        if (num >= 50):
            if (num // 10 == 9):
                ans += "XC"
                num -= 90
            else:
                while(num >= 50):
                    ans += "L"
                    num -= 50
        if (num >= 10):
            if (num // 10 == 4):
                ans += "XL"
                num -= 40
            else:
                while(num >= 10):
                    ans += "X"
                    num -= 10
        if (num >= 5):
            if (num // 1 == 9):
                ans += "IX"
                num -= 9
            else:
                while(num >= 5):
                    ans += "V"
                    num -= 5
        if (num >=1):
            if (num // 1 == 4):
                ans += "IV"
                num -= 4
            else:
                while (num >= 1):
                    ans += "I"
                    num -= 1
        return ans

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.
#
# Example 1:
#
# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.
# Example 2:
#
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# Example 3:
#
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
# Constraints:
#
# 1 <= num <= 3999



#### better way

# StringBuilder result = new StringBuilder();

# 	String[] roman = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
# 	int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };

# 	int i = 0;
#             //iterate until the number becomes zero, NO NEED to go until the last element in roman array
# 	while (num >0) {
# 		while ( num >= values[i]) {
# 			num -= values[i];
# 			result.append(roman[i]);
# 		}
# 		i++;
# 	}
# 	return result.toString();