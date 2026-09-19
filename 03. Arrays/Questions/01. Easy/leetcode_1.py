"""
🚀 LEETCODE 1 — TWO SUM
============================================================

📝 PROBLEM
------------------------------------------------------------
Given an array of integers nums and an integer target,
return the indices of the two numbers such that they add
up to target.

You may assume that each input has exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.


📌 EXAMPLE 1
------------------------------------------------------------
Input:
nums = [2,7,11,15]
target = 9

Output:
[0,1]

Explanation:
nums[0] + nums[1] = 2 + 7 = 9


📌 EXAMPLE 2
------------------------------------------------------------
Input:
nums = [3,2,4]
target = 6

Output:
[1,2]


📌 EXAMPLE 3
------------------------------------------------------------
Input:
nums = [3,3]
target = 6

Output:
[0,1]


💡 CONSTRAINTS
------------------------------------------------------------
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9

Exactly one valid answer exists.


🎯 EXPECTED COMPLEXITY
------------------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(n)


🧠 APPROACH
------------------------------------------------------------





⚙️ ALGORITHM
------------------------------------------------------------


Step 1:

Step 2:

Step 3:

Step 4:

Step 5:


⏱️ COMPLEXITY ANALYSIS
------------------------------------------------------------
Time Complexity:  O(?)
Space Complexity: O(?)
"""

def two_sum(a, key):
    nmap = {}

    for i, n in enumerate(a):
        com = key - n
        if com in nmap:
            return [nmap[com], i]
        nmap[n] = i