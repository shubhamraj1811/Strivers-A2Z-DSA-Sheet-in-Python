"""
🚀 LEETCODE 136 — SINGLE NUMBER
============================================================

📝 PROBLEM
------------------------------------------------------------
Given a non-empty array of integers nums, every element appears twice except for one element.
Find and return the element that appears only once.

You must solve the problem with:
- O(n) linear runtime
- O(1) extra space


📌 EXAMPLES
------------------------------------------------------------

Example 1:
Input:  nums = [2,2,1]
Output: 1


Example 2:
Input:  nums = [4,1,2,1,2]
Output: 4


Example 3:
Input:  nums = [1]
Output: 1


💡 CONSTRAINTS
------------------------------------------------------------
1 <= nums.length <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4

Every element appears twice except for one element.


🎯 EXPECTED COMPLEXITY
------------------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(1)


🧠 APPROACH
------------------------------------------------------------
XOR has three properties that make this problem perfect for it:
x ^ x = 0
x ^ 0 = x
XOR is commutative and associative
[4, 1, 2, 1, 2] -> 0 ^ 4 ^ 1 ^ 2 ^ 1 ^ 2 -> (1 ^ 1) ^ (2 ^ 2) ^ 4




⚙️ ALGORITHM
------------------------------------------------------------
Step 1: Just use xor operator


⏱️ COMPLEXITY ANALYSIS
------------------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(1)
"""

def single_number(a):
    s = 0
    for i in a:
        s ^= i
    return s

# nums = [4, 1, 2, 1, 2]
# nums = [2, 1, 2]
nums = [2]
nums = [2, 2]
print(f"Missing Number: [{single_number(nums)}]")
