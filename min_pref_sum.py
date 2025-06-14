class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s = 0
        buff = 0
        for n in nums:
            s += n
            buff = min(buff, s)

        return 1 - buff