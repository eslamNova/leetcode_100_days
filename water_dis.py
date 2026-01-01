class Solution:
    def fillCups(self, amount: List[int]) -> int:
        s = sum(amount)

        if 0 in amount or max(amount) > (s - max(amount)):
            return max(amount)
        x =  s % 2 
        r = s // 2 + x
        return r
        