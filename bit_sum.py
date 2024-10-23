# O(LOG(N))

class Solution:
    def evenOddBit(self, n: int) -> List[int]:

        s = bin(n)
        o, e= 0,0 

        for k,i in enumerate(s[::-1]):
            if k % 2 == 0 and i == "1":
                e += 1
            elif i == "1":
                o += 1
        return [e,o]
        