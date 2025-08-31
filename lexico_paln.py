class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        for i in range(n//2):
            print(i)
            if s[i] == s[n-i-1]:
                pass
            else:
                if s[i] < s[n-i-1]:
                    sl = list(s)
                    sl[n-i-1] = s[i]
                    s = "".join(sl)
                    
                else:
                    sl = list(s)
                    sl[i] = s[n-i-1]
                    s = "".join(sl)

                    
        return s



        