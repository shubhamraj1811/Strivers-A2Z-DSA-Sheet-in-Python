"""
🚀 LEETCODE 283 — MOVE ZEROES
============================================================

📝 PROBLEM
------------------------------------------------------------
Given an integer array nums, move all 0's to the end of itwhile maintaining the relative order of the non-zero elements.

IMPORTANT:
- You must do this in-place.
- Do not make a copy of the array.

Example 1:
Input:  nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input:  nums = [0]
Output: [0]


💡 CONSTRAINTS
------------------------------------------------------------
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1

🎯 EXPECTED COMPLEXITY
------------------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(1)


🧠 APPROACH
------------------------------------------------------------
I started solving this problem with a two pointer approach - Read and Write
read - traverse the array
write - correct pos of nums


⚙️ ALGORITHM
------------------------------------------------------------

Step 1: we take two pointers , read & write and initialize both as 0
Step 2: read traverse the whole array and write track the swap position
Step 3: when read is not zero -> swap read and write postion values and increment write
Step 4: zeros are moved to the end in-place

⏱️ COMPLEXITY ANALYSIS
------------------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(1)

"""

def move_zeros(ar):
    write = 0
    for read in range(len(ar)):
        if ar[read] != 0:
            ar[read], ar[write] = ar[write], ar[read]
            write += 1

nums = [0, 1, 0, 3, 12]
move_zeros(nums)
print(nums)