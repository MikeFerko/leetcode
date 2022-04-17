from typing import List
from math import floor, inf

class sorting:
    def mergeSort(A: List[int], p : int, r : int) -> List[int]:
        '''
        Algorithm from intro to Algorithms 3rd Ed.
        
        Worst Case.
        Time Complexity: T(n) = O(n log n)
        Space Complexity: S(n) = O(n)

        A : array of integers
        p : start of array A
        r : end of array A
        q : middle pivot dividing the arrays
        '''
        if len(A) == 1:
            return A
        if p < r:
            q = floor((p + r) // 2)
            sorting.mergeSort(A, p, q) # recurs on left side of array
            sorting.mergeSort(A, q + 1, r) # recurs on right side of array
            sorting.merge(A, p, q, r)
        
        return A

    def merge(A: List[int], p : int, q : int, r : int) -> List[int]:
        '''
        A : array of integers
        p : start of array A
        q : middle pivot dividing the arrays
        r : end of array A
        '''
        
        n1 = q - p + 1 # length of left half of array A
        n2 = r - q # length of right half of array A
        
        # create two empty arrays L[0...n1] : left and R[0...n2] : right
        L = [0] * (n1 + 1)
        R = [0] * (n2 + 1)

        # copy the left half of array A to L[0...n1-1]
        for i in range(0, n1):
            L[i] = A[p + i]
        
        # copy the right half of the array A to R[0...n2-1]
        for j in range(0, n2):
            R[j] = A[q + 1 + j]

        # create sentinel/flag values at the end of array L and array R
        L[n1] = inf
        R[n2] = inf

        # iterate over L and R
        # copying the smallest from L[i] and R[j] to array A[k]
        i = 0
        j = 0
        for k in range(p, r + 1):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
        
        return A




