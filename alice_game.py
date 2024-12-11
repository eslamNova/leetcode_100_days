class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        al, bb = 0,0
        for d in nums:
            if d > 9:
                al += d
            else:
                bb += d
        if al == bb:
            return False
        return True
        