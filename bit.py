# O(LOGN)

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        xor = start ^ goal

        c = 0 

        while xor:
            c += xor & 1
            xor >>= 1

        return c