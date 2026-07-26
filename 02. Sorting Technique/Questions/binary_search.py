import random

def binarySearch(ar):
    left, right = 0 , len(ar)-1

    while left <= right:
        # calculate mid
        mid = left + (right - left)
        # found case
        if ar[mid] == key:
            print(f"{key} found at {mid}")
            return

        # mid element is greater than key -> go left
        elif ar[mid] > key:
            right = mid-1

        # mid element is smaller than key -> go right
        else:
            left = mid+1

    print(f"{key} is not found")
    return

# main function
my_list = [int(x) for x in input("Enter Numbers separated by spaces: ").split()]
print(f"This is my list: {my_list}")

key = random.choice(my_list)
print(f"This is my key: {key}")

found = binarySearch(my_list)
print(f"Found = {found}")