"""
🚀 Count Frequency of Each Element

Given an integer array nums, count the frequency of each distinct
element in the array.

Return the result as a dictionary/map where:
- Key = the element
- Value = number of times it occurs

🤖 Example 01
Input:
nums = [1, 2, 2, 3, 1, 2]

Output:
{
    1: 2,
    2: 3,
    3: 1
}

⚓ Constraints
1 <= len(nums) <= 10^5
-10^9 <= nums[i] <= 10^9

🛡️ Expected Complexity
Time:  O(n)
Space: O(n)

❇️ Approach

We will use dictionary

🔰 Algorithm

1. Start with empty dict
2. Traverse the array
3. If element doesnt exist, add the key
4. If element exist, increment the value

"""


def freq_of_elements(ar):
    table = {}

    for num in ar:
        if num in table:
            table[num] += 1
        else:
            table[num] = 1

    return table

ar = [1, 2, 2, 3, 1, 2]
print(freq_of_elements(ar))