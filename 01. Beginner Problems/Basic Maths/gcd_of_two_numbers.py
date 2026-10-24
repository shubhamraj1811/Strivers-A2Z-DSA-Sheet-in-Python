"""
Find the GCD of two numbers - optimal approach

🤖 Approach
1. Find remainder a % b
2. Move b into a
3. Move remainder into b
4. Repeat
5. When b becomes 0, a is the GCD.

⌛ TC = O(log(min(a, b)))
🛡️ SC = O(1)
"""

def gcd(a, b):
   while b != 0:
      a, b = b, a % b

   return a

# Example
print(gcd(30, 5))
