class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed = False
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                if removed:
                    return False
                removed = True
                # If removing nums[i] doesn't work, then nums[i+1] must be removed
                if i > 0 and nums[i - 1] >= nums[i + 1]:
                    nums[i + 1] = nums[i]  # force skip nums[i+1]
        return True
        