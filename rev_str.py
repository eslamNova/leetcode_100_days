#O(N)

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = 0 
        r = len(s) -1
        sl = list(s)

        while l < r:
            
            if sl[l].isalpha():
                if sl[r].isalpha():
                    sl[l], sl[r] = sl[r], sl[l]
                    l += 1
                    r -= 1
                else:
                    r -= 1
            else:
                l += 1
        return "".join(sl)