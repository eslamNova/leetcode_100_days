class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        m = 0
        for i in range(len(nums)):
            l = 0
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    l = (nums[i] - nums[j]) * nums[k]
                    if l > m:
                        m = l 

        return m

        