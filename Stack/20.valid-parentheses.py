#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.

        Args:
            s (str): string of parentheses

        Returns:
            bool: True if valid, False otherwise

        @complexity: Time: O(n)
        @complexity: Space: O(n)
        """
        pairs = {")": "(", "]": "[", "}": "{"} # map of closing to opening
        stack = [] # holds openers we've seen but not yet closed
        for char in s:
            if char in pairs:
                # stack empty or top of stack doesn't match
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)

        return not stack
# @lc code=end
