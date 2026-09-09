"""
❇️ Problem
Given an integer array nums, count the frequency of every distinct element in the array.
Return or print each element along with the number of times it occurs.

💭 Example 1
Input:
nums = [1, 2, 2, 3, 1, 4, 2]

Output:
1 -> 2
2 -> 3
3 -> 1
4 -> 1

💭 Example 2
Input:
nums = [1, 2, 2, 3, 1, 4, 2]

Output:
1 -> 2
2 -> 3
3 -> 1
4 -> 1

📌 Target
Time:  O(n)
Space: O(n)

⚙️ Approach & Algorithm
1. Create empty Frequency table
2. Traverse the whole array
    a. If key exist -> increment the value
    b. if not , add the key with value = 1
3. At the end, print the table

"""

def frequency(nums):
    freq = {}

    # traverse the array
    for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
    print(freq)

# main
nums1 = [1, 2, 2, 3, 1, 4, 2]

frequency(nums1)