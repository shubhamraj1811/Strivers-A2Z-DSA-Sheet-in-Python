"""
🚀 Problem
You are given an array of integers arr[]. You have to reverse the given array.
Note: Modify the array in place.

🚦Example 1
Input: arr = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]
Explanation: The elements of the array are [1, 4, 3, 2, 6, 5].
After reversing the array, the first element goes to the last position,
the second element goes to the second last position and so on.
Hence, the answer is [5, 6, 2, 3, 4, 1].

⌛ Expected Complexity
Time:  O(n)
Space: O(1)

🎯 Try to solve it without using a built-in reverse function.


"""

def reverse_array(ar):
    n = len(ar)
    for i in range(n//2):
        ar[i], ar[n-1-i] = ar[n-1-i], ar[i]

# MAIN
arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)