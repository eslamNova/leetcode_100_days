class Solution:
    def minOperations(self, nums: List[int]) -> int:
        r = 0 
        i = 1
        while i < len(nums):

            if nums[i] <= nums[i-1]:
                t = nums[i-1] - nums[i] + 1
                nums[i] += t
                r += t 
                i += 1
            else:
                i += 1

        return r




        