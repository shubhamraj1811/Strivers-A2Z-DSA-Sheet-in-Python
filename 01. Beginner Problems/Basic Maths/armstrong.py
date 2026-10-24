"""
Check if the Number is Armstrong

You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.

An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.

Example 1
Input: n = 153
Output: true
Explanation: Number of digits : 3.
13 + 53 + 33 = 1 + 125 + 27 = 153.
Therefore, it is an Armstrong number.

Example 2
Input: n = 12
Output: false
Explanation: Number of digits : 2.
12 + 22 = 1 + 4 = 5.
Therefore, it is not an Armstrong number.

Constraints : 0 <= n <= 109

🤖 Approach

1. Store original number
2. Count digits

3. Initialize armstrong_sum = 0

4. While n > 0:
      digit = n % 10
      armstrong_sum += digit ^ digits
      n = n // 10

5. Return (armstrong_sum == original)

⌛ TC = O(1)
🛡️ SC = O(1)
"""
def armstrong(n):
   temp = n
   digits = len(str(n))

   armstrong_num = 0

   while temp > 0:
      digit = temp % 10
      armstrong_num += digit ** digits
      temp //= 10

   return armstrong_num == n

# example
print(armstrong(121))
print(armstrong(153))