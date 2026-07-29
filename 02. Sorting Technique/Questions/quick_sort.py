# ===== QUICK SORT =====
def quickSort(ar, low, high):
    if low < high:
        # get pivot index
        p_index = partition(ar, low, high)

        # left unsorted part
        quickSort(ar, low, p_index-1)

        # right unsorted part
        quickSort(ar, p_index+1, high)

def partition(ar, low, high):
    # take a pivot
    pivot = ar[low]
    i, j = low, high

    # 
    while i < j:
        while i <= high - 1 and ar[i] <= pivot:
            i += 1

        while j >= low + 1 >= pivot and ar[j] > pivot:
            j -= 1

        if i < j:
            ar[i], ar[j] = ar[j], ar[i]
    # 
    ar[low], ar[j] = ar[j], ar[low]
    return j

# main
ar = [3, 1, 2, 4, 7, 6, 8]
n = len(ar)
quickSort(ar, 0, n-1)
print(ar)