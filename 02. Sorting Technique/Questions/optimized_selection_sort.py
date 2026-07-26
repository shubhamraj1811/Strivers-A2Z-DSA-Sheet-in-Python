def selection_sort(ar):
    n = len(ar)

    # traverse thru entire array
    for i in range(n-1):
        min = i

        # find smallest element index
        for j in range(i+1, n):
            if ar[j] < ar[min]:
                min = j

        # optimization
        if min != i:
            ar[i], ar[min] = ar[min], ar[i]
    return ar

# Example 1
arr1 = [2, 7, 5, 9, 11, 4]
print("Original Array:", arr1)
selection_sort(arr1)
print("Sorted Array:  ", arr1)
print()

# Example 2
arr2 = [7, 4, 1, 5, 3]
print("Original Array:", arr2)
selection_sort(arr2)
print("Sorted Array:  ", arr2)