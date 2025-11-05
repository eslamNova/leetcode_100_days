class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        a = 0
        for n in nums:
            if n % 2 == 0:
                a = a | n

        return a
        