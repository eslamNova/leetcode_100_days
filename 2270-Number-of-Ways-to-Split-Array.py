class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        l = 0 
        ans = 0
        s = sum(nums)

        for i in range(len(nums)-1):

            l += nums[i]
            r = s - l 
            if l >= r:
                ans += 1

        return ans
        