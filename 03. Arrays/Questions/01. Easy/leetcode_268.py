"""
🚀 LEETCODE 268 — MISSING NUMBER
============================================================

📝 PROBLEM
------------------------------------------------------------
Given an array nums containing n distinct numbers in therange [0, n], return the only number in the range that is missing from the array.


Example 1:
Input:  nums = [3,0,1]
Output: 2

Explanation:
n = 3, so the complete range is [0,3].
The numbers should be [0,1,2,3].
2 is missing.


Example 2:
Input:  nums = [0,1]
Output: 2


Explanation:
n = 2, so the complete range is [0,2].
2 is missing.


Example 3:
Input:  nums = [9,6,4,2,3,5,7,0,1]
Output: 8


💡 CONSTRAINTS
------------------------------------------------------------
1 <= nums.length <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.


🎯 EXPECTED COMPLEXITY
------------------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(1)


🧠 APPROACH
------------------------------------------------------------
If there are numbers from 0 to n
I add them all -> Sum of n terms
Then I start subtracting each element from the sum and the number left in the sum is the number that we need


⚙️ ALGORITHM
------------------------------------------------------------

Step 1: Take Sum = sum of n terms
Step 2: Traverse the array and keep subtracting each element from the Sum

Step 3:

Step 4:

Step 5:


⏱️ COMPLEXITY ANALYSIS
------------------------------------------------------------
Time Complexity:  O(?)
Space Complexity: O(?)

"""

def missing_number(a):
    n = len(a)
    total = n * (n+1) // 2

    for x in a:
        total -= x

    return total

nums = [3, 0, 1]
print(missing_number(nums))