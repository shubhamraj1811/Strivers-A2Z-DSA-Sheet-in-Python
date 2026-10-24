"""
Sum of First N Nums using recursion
n = 5
sum = 1 + 2 + 3 + 4 + 5
"""


def sumOfN(n):
   if n == 0:
      return 0

   return n + sumOfN(n - 1)


# main
n = int(input("Enter a number: "))

sum = sumOfN(n)
print("Sum of First N terms are:", sum)