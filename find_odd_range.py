class Solution:
    def countOdds(self, low: int, high: int) -> int:

        a = high - low

        if low % 2 != 0 or high % 2 != 0:

            return a // 2 + 1
        return a // 2