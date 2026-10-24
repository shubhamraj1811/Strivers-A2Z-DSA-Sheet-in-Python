"""
Factorial of n terms

n = 5
n = 5 * 4 * 3 * 2 * 1
"""

def factorial(n):
    # edge case
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # base case
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

# main
n = int(input("Enter a num: "))
fact = factorial(n)
print(f"{n}! = {fact}")
