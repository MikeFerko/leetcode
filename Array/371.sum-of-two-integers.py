#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

binary representation i.e. base 2 number system.

We can convert the base 10 integers into base 2 and then do
boolean logic gate operations to create the adder and subtractor
operations.

Boolean logic gate Operators include:
OR, AND, XOR, NOT, NOR, NAND, NXOR etc...

Same designs as in electrical hardware design frameworks like VHDL
or FPGA etc...

use xor operator ^ and AND operator & along with the 
signed (twos compliment) representation to include signed values

On 4 bits:
    1  0001         1  0001
  + 2  0010         1  0001
------------------------------
    3  0011 = (1^2) 2  0010 << 1 (1&1) << 1 (carry over with a left shift)


    1  0001
  + 3  0011
-----------------------
    2  0010 ^
  + 2  0010 (&)<<1
-----------------------
    0  0000 ^
  + 4  0100 (&)<<1


  -2  1110
   3  0011
-----------------------
      1101
      1000
-----------------------
      0001
      0000

*NOTE: there is a 32 bit limit
Time Complexity: T(n) = O(1) # constant time

"""

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff # this is just the carry limit
        while (b & mask): # Loop until carry value is zero
            xor = (a ^ b)
            carry = (a & b)
            a = xor
            b = carry << 1 # left shift by 1
        # If a is negative in a 32 bit sequence
        # else it will return a
        return ((a & mask) if b>0 else a)

# sol = Solution()
# print(sol.getSum(2,1))
# @lc code=end

