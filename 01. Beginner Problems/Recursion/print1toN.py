"""
Print 1 to N using Recursion
Print N to 1 using Recursion
"""

class Solution:
    def printNto1(self, n:int) :
        # base case
        if n==0:
            return
        print(n, end=" ")
        self.printNto1(n-1)

    def print1toN(self, n: int):
        # base case
        if n == 0:
            return
        self.printNto1(n - 1)
        print(n, end=" ")


# main
sol = Solution()

sol.printNto1(5)
print()
sol.print1toN(5)