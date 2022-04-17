from math import floor
from typing import List
from math import floor

class Search:
    def binarySearch(A : List[int], l : int, r : int, x : int) -> int:
        '''
        Algorithm from intro to Algorithms 3rd Ed.
        
        Worst Case.
        Time Complexity: T(n) = O(log n)
        Space Complexity: S(n) = O(n)

        A : array of integers
        l : start of array A
        r : end of array A
        x : value to search in array A

        binary search assumes the array is sorted
        We can use mergesort or quicksort to do fast sorting of our array
        return location of x in array A
        '''
        # check the base case
        if r >= l:
            mid = l + (r - l) // 2 # // is the floor division

            # If the element is present at the middle itself
            if A[mid] == x:
                return mid
            
            # If the element is smaller than the mid, then
            # the target value x can only be present in the 
            # left side of the subarray
            elif A[mid] > x:
                return Search.binarySearch(A, l, mid - 1, x)
            
            # If the element is larger than the mid, thne
            # the target value x can only be present in the 
            # right side of the subarray
            else:
                return Search.binarySearch(A, mid + 1, r, x)
        
        else:
            # element is not present in the array
            return -1
