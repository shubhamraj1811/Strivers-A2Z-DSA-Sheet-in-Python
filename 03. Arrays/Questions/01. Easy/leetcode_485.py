"""
🚀 LEETCODE 485 — MAX CONSECUTIVE ONES
============================================================

📝 PROBLEM
------------------------------------------------------------
Given a binary array nums, return the maximum number of
consecutive 1's in the array.


📌 EXAMPLE 1
------------------------------------------------------------
Input:
nums = [1,1,0,1,1,1]

Output:
3

Explanation:
The first two 1's have a length of 2.
The last three 1's have a length of 3.
Therefore, the maximum number of consecutive 1's is 3.


📌 EXAMPLE 2
------------------------------------------------------------
Input:
nums = [1,0,1,1,0,1]

Output:
2


📌 EXAMPLE 3
------------------------------------------------------------
Input:
nums = [0,0,0,0]

Output:
0


💡 CONSTRAINTS
------------------------------------------------------------
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.


🎯 EXPECTED COMPLEXITY
------------------------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(1)


🧠 APPROACH
------------------------------------------------------------
- Here the approach is I keep counting the ones that i encounter and increase the counter variable
- I also maintain a max_count
- when count grows bigger than max_count, I update max_count
- at the end of the loop -> max_count is returned


⚙️ ALGORITHM
------------------------------------------------------------

Step 1:
Take two variables: count & max

Step 2:
Traverse thru array, If found 1 -> count + 1 and if count > max -> max = count

Step 3:
If not 1 -> count = 0

Step 4:
Return Max



⏱️ COMPLEXITY ANALYSIS
------------------------------------------------------------
Time Complexity:  O(?)
Space Complexity: O(?)


"""

def solution(a):
    max = count = 0

    for num in a:
        if num == 1:
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    return max

ar1 = [1, 1, 0, 1, 1, 1] # 3
print(solution(ar1))
ar2 = [1, 0, 1, 1, 0, 1] # 2
print(solution(ar2))
ar3 = [0, 0, 0, 0] # 0
print(solution(ar3))
ar4 = [0] # 0
print(solution(ar4))