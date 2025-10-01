class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        used = 0

        while numBottles >= numExchange:
            
            k = numBottles // numExchange

            used += numExchange * k
            numBottles -= numExchange * k
            

            numBottles += k
        return used + numBottles
            

        return ans
        