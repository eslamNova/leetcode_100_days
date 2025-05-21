class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s = sum(nums)
        sn = "".join([str(x) for x in nums])
        a = 0
        for n in sn:
            a += int(n)
        return abs(s - a)