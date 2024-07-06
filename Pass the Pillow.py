# O(1)

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time < n:
            return time + 1
        else:
            if (time // (n-1)) % 2 == 0 :
                return (time % (n-1)) + 1
            return n - (time % (n-1)) 