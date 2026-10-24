"""
🚀 COUNT ALL DIGITS OF A NUMBER
🕹️ Difficulty : 🟢 Easy

============================================================

🏷️ TOPICS / CONCEPTS
------------------------------------------------------------

• Basic Math
• While Loop
• Integer Division
• Modulo Operator
• Number Manipulation


📝 PROBLEM
------------------------------------------------------------

Given an integer n, count the total number of digits in it.
Return the total digit count as an integer.
For this problem, n = 12345.


📌 EXAMPLE 1
------------------------------------------------------------

Input:
n = 12345

Output:
5

Explanation:
The number 12345 contains 5 digits.


📌 EXAMPLE 2
------------------------------------------------------------

Input:
n = 908

Output:
3

Explanation:
The number 908 contains 3 digits.


📌 EXAMPLE 3
------------------------------------------------------------

Input:
n = 7

Output:
1

Explanation:
The number 7 contains only 1 digit.


💡 CONSTRAINTS
------------------------------------------------------------

-10⁹ <= n <= 10⁹

The input may be positive, negative, or zero.
The minus sign is not counted as a digit.


🎯 EXPECTED COMPLEXITY
------------------------------------------------------------

Time Complexity:  O(log₁₀ |n|) for n != 0
Space Complexity: O(1) auxiliary space


🧠 APPROACH
------------------------------------------------------------

A simple and easy approach for this problem is that we convert the given number into a string.
Then we simply use the len() function to output the lenght of the string.

But we will not use this method as this is the brute force method.

Instead I will apply digit extaction and for every digit extracted I will maintain a count variable.
It will continue until num is not zero.





⚙️ ALGORITHM
------------------------------------------------------------

✍️ YOUR ALGORITHM HERE

Step 1: If n = 0, return zero

Step 2: Remove negative sign

Step 3: Count the digits : new_num = new_num/10 and increment count on each digit removal

Step 4:


⏱️ COMPLEXITY ANALYSIS
------------------------------------------------------------

Time Complexity:  O(log₁₀ |n|)
Space Complexity: O(1)
"""

# Code Solution


def solution(num):
    # edge case
    if num == 0:
        return 1
    
    new_num = abs(num)
    count = 0
    while new_num:
        new_num //= 10
        count+=1
    return count

# MAIN
num = int(input("Enter a number: "))
count = solution(num)
print(f"Number of digits = {count}")