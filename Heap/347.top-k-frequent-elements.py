#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (66.36%)
# Likes:    19896
# Dislikes: 859
# Total Accepted:    3.9M
# Total Submissions: 5.8M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# 
# Output: [1,2]
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# 
# Output: [1]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# 
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# 
# 
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# 
#

# @lc code=start
from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent
        elements. You may return the answer in any order. Use a count dictionary
        to keep track of the frequency of each number. Use a min heap to find the
        k most frequent elements using (freq, num) tuples as the heap items.

        Args:
            nums (List[int]): array of integers
            k (int): the number of most frequent elements to find

        Returns:
            List[int]: the k most frequent elements in nums
        
        @complexity: Time: O(nlogk)
        @complexity: Space: O(k)
        """
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for freq, num in min_heap]

# @lc code=end

