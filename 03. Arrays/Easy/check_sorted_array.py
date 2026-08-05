"""
❇️ Check if the given array is sorted in ascending order.

=============================================================

⚙️ ALGORITHM

1. Compare every adjacent pair of elements.
2. If any element is greater than the next one,
   the array is not sorted.
3. If the loop finishes, the array is sorted.

⌛ Time: O(n)
🌐 Space: O(1)

=============================================================
"""

def checkSortedArray(ar):
    n = len(ar)
    
    for i in range(n - 1):
        if ar[i] > ar[i + 1]:
            return False

    return True

# ==== MAIN ====
arr1 = [1, 2, 3, 4, 5] 
arr2 = [2, 1, 3, 4, 5]
arr3 = [5, 1, 2, 3, 4]
arr4 = [1, 2, 3, 4, 0]
arr5 = [1, 2, 9, 4, 5]
arr6 = [1, 1, 1, 1, 1]
arr7 = [1, 2, 2, 2, 5]
arr8 = []
arr9 = [9]

my_list = [arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9]

for ar in my_list:
    if checkSortedArray(ar):
        print("✅ Sorted")
    else:
        print("❌ Not Sorted")
