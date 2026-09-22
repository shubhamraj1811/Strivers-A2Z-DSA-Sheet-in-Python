"""
#️⃣ QUESTION
Given an array arr[]. Rotate the array to the left (anti-clockwise direction) by k steps, where k is a positive integer.

🌐 Example
Input: arr[] = [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]
Explanation: 
when rotated by 2 elements, it becomes [3, 4, 5, 1, 2]
"""

"""
🔰 ALGORITHM

1. Let n = length of the array.
2. If n < 2:
      Stop.
3. Normalize k.
      k = k % n
4. If k == 0:
      Stop.
5. Reverse the first k elements.
      (Index 0 to k-1)
6. Reverse the remaining n-k elements.
      (Index k to n-1)
7. Reverse the entire array.
      (Index 0 to n-1)
8. Rotation completed.

===========================
Normalize k
      ↓
Reverse Left Part
      ↓
Reverse Right Part
      ↓
Reverse Whole Array
===========================

⌛ Time Complexity: O(n)
🌐 Space Complexity: O(1)
"""


# ========== Revserse Function ==========
def reverse(a, start, end):
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1

# ===== Rotate Function =====
def leftRotateByK(a, k):
    n = len(a)
    # edge case
    if n < 2:
        return

    # normalise k
    k = k % n
    if k == 0:
        return

    # reverse first k elements
    reverse(a, 0, k-1)

    # reverse remaining n-k elements
    reverse(a, k, n-1)

    # reverse whole array
    reverse(a, 0, n-1)

# main
ar = [1, 2, 3, 4, 5, 6, 7]
d = 3

print(f"Original Array: {ar}")

leftRotateByK(ar, d)

print(f"Array after {d} left rotations: {ar}")
