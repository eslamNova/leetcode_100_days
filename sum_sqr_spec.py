class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        a = 0 
        for i in range(1,len(nums)+1):
            if len(nums) % i == 0:
                a += nums[i-1] ** 2
        return a
        