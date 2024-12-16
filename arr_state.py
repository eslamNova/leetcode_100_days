# O(K)
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for i in range(k):
            m = min(nums)
            j = nums.index(m)
            x = m * multiplier
            nums[j] = x 
        return nums