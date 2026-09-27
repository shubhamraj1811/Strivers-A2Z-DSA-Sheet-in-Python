"""
🚀 CHECK IF THE ARRAY IS SORTED
============================================================


📝 PROBLEM
------------------------------------------------------------
Given an integer array nums, determine whether the array is
sorted in non-decreasing order.

Return True if the array is sorted. Otherwise, return False.


📌 EXAMPLE 1
------------------------------------------------------------
Input:
nums = [1, 2, 3, 4, 5]

Output:
True


📌 EXAMPLE 2
------------------------------------------------------------
Input:
nums = [1, 2, 2, 3, 4]

Output:
True

Explanation:
Equal adjacent elements are allowed.


📌 EXAMPLE 3
------------------------------------------------------------
Input:
nums = [1, 3, 2, 4, 5]

Output:
False

Explanation:
3 > 2, so the array is not sorted.


📌 EXAMPLE 4
------------------------------------------------------------
Input:
nums = [5, 4, 3, 2, 1]

Output:
False


📌 EXAMPLE 5
------------------------------------------------------------
Input:
nums = [1]

Output:
True


💡 CONSTRAINTS
------------------------------------------------------------
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9


🎯 EXPECTED COMPLEXITY
------------------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(1)
"""

def solution(a):

    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True

ar = [1, 2, 3, 4, 5]
print(solution(ar))