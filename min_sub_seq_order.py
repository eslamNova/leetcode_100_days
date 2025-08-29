class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        
        if len(nums)< 2:
            return nums
        a = sorted(nums)[::-1]
        s = sum(nums)

        print(a)
        for i in range(len(a)):
            sm = sum(a[:i])
            re = s - sm
            if sm > re:
                return a[:i]
        return nums