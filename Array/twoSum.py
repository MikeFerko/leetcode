from typing import List

class BruteForceSolution:
    '''
    Time Complexity: T(n) = O(n^2)
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            '''
            check every combination of nums[i] and nums[j] that add up to target
            after the current index i. Checking everything after i will allow us to
            only check combinations that we have not conditionally checked before the
            current index i. So j needs to start at index i + 1 up to n - 1 indices.
            '''
            for j in range(i + 1, n):
                ''' 
                here is our conditonal check to see if the two indexed values add up to
                the two sum target value.
                '''
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i,j]
        
        return []

class HashMapSolution:
    '''
    Time Complexity: T(n) = O(n)
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        We can use the set data structure in python for a hash table
        '''
        hashMap = {} # value : index

        n = len(nums) # make sure we only calculate the length of the list n once
        for i in range(0, n):
            '''
            Q: What is happening here?
            A: Here we have initialized a hashmap as a set to store our value and index pairs.
                1. Upon the first iteration we will see a value from the 0th postion of the nums array.
                the difference value between the current value at index 0 and target will tell us nothing
                because no previous difference values are in the hashMap currently. At the end we store the
                current iteration value and index into our hashMap.

                2. Upon the second iteration we will see a similar process, but we have stored the previous
                iteration value into our hashMap so 
                    
                    a. If that value from our hash map is the difference between
                    the current value and the target - then we know the current value plus the prvious value add up
                    to the target value and we can return the current index and the hashMap index of the difference vlaue
                    which will give us the resulting indices of the input nums list that add up to the target value
                    
                    b. If that value does not add up to the difference stored in our hashMap we will also store that value
                    in our HashMap to keep track of that difference value and it's index in the nums array.
            '''
            value = nums[i]
            diffValue = target - value

            if diffValue in hashMap:
                # return a list/array of the prvious difference value index and the current index
                return [hashMap[diffValue], i] 

            hashMap[value] = i # store the current value and it's index in the hashMap


if __name__=="__main__":
    a = [7,2,6,3,8]
    target  = 8
    list_ = []
    list_ = BruteForceSolution.twoSum(list_, a, target)

    print(list_)
    print(a[list_[0]], "+", a[list_[1]], " = {}".format(target))

    list_ = []
    list_ = HashMapSolution.twoSum(list_, a, target)

    print(list_)
    print(a[list_[0]], "+", a[list_[1]], " = {}".format(target))
