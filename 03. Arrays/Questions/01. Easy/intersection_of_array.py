"""
🚀 LEETCODE 349 — INTERSECTION OF TWO ARRAYS
============================================================

📝 PROBLEM
------------------------------------------------------------
Given two integer arrays nums1 and nums2, return an array
of their intersection.

Each element in the result must be unique.

You may return the result in any order.


📌 EXAMPLE 1
------------------------------------------------------------
Input:
nums1 = [1,2,2,1]
nums2 = [2,2]

Output:
[2]


📌 EXAMPLE 2
------------------------------------------------------------
Input:
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

Output:
[4,9]

Explanation:
[9,4] is also accepted.


💡 CONSTRAINTS
------------------------------------------------------------
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Every element in the result must be unique.


🎯 EXPECTED COMPLEXITY
------------------------------------------------------------
Time Complexity:  O(n + m)
Space Complexity: O(n + m)


🧠 APPROACH
------------------------------------------------------------
We will put first array into a set - duplicate elements deleted
Traverse the second array




⚙️ ALGORITHM
------------------------------------------------------------
put array a1 in set1
also declare an empty set = result

"""

def solution(a1, a2):
    set1 = set(a1)
    result = set()

    for num in a2:
        if num in set1:
            result.add(num)
    return list(result)

# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(solution(nums1, nums2))