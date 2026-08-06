"""
❇️ Given an array of integers nums, return the value of the largest element in the array

💭 Example:
Input: nums = [3, 3, 6, 1]
Output: 6
Explanation: The largest element in array is 6
"""

# ====== first method - linear search ======
# Time = O(n)
# Space = O(1)
def findLargestElement (ar):
    # edge case - empty array
    if not ar:
        return None

    large = ar[0]
    for num in ar:
        if num > large:
            large = num

    return large

# ====== second method - max function ======
# Even though this is still $O(N)$ time complexity
# the max() function is implemented in highly optimized C code under the hood.
# It avoids the overhead of the Python interpreter running a for loop,
# making it significantly faster in real time than our manual loop.
def pythonMethod(ar):
    return max(ar, default=None)

# ====== main ======
ar = [2, 3, 41, 6, 0, 9]
largest1 = findLargestElement(ar)
print(f"Largest element in the array is: {largest1}")

print()

largest2 = pythonMethod(ar)
print(f"Largest element in the array is (MAX FUN): {largest2}")