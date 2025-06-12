class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        ss = set(nums)
        ssl =  list(ss)
        sslo = sorted(ssl)[::-1]
        print(sslo)
        if len(sslo) > 2:
            return sslo[2]
        return max(nums)