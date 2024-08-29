# O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pr = [] 
        gm = prices[0]

        for s in prices:
            if s > gm:
                pr.append(s - gm)

            if s < gm:
                gm = s
        if pr:
            return max(pr)
        return 0
