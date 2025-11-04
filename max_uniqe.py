class Solution:
    def maxSum(self, nums: List[int]) -> int:

        if sum(nums) < 0 and max(nums) < 0:
            return max(nums)

        s = set(nums)
        s = sorted(s)

        a = 0 
        for n in s:
            if n > 0:
                a += n

        return a
        