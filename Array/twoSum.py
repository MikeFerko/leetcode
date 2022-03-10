from typing import List

class BruteForceSolution:
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


if __name__=="__main__":
    a = [7,2,6,3,8]
    target  = 8
    list_ = []
    list_ = BruteForceSolution.twoSum(list_, a, target)

    print(list_)
    print(a[list_[0]], "+", a[list_[1]], " = {}".format(target))
