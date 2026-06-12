"""
Leetcode Problem: 7. Reverse Integer
Difficulty: 🟨 Medium
Topic: Math

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

# Constraints:  -2**31 <= x <= 2**31 - 1

🤖 Approach
1. Store sign.
2. Convert the number to +ve
3. reverse digit by digit, extract last digit and add to reversed number
4. restore sign and check for overflow

⌛ Time Complexity: O(log10(n)) : where n is the input number, since we are processing each digit once.
🛡️ Space Complexity: O(1) : as we are using a constant amount of extra space.
"""

class Solution:
   def reverse(self, x:int) -> int:
      sign = -1 if x < 0 else 1
      x = abs(x)

      reverse = 0

      while x:
         digit = x % 10
         reverse = reverse * 10 + digit
         x //= 10

      reverse *= sign

      if reverse < -2**31 or reverse > 2**31 - 1:
         return 0
      
      return reverse
   
# Example usage
solution = Solution()
print(solution.reverse(123))   # Output: 321
print(solution.reverse(-123))  # Output: -321
print(solution.reverse(120))   # Output: 21
print(solution.reverse(0))     # Output: 0
print(solution.reverse(1534236469))  # Output: 0 (overflow case)