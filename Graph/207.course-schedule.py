#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (51.35%)
# Likes:    18328
# Dislikes: 886
# Total Accepted:    2.8M
# Total Submissions: 5.4M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
# 
# 
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
# 
# 
# Return true if you can finish all courses. Otherwise, return false.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
# 
# 
#

# @lc code=start
from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        There are a total of `numCourses` courses you have to take, labeled from `0` to
        `numCourses - 1`. You are given an array `prerequisites` where 
        `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` 
        first if you want to take course `ai`.

        Algorithm:
            1. Create a graph representation of the courses and their prerequisites.
            2. Use Kahn's algorithm (BFS) to perform topological sorting.
            3. Maintain an in-degree array to track the number of prerequisites for each course.
            4. Initialize a queue with all courses that have no prerequisites (in-degree of 0).
            5. Process each course in the queue, reducing the in-degree of its dependent courses.
            6. If a dependent course's in-degree becomes zero, add it to the queue.
            7. Count the number of courses processed. If it equals `numCourses`, return True; 
                otherwise, return False.

        Args:
            numCourses (int): The total number of courses.
            prerequisites (List[List[int]]): A list of prerequisite pairs.
        
        Returns:
            bool: True if you can finish all courses, otherwise False.
        
        @complexity:
            Time Complexity: T(V, E) = O(V + E), where V is the number of courses (vertices) and E is the number of prerequisites (edges).
            Space Complexity: S(V, E) = O(V + E), for storing the graph and the visited set.
        """
        # Create a graph representation of the courses and their prerequisites
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Initialize a queue with all courses that have no prerequisites (in-degree of 0)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # Count the number of courses processed
        processed_courses = 0
        
        while queue:
            course = queue.popleft()
            processed_courses += 1
            
            # Reduce the in-degree of dependent courses
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                # If a dependent course's in-degree becomes zero, add it to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If the number of processed courses equals numCourses, return True; otherwise, return False
        return processed_courses == numCourses
        
# @lc code=end

