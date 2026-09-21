#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#
# https://leetcode.com/problems/hand-of-straights/description/
#
# algorithms
# Medium (58.42%)
# Likes:    3834
# Dislikes: 301
# Total Accepted:    490.6K
# Total Submissions: 839.9K
# Testcase Example:  '[1,2,3,6,2,3,4,7,8]\n3'
#
# Alice has some number of cards and she wants to rearrange the cards into
# groups so that each group is of size groupSize, and consists of groupSize
# consecutive cards.
# 
# Given an integer array hand where hand[i] is the value written on the i^th
# card and an integer groupSize, return true if she can rearrange the cards, or
# false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
# 
# 
# Example 2:
# 
# 
# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.
# 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= hand.length <= 10^4
# 0 <= hand[i] <= 10^9
# 1 <= groupSize <= hand.length
# 
# 
# 
# Note: This question is the same as 1296:
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
# 
#

# @lc code=start
from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Alice has some number of cards and she wants to rearrange the cards 
        into groups so that each group is of size groupSize, and consists of 
        groupSize consecutive cards.

        Given an integer array hand where hand[i] is the value written on the
        i^th card and an integer groupSize, return true if she can rearrange
        the cards, or false otherwise.

        Algorithm:
            1. Return False if the hand cannot be evenly divided into groups.
            2. Count the frequency of each card and sort the unique cards.
            3. For each unique card, repeatedly form a group while its remaining
            frequency is greater than 0 by decrementing the counts of the next
            groupSize consecutive cards.
            4. Return False if a required consecutive card is unavailable;
            otherwise, return True after all cards are used.
        
        Args:
            hand (List[int]): The list of cards in Alice's hand.
            groupSize (int): The size of each group to be formed.
        
        Returns:
            bool: True if the cards can be rearranged into groups of size 
            groupSize with consecutive cards, False otherwise.
        
        @complexity:
            Time: T(n) = O(n log n) due to sorting the unique cards.
            Space: S(n) = O(n) for storing the frequency of each card.
        """
        # Check if the total number of cards is divisible by the groupSize w/o a remainder
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        unique_cards = sorted(count.keys()) # O(n log n) time complexity for sorting

        for card in unique_cards:
            while count[card] > 0:
                for i in range(groupSize):
                    next_card = card + i
                    if count[next_card] <= 0:
                        return False
                    count[next_card] -= 1
        return True
        
# @lc code=end

