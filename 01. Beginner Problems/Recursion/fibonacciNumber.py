"""
Fibonacci Series : 0 1 1 2 3 5 8 13 21...
Find the Nth Fibonacci Number

"""

class Solution:
   def fibonacci(self, n: int, first: int, second: int) -> int:
      # base case
      if n <= 0:
         return first
      
      return self.fibonacci(n-1, second, second+first)
   
# main
sol = Solution()
n = 1000
first = 0
second = 1

number = sol.fibonacci(n-1, first, second)
print(number)