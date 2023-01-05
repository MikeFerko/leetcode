#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        n : input number of stairs we can climb
        one : the pointer variable to bottom up element in dp array starting at n - 1 finishing
        @ the solution number of possible distinct ways to climb to the top.
        two : the pointer variable to the previous element in dp array starting at n
        and finishing at the number of possible distinct ways to climb to the top from the first step 
        in the stair case.

        Algorithm: Use fibonacci sequence to calculate all distinct possible ways to climb to the
        top of our stair case from the bottom up dp approach and when the second element in the fib
        sequence reaches the 0th floor we return that variable.

        time T(n) = O(n) -> linear maxes out at taking 1 step at a time.
        space S(n) = O(1) -> we used three variables that consistently get reevaluated.

        S(n) = O(n) if we use a dp array and pointers to the fib numbers instead of just veriables
        '''
        
        one, two = 1, 1

        for _ in range(n - 1, 0, -1):
            temp = one
            one = one + two
            two = temp
        
        return one


# @lc code=end

