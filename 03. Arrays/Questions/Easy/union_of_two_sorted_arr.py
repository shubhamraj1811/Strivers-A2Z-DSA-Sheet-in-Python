# Union of 2 Sorted Arrays

"""
Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.
Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.

🔥 Two pointer approach + Last element check

1. Initialize two pointers i = 0, j = 0 and an empty result.
2. Compare ar[i] and br[j].
3. Take the smaller element. If both are equal, take it only once and move both pointers.
4. Before adding an element, check whether it is already the last element of result.
5. After one array is exhausted, traverse the remaining elements of the other array, again skipping duplicates.
6. Return result.

🔰 Complexity Analysis
⏰ Time Complexity: O(n + m) — We traverse both arrays once.
🌐 Space Complexity: O(n + m) — We store the union of both arrays
"""

from unittest import result


def unionOfTwoSortedArray(ar, br):
    n, m = len(ar), len(br)
    i = j = 0
    result = []

    while i < n and j < m:

        if ar[i] <= br[j]:
            value = ar[i]
            i+=1
        else:
            value = br[j]
            j+=1

        if not result or result[-1] != value:
            result.append(value)

    while i < n:
        if not result or result[-1] != ar[i]:
            result.append(ar[i])
        i+=1

    while j < m:
            if not result or result[-1] != br[j]:
                result.append(br[j])
            j+=1
    
    return result

# main
array1 = [1, 2, 3, 3, 4, 5]
array2 = [1, 2, 3]

result = unionOfTwoSortedArray(array1, array2)
print(result)
