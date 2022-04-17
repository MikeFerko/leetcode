from typing import List

class sorting:
    def quickSort(A : List[int], p : int, r : int) -> List[int]:
        '''
        Algorithm from intro to Algorithms 3rd Ed.

        Worst Case.
        Time Complexity: T(n) = O(n^2)
        Space Complexity: S(n) = O(log n)

        A : array of integers
        p : start of array A
        r : end of array A
        '''
        if len(A) == 1:
            return A
        if p < r:
            q = sorting.partition(A,p,r) # partition index
            # Arr[q] is not in the correct place.

            # separately we sort the elements before and after
            # the partition
            sorting.quickSort(A,p,q-1)
            sorting.quickSort(A,q+1,r)
        
        return A
    
    def partition(A : List[int], p : int, r : int) -> int:
        x = A[r] # pivot element
        i = p - 1 # index of the smaller element
        for j in range(p, r):
            # if the current element is less than or equal to
            # the pivot then exchange the elements
            if A[j] <= x:
                # increase the index of the smaller element
                i += 1
                # exchange A[i] with A[j] 
                A[i], A[j] = A[j], A[i]

        #  exchange A[i + 1] with A[r]
        A[i + 1], A[r] = A[r], A[i + 1]

        return i + 1

