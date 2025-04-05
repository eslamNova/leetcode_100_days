class Solution:
    def replaceDigits(self, s: str) -> str:

        ans = s[0]
        alpha = "abcdefghijklmnopqrstuvwxyz"

        for i in range(1,len(s)):

            if s[i].isdigit():
                a = s[i-1]
                b = int(s[i])
                n = ord(s[i-1])-ord("a")
                print(n)
                ans += alpha[n+b]
            else:
                ans += s[i]
        return ans