class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = sum(nums)
        return s % k
        # r = s % k
        # if r == 0:
        #     return 0
        # else:
        #     return r
        # for n in nums:
        #     r2 = n % k 
        #     if r2 == r:
        #         return r

        # if s > k:
        #     return s - k
        # return s