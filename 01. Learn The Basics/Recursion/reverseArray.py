"""
Reverse an array using recursion
array = [1,2,3,4,5]
result = [5,4,3,2,1]

🤖 Approach
1. Swap the first and last element
2. Move the two pointers inwards
3. Recursively reverse the remaining array
4. Stop when pointers cross or meet
"""

def reverseArray(arr, first, last):
   # base case
   if first >= last:
      return
   
   arr[first], arr[last] = arr[last], arr[first]
   reverseArray(arr, first+1, last-1)

# main
lst = [1,2,3,4,5]
first = 0
last = len(lst) - 1
reverseArray(lst, first, last)
print(lst)