"""
Print 1 to N using Recursion
"""

class Solution:
   def print1toN(self, n:int) :
      # base case
      if n==0:
         return
      print(n, end=" ")
      self.print1toN(n-1)
   
# main
sol = Solution()

sol.print1toN(9)