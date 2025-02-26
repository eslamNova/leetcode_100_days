# O(N)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""

        if k == 1:
            return s
        if len(s) <= k:
            return s[::-1]
        r,l = 0,0

        for i in range(0,len(s), 2*k):

            r = i
            l = i + k 
            print(r,l)
            print(s)
            rv = s[r:l]
            ans += rv[::-1]
            print(ans)
            ans += s[l:i+2*k]
            print(ans)
        return ans
            