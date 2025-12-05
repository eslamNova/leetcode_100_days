class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        o = 0 
        
        for i in range(1,len(nums)):
            # print(sum(nums[:i]), sum(nums[i:]))
            if abs(sum(nums[:i]) - sum(nums[i:])) % 2 == 0:
                o += 1
        return o 
        