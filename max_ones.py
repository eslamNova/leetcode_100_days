class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        o = 0
        s = []
        for n in nums:
            if n == 1:
                o += 1

            else:
                s.append(o)
                o = 0
        s.append(o)
        return max(s)
