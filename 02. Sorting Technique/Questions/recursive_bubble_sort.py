def recursiveBubbleSort(ar, n):
    # base case
    if n <= 1:
        return

    # recursive logic
    for i in range(n-1):
        if ar[i] > ar[i+1]:
            ar[i], ar[i + 1] = ar[i + 1], ar[i]

    recursiveBubbleSort(ar, n-1)


# main function
my_list = [int(x) for x in input("Enter Numbers separated by spaces: ").split()]
print("Unsorted Array: ")
print(my_list)

recursiveBubbleSort(my_list, len(my_list))

print("Sorted Array: ")
print(my_list)