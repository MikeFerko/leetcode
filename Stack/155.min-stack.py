#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

from typing import Union

# @lc code=start
class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    
    NOTE stacks are Last In First Out (LIFO)
    [], < -- top
    [],
    []  < -- bottom

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int value) pushes the element value onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time complexity for each function.

    @complexity: Time: O(1) for each operation
    @complexity: Space: O(n) where n is the number of elements
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        """
        :rtype: None
        """
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> Union[int, None]: #int:
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> Union[int, None]: #int:
        """
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]
        return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
