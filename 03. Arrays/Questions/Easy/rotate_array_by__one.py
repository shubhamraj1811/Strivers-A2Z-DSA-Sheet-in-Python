"""
#️⃣ Question
Given an array ar, rotate the array by one position in clockwise direction.

🚀 Example 01
Input: ar = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]
Explanation:
If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.

🔰 Approach

🔰 Algorithm

"""

def rightRotateByOne(ar):
    n = len(ar)
    # edge case
    if n < 2:
        return
    
    save_last = ar[n-1] # save last element
    for i in range(n-1, 0, -1):
        ar[i] = ar[i-1]
    ar[0] = save_last
    return ar

def leftRotateByOne(ar):
    n = len(ar)
    # edge case
    if n < 2:
        return

    save_first = ar[0]
    for i in range(n-1):
        ar[i] = ar[i+1]
    ar[-1] = save_first
    return ar


# main
a = [1, 2, 3, 4, 5]
print(f"Original Array: {a}")
print(f"Right Rotate: {rightRotateByOne(a)}")

a = [1, 2, 3, 4, 5]
print(f"Left Rotate: {leftRotateByOne(a)}")
