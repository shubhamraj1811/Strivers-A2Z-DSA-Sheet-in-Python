"""
🚀 BUILD THIS PATTERN — RIGHT-ANGLED TRIANGLE
🕹️ Difficulty : 🟢 Easy

============================================================

🏷️ TOPICS / CONCEPTS
------------------------------------------------------------

• Patterns
• Nested Loops
• For Loops
• Rows and Columns
• Basic Problem Solving


📝 PROBLEM
------------------------------------------------------------

Given an integer n, print a right-angled triangle pattern
consisting of asterisks (*).

The pattern must contain n rows. The first row contains
1 asterisk, the second row contains 2 asterisks, and so on,
until the nth row contains n asterisks.

For this problem, n = 5.


📌 EXAMPLE 1
------------------------------------------------------------

Input:
n = 5

Output:

*
**
***
****
*****


📌 EXAMPLE 2
------------------------------------------------------------

Input:
n = 3

Output:

*
**
***


💡 CONSTRAINTS
------------------------------------------------------------

1 <= n <= 100

The pattern must contain exactly n rows.

Row i must contain exactly i asterisks.


🎯 EXPECTED COMPLEXITY
------------------------------------------------------------

Time Complexity:  O(n²)

Space Complexity: O(1) auxiliary space (excluding output storage)


🧠 APPROACH
------------------------------------------------------------

✍️ YOUR APPROACH HERE





⚙️ ALGORITHM
------------------------------------------------------------

✍️ YOUR ALGORITHM HERE

Step 1:

Step 2:

Step 3:

Step 4:


⏱️ COMPLEXITY ANALYSIS
------------------------------------------------------------

Time Complexity:  O(n)

Space Complexity: O(1)
"""

# Code Solution


def solution(n):
    for i in range(n):
        print("* " * (i+1))
    return


# MAIN
num = int(input("Enter a number: "))
solution(num)