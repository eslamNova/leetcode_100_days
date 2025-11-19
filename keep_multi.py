class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        o = original
        while 1:

            if o in nums:
                o = 2 * o
            else:
                break
        return o
        