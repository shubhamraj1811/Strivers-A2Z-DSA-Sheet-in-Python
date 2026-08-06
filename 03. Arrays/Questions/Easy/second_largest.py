"""
❇️ Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.

💭 Example 1
Input: nums = [8, 8, 7, 6, 5]
Output: 7
Explanation: The largest value in nums is 8, the second largest is 7
"""

# ============ 🚀 ALGORITHM ================
# 1. Edge Case: 0 or single element array
# 2. Initialize two variables, largest and second_largest, to negative infinity
# 3. Loop thru each num in array
# 4. Condition 1: if num is greater than largest:
#       bump largest to second largest
#       update largest = num
# 5. Condition 2: if num is strictly greater than second_largest AND num is not equal to largest (this prevents duplicates from taking both spots):
#       Update second_largest to be num.
# 6. Final Check:
#       After the loop, if second_largest was never updated (meaning the array had fewer than 2 unique elements, like [2, 2]),
#       return -1. Otherwise, return second_largest.
# ====================================================================
# Time Complexity: O(N) — We only visit each element exactly once.
# Space Complexity: O(1) — We only use two variables to store our state.
# ====================================================================

def findSecondLargest(ar):
    # Guard clause for edge case
    if len(ar) < 2:
        return -1

    largest = float('-inf')
    second = float('-inf')

    for num in ar:
        # condition 1
        if num > largest:
            second = largest
            largest = num
        # condition 2
        elif num > second and num != largest:
            second = num
    # final check
    if second == float('-inf'):
        return -1
    return second

# =========== main ===========
ar1 = [8, 8, 7, 6, 5, 90, 91]
ar2 = [9, 9, 9, 9, 9]
ar3 = [99]
ar4 = []

print(f"Second Largest Element in Array 1: {findSecondLargest(ar1)}")