# arr = [22, 11, 34, 90, 25, 35]

# 1. save the length
# 2. start an outer loop from 1 to n-1
# 3. save ar[i] in currentCard and save i-1 in j (inner loop)
# 4. inner loop will run until j >= 0
# 5. if ar[j] is smaller than current  -> break
# 6. else shift j to right side and j ko -1 kardo
# 7. inner loop hone ke baad current ko j+1 me daal do 

def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        current = arr[i]
        j = i-1

        while j >= 0:

            if current >= arr[j]:
                break
            else:
                arr[j+1] = arr[j]
                j -= 1

        arr[j+1] = current
        
    return arr


arr = [22, 11, 34, 90, 25, 35]
print(f"Unsorted Array : {arr}")
insertionSort(arr)
print(f"Sorted Array: {arr}")