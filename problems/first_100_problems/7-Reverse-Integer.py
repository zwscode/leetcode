"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


https://leetcode.com/problems/reverse-integer/
"""

# naive implementation
def reverse(self, x: int) -> int:
    sign = 1
    if x < 0:
        sign = -1
        x = -x
    nums = []
    while(x != 0):
        mod = x % 10
        nums.append(mod)
        x = x // 10
    result = 0
    for num in nums:
        result = result*10 + num
    # check if result is out of range
    if result > (2**31 - 1):
        return 0
    return result * sign

