# O(N∗Log(Max(Piles)))

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l,r = 1, max(piles)

        res = r

        while l <= r:
            k = (l+r) // 2

            hs = 0 

            for p in piles:
                hs += math.ceil(p/k)
            
            if hs <= h:
                res = min(res, k)
                r = k-1
            else:
                l = k+1

        return res 
        