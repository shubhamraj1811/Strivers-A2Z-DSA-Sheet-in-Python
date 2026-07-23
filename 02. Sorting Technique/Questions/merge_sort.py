def mergeSort(ar):
    n = len(ar)
    # base case
    if n <= 1:
        return

    # find mid
    mid = n // 2

    # split
    left = ar[:mid]
    right = ar[mid:]

    # recursive call
    mergeSort(left)
    mergeSort(right)

    # call merge
    merge(ar, left, right)

    return ar


def merge(ar, left, right):

    i, j = 0, 0
    k = 0

    l = len(left)
    r = len(right)

    # sort and merge
    while i < l and j < r:
        if left[i] < right[j]:
            ar[k] = left[i]
            i += 1
            k += 1
        else:
            ar[k] = right[j]
            j += 1
            k += 1

    # copy remaining elements
    while i < l:
        ar[k] = left[i]
        i += 1
        k += 1

    while j < r:
        ar[k] = right[j]
        j += 1
        k += 1

    return ar

# main
my_list = [3, 1, 7, 5, 6, 9, 0, 2]
print(f"Unsorted Array: {my_list}")
mergeSort(my_list)
print(f"Sorted Array: {my_list}")
