"""
🚀 Problem
Given an integer array arr, determine whether the array is a palindrome.
An array is a palindrome if it reads the same from left to right and right to left.
Return True if it is a palindrome; otherwise, return False.

🤖 Example 01
Input:   arr = [1, 2, 3, 2, 1]
Output:  True

⚓ Constraints
1 <= arr.length <= 10^6
1 <= arr[i] <= 10^9
"""

def p_array(ar):
    n = len(ar)
    # base case - does not need edge case becase n//2 does nothing for n=1
    if n <= 1:
        print("True")
        return

    for i in range(n//2):
        if ar[i] != ar[n-1-i]:
            print("False")
            return
    print("True")

# MAIN
# arr = [1, 2, 3, 2, 1]
# arr = [1, 2, 3, 4, 5]
arr = [1]

p_array(arr)
