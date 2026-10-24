"""
🚀 BUILD THIS PATTERN — SOLID SQUARE
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

Given an integer n, print a square pattern consisting of
n rows and n columns of asterisks (*).

Each row must contain exactly n asterisks.

For this problem, n = 4.


📌 EXAMPLE 1
------------------------------------------------------------

Input:
n = 4

Output:

****
****
****
****


📌 EXAMPLE 2
------------------------------------------------------------

Input:
n = 3

Output:

***
***
***


💡 CONSTRAINTS
------------------------------------------------------------

1 <= n <= 100

Each row must contain exactly n asterisks.

The pattern must contain exactly n rows.


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
        print("* " * n)
    return

# MAIN
num = int(input("Enter a number: "))
solution(num)