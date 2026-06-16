"""

Leetcode 125 - Valid Palindrome
Difficulty: 🟢 Easy
Topic: Two Pointer, String

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

---

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "racecar" is not a palindrome.

🤖 Approach
1. use two pointer left and right
2. if left > right -> return
3. check if s[left] is not alphanumeric -> left+1
4. check if s[right] is not alphanumeric -> right-1
5. check if s[left] != s[right] -> false
"""

"""

Leetcode 125 - Valid Palindrome
Difficulty: 🟢 Easy
Topic: Two Pointer, String

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

---

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "racecar" is not a palindrome.

🤖 Approach
1. use two pointer left and right
2. if left > right -> return
3. check if s[left] is not alphanumeric -> left+1
4. check if s[right] is not alphanumeric -> right-1
5. check if s[left] != s[right] -> false
"""


"""

Leetcode 125 - Valid Palindrome
Difficulty: 🟢 Easy
Topic: Two Pointer, String

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

---

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "racecar" is not a palindrome.

🤖 Approach
1. use two pointer left and right
2. if left > right -> return
3. check if s[left] is not alphanumeric -> left+1
4. check if s[right] is not alphanumeric -> right-1
5. check if s[left] != s[right] -> false
"""


def validPalindrome(s, l, r):
   # Base case
   if l >= r:
      return True

   # Skip non-alphanumeric characters from left
   if not s[l].isalnum():
      return validPalindrome(s, l + 1, r)

   # Skip non-alphanumeric characters from right
   if not s[r].isalnum():
      return validPalindrome(s, l, r - 1)

   # Compare characters (case-insensitive)
   if s[l].lower() != s[r].lower():
      return False

   # Check remaining substring
   return validPalindrome(s, l + 1, r - 1)


# Main
s = "A man, a plan, a canal: Panama"
left = 0
right = len(s) - 1

flag = validPalindrome(s, left, right)
print(flag)  # True