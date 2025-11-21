class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:

        s = len(nums)

        for n in nums:
            if n == 1:
                if s < k:
                    return False
                s = 0
            else:
                s += 1
        return True
        