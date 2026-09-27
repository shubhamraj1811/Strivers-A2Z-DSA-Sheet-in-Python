"""
🚀 LEETCODE 1838 — FREQUENCY OF THE MOST FREQUENT ELEMENT
============================================================

🏷️ TOPICS / CONCEPTS
------------------------------------------------------------
• Array
• Sorting
• Sliding Window
• Two Pointers
• Prefix Sum / Running Sum
• Greedy
• Binary Search (alternative approach)


📝 PROBLEM
------------------------------------------------------------

The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k.

In one operation, you can choose any index i and increment nums[i] by 1.

Return the maximum possible frequency of an element after
performing at most k operations.


📌 EXAMPLE 1
------------------------------------------------------------

Input:
nums = [1,2,4]
k = 5

Output:
3

Explanation:

We can increment 1 three times and 2 two times:

[1,2,4]
 ↓ ↓↓↓
[4,4,4]

Total operations:

(4 - 1) + (4 - 2)
= 3 + 2
= 5

Therefore, the maximum possible frequency is 3.


📌 EXAMPLE 2
------------------------------------------------------------

Input:
nums = [1,4,8,13]
k = 5

Output:
2

Explanation:

We can increment 1 three times:

[1,4,8,13]
 ↓↓↓
[4,4,8,13]

Therefore, the maximum possible frequency is 2.


📌 EXAMPLE 3
------------------------------------------------------------

Input:
nums = [3,9,6]
k = 2

Output:
1


💡 CONSTRAINTS
------------------------------------------------------------

1 <= nums.length <= 10^5

1 <= nums[i] <= 10^5

1 <= k <= 10^5


🎯 EXPECTED COMPLEXITY
------------------------------------------------------------

Time Complexity:
O(n log n)

Space Complexity:
O(1) extra space
or O(n) depending on the sorting implementation.


🧠 APPROACH
------------------------------------------------------------
We will use sorting + sliding window approach
First, sort the array -> we will form a window/group and the largest element of the group will be the target
We try to make all elements of the group equal to the largest element

We maintain sliding window -> l and r (Left and right)
For current window we calculate cost
Cost = target x window_size - window_sum

cost help us calculate the maximum number of operations needed to make the rest of the
elements equal to the rightmost / largest element

If the cost is greater than k, we shrink the window from left
and whenevr the window is valid , i.e, cost is equals or smaller than k ->
we update the max_frequency


⚙️ ALGORITHM
------------------------------------------------------------
1.
Sort array

2.
Initialize ->
    left = 0
    window_sum = 0
    max_freq = 0

3.
Traverse the array : right -> 0 to n-1
    Add right to window_sum
    calc cost

    while cost > k
        remove ar[left] and left++
        recalc cost

    update max_freq

4.
Return max_freq

Sorting        → O(n log n)
Sliding window → O(n)

Overall        → O(n log n)


"""

def solution12(ar, k):
    # sort array
    ar.sort()

    # initialize
    left = 0
    window_sum = 0
    max_freq = 0

    # traverse array 0 to n-1
    for right in range(len(ar)):
        window_sum += ar[right]

        # calc cost = target x window size - window sum
        cost = ar[right] * (right - left + 1) - window_sum

        # check cost
        while cost > k:
            # shrink window from left
            window_sum -= ar[left]
            left += 1

            # recalc cost
            cost = ar[right] * (right - left + 1) - window_sum

        # update freq
        max_freq = max(max_freq, (right-left+1))

    return max_freq

# main
nums = [1, 4, 8, 13] # 2
k = 5
ans = solution12(nums, k)
print(ans)
