"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

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
 

Constraints:

-2^31 <= x <= 2^31 - 1


"""
import math
def reverse_int(x: int) -> int:
    if x > 0:
        num = int(str(x)[::-1])
        if num >=math.pow(-2,31)  and num <= math.pow(2,31) -1:
            return num
        else:
            return 0
    else:
        num = int('-' + str(-x)[::-1])
        if num >=math.pow(-2,31)  and num <= math.pow(2,31) -1:
            return num
        else:
            return 0




