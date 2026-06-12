"""
Leetcode Problem: 9. Palindrome Number
Difficulty: 🟢 Easy
Topic: Math

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left.

Constraints:
-2**31 <= x <= 2**31 - 1

🤖 Approach - Reverse half
1. Negative numbers are not palindromes.
2. Reverse only the half digit and compare with other half
3. 12321 -> left half = 12, right half = 12 (reverse of 21) -> palindrome

⌛ Time Complexity: O(log(n)) : where n is the input number, since we are processing each digit once.
🛡️ Space Complexity: O(1) : as we are using a constant amount of extra space.
"""

class Solution:
   def isPalindrome(self, x: int) -> bool:
      # Negative numbers are not palindromes
      if (x < 0) or (x % 10 == 0 and x != 0):
         return False
      
      half_reversed = 0
      while x > half_reversed:
         half_reversed = half_reversed * 10 + x % 10
         x //= 10

      return x == half_reversed or x == half_reversed // 10

# Example usage
solution = Solution()
print(solution.isPalindrome(121))   # Output: True
print(solution.isPalindrome(-121))  # Output: False
print(solution.isPalindrome(10))    # Output: False
print(solution.isPalindrome(12321)) # Output: True