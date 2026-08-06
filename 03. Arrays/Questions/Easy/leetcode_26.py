"""
🚀 26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be K. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

===================================================

🌐 Example 1

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation:
Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k
(hence they are underscores).

🌐 Example 2

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation:
Your function should return k = 5,
with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

===================================================

🔰 Approach: Two Pointer

-> There will be two pointers: read and write
-> read = it will traverse the whole array atleast ones
-> write = it will track the unique elements also store where the elements should be placed
-> read will travel ahead of write
-> write = 0, read = 1 : since first element will already be in its right place

🔥 ALGORITHM

1. Edge Case: Array with 0 or 1 element already have all unique elements
    a. return immediately
2. read will traverse the whole array and write will track the location of unique elements
3. write = 0, read = 1
4. loop: until read 0 to n-1
    a. If ar(read) == ar(write): do nothing
    b. else: write++, swap read and right 
5. return write+1 -> unique element array lenght

🌐 Complexity
Time Complexity: O(N) — We only visit each element exactly once.
Space Complexity: O(1) — We only use two variables to store our state.

"""

def removeDuplicates(ar):
    n = len(ar)
    # edge case
    if n < 2:
        return n

    w = 0

    for r in range(1, n):
        if ar[r] != ar[w]:
            w += 1
            ar[w] = ar[r]
    return w+1

# main

array = [0,1,1,2,2]
# array = [0,1,1,2,2,2,3,3,4,5]
# array = []
# array = [1]
# array = [2,2,2,2,2,2,2]
# array = [0,0,0,0,0,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,6,6,7,7,7,7,7,7]

print(array)

n = removeDuplicates(array)
print(f"Elements = {n}")
for i in range(n):
    print(array[i], end=" ")