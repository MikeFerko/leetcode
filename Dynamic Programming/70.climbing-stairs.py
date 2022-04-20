#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

'''
Can take one or two steps -> how many combinations of 1 or two steps can get us to the top?

We can use a decision tree to see if we want to take one step or two steps
i.e. every time we reach a leaf node in the decision tree the node value at that level will be
the top step value. 

We can use depth first search on the decision tree, but we can use dp to remember the number of solutions
for parts of the decision tree that have already been solved on other branches that lead to a solution.

This can be done using memoization/caching
this will look like a reversed Fibonacci sequence 

Time Complexity: T(n) = 
Space Complexity: S(n) = O(1)
'''

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp fibonacci sequence
        fibOne = 1 # starts at Fibonacci[1]
        fibTwo = 1 # starts at Fibonacci[2]
        for i in range(0, n - 1):
            temp = fibOne
            fibOne = fibOne + fibTwo
            fibTwo = temp
        return fibOne
            
# def DP_Fibonacci(n: int):
#     f = [0, 1]
#     for i in range(2, n + 1):
#         f.append(f[i-1] + f[i-2])
#     return f[n]

# @lc code=end

