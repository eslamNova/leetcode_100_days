# O(N)
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd = False
        c = 0

        for n in arr:
            if n % 2 != 0:
                odd = True 
            else:
                odd = False
                c = 0

            if odd:
                c += 1

            if c >= 3:
                return True
        return False