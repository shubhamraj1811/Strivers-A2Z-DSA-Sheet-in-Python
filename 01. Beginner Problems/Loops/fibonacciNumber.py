class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1

        while n > 0:
            first, second = second, first + second
            n -= 1

        return first

sol = Solution()

n = 1500
num = sol.fib(n)
print(num)

# 0 1 1 2 3 5 8 13
# 0 1 2 3 4 5 6 7