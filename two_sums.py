# O(N2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        for i in range(len(nums)):
            t = target - nums[i]
            print(target,nums[i], t)
            if t in nums:
                if i != nums.index(t):
                    return [i, nums.index(t)]
                
                
# O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pmap = {}

        for i,n in enumerate(nums):

            d = target - n

            if d in pmap:
                return [pmap[d], i]
            pmap[n] = i
        return 
        
        