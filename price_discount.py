# O(N2)
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        ans = [] 
        
        for i in range(len(prices)):
            dis = False
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    dis = True
                    ans.append(prices[i]-prices[j])
                    break
            if not dis:
                ans.append(prices[i])
        return ans
                