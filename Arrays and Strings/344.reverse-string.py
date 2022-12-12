#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        '''
        s : input array of string characters
        n : length of input array s
        l : left pointer in array s
        r : right pointer in array s

        brute force: create a new array and populate the reversed string array while
        moving a pointer from right to left in the input array. Reassign the
        input array to the reversed string array.
        
        time T(n) = O(n) -> iterate through the entire array
        space S(n) = O(n) -> new array

        algorithmic: we can itterate through s with l from left to right and
        r from right to left and just swap the letters at the locations
        until the right pointer pass the left pointer at which point
        we will have swapped all the characters in place to reverse the string
        
        time T(n) = O(n/2) = O(n) -> iterate through the half the array, but in terms of asyptotes it simplifies to the whole array
        space S(n) = O(1) -> modifying the original array means no extra space usage.
        
        We will use the algorithmic approach
        loop termination condition: r >= l
        '''
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            vall = s[l]
            valr = s[r]
            s[r] = vall
            s[l] = valr
            l += 1
            r -= 1
        # at this point we would return the reversed string array
        
# @lc code=end

