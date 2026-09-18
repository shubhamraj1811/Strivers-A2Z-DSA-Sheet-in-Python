"""
🚀 287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each
integer is in the range [1, n] inclusive.

There is only one repeated number in nums,
return this repeated number.

You must solve the problem without modifying the array nums
and using only constant extra space.

🤖 Example 01
Input: nums = [1,3,4,2,2]
Output: 2

🤖 Example 02
Input: nums = [3,1,3,4,2]
Output: 3

🚨 Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely 
one integer which appears two or more times.

🚨 Foolow Up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""

"""
✅ Follow Up 1
- So it is basically asking abt the mathematical observation before actually solving the problem
- This is Pigeonhole Principal
- According to the problem: nums has n + 1 elements
- But each element can have values from 1 to n only
- Therefore, it is must that there will be 1 duplicate elements for

✅ Follow Up 2
- Can you find that duplicate in O(n) time?
"""

"""
🎯 === APPROACH ===
Observation 1
Since there are n values only but array length is n+1
means arr len = 5 , but values [1, 2, 3, 4]
Hence, something must repeat

Observation 2
We can treat index as next pointer
After traversing we see a cycle is forming due to duplicates

We have to find the entrance of the cycle - to find the duplicate number and solve this problem
We use Floyd's Tortoise and Hare Algorithm
   - Slow pointer: 1 step move karega
   - Fast pointer: 2 steps move karega

Phase 1 - Detect Cycle
Move slow and fast through array
If cycle exists, slow and fast pointer will collide

Phase 2 - Find where cycle starts
move slow back to index[0]
move both fast and slow +1 until they meet - that is where cycle starts - and that is our duplicate element

❇️ ALGORITHM — Find the Duplicate Number
Step 1:
Take the array nums as input.

Step 2:
Initialize the slow pointer at nums[0].

Step 3:
Initialize the fast pointer at nums[0].

Step 4:
Move the slow pointer one step:
    slow = nums[slow]

Step 5:
Move the fast pointer two steps:
    fast = nums[nums[fast]]

Step 6:
Keep moving slow and fast until they meet.

Step 7:
When slow == fast, a cycle has been detected.

Step 8:
Reset the slow pointer to the starting point:
    slow = nums[0]

Step 9:
Now move both pointers one step at a time:
    slow = nums[slow]
    fast = nums[fast]

Step 10:
Repeat Step 9 until slow == fast.

Step 11:
The position where they meet is the entrance of the cycle.

Step 12:
The cycle entrance represents the duplicate number.

Step 13:
Return slow (or fast) as the duplicate number.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def duplicate_num_brute_force(ar):
    seen = set()

    for num in ar:
        if num in seen:
            return num
        seen.add(num)

    return None

def duplicate_num(ar):
    slow = fast = ar[0]

    while True:
        slow = ar[slow] # one step
        fast = ar[ar[fast]] # two step
        if slow == fast:
            break

        slow = ar[0]
        while slow != fast:
            slow = ar[slow]
            fast = ar[fast]

        return slow




nums = [1, 3, 4, 2, 2] # 2
# nums = [3, 1, 3, 4, 2] # 3
# nums = [3, 3, 3, 3, 3] # 3
# nums = [5]
# nums = [1, 3, 4, 2, 2]

duplicate = duplicate_num(nums)

if not duplicate == None:
    print(f"Duplicate number is {duplicate}")
else:
    print("None")
