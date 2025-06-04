class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = 0
        mi = 0 

        for i in range(len(nums)):
            if nums[i] > m:
                m = nums[i]
                mi = i
        
        for n in nums:
            if n != m and m < 2*n:
                return -1
        return mi