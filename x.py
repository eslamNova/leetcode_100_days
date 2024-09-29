class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        l = len(nums)

        for i in range(l):
            if l-i <= nums[i] and (i == 0 or l-i > nums[i - 1]):
                return l-i

        return -1