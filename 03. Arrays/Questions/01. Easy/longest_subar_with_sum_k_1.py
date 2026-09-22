"""
🚀 LONGEST SUBARRAY WITH SUM K — POSITIVE NUMBERS
============================================================


📝 PROBLEM
------------------------------------------------------------
Given an array of positive integers nums and an integer k,
return the length of the longest contiguous subarray whose
sum is exactly equal to k.


📌 EXAMPLE 1
------------------------------------------------------------
Input:
nums = [1, 2, 3, 1, 1, 1, 1]
k = 6

Output: 4

Explanation:
[3, 1, 1, 1] = 6
its length is 4.

📌 EXAMPLE 2
------------------------------------------------------------
Input:
nums = [1, 2, 1, 1, 1, 3, 2]
k = 5

Output: 4


📌 EXAMPLE 3
------------------------------------------------------------
Input:
nums = [2, 4, 6]
k = 5

Output:
0

Explanation:
No subarray has sum exactly equal to 5.


💡 CONSTRAINTS
------------------------------------------------------------
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= 10^14


🎯 EXPECTED COMPLEXITY
------------------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(1)


🧠 APPROACH
------------------------------------------------------------
Going with the sliding window approah
Concept is simple take left and right pointers
Expand right until sum is smaller than K -> keep moving right each iteration
If sum > k -> then reduce the window by shrinking from left


⚙️ ALGORITHM
------------------------------------------------------------
Take left and right and start them from 0
Take count = 0 -> to track count of max lenght
Take max = 0 -> to store max lenght
Take sum to store sum of the window




⏱️ COMPLEXITY ANALYSIS
------------------------------------------------------------
Time Complexity: O(n)
Space Complexity: O(1)
"""

# 1 2 1 1 1 3 2
# 5

def solution(a, k):
    l = r = 0
    sum = count = max_count = 0

    while r < len(a):
        # update sum and count in each iteration
        sum += a[r]
        count +=1

        # if sum == k then and count is greater than max count
        if sum == k:
            if count > max_count:
                max_count = count

        # if sum is bigger than k
        while sum > k:
            sum -= a[l]
            count -=1
            l+=1
        r+=1
    
    return max_count

nums = [1, 2, 3, 1, 1, 1, 1] # 4
nums2 = [1, 2, 1, 1, 1, 3, 2] # 4
nums3 = [2, 4, 6] # 0
a = [1, 2, 1, 1, 1] # 3
print(f"Answer: {solution(nums, 6)}")
print(f"Answer2: {solution(nums2, 5)}")
print(f"Answer3: {solution(nums3, 5)}")
print(f"Answer 4: {solution(a, 4)}")