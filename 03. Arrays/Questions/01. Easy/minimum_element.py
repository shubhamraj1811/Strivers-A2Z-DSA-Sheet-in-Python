"""
🔹 Minimum Element in an Array

📝 Problem Statement
Given an integer array nums, return the smallest element present in the array.
You may assume that the array contains at least one element.

📌 Examples
Example 1:
Input: nums = [5, 2, 8, 1, 3]
Output: 1

🔒 Constraints
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

🎯 Expected Complexity
Time: O(n)
Extra Space: O(1)

================================================

🔰 Approach & Algorithm
It is not necessary to sort the array to find our answer.
We can solve this problem by doing a linear search

1. Edge Case : If array have a single element
2. Do linear search to find the smallest element

"""

def findMinimum(ar):
    n = len(ar)
    if n == 1:
        return ar[0]

    min = 9999
    print(min)

    for num in ar:
        print(num)
        if min < num:
            min = num
            print("Hello")

    return min

# main
arr = [1, 2, 3, 4, 5]
minimum = findMinimum(arr)
print(f"Minimum Element in the Array: {minimum}")