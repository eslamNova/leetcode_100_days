class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        d = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                if nums[j] - nums[i] > d and nums[j] - nums[i] != 0:
                    d = nums[j] - nums[i]
        
        return d

        