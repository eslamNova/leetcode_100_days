class Solution:
    def makeFancyString(self, s: str) -> str:

        if len(s) < 3:
            return s
        ans = ""

        for i in range(0, len(s)-2, 1):
            if s[i] == s[i+1] == s[i+2]:
                if ans == "":
                    ans += s[:2]
            else:
                if ans == "":
                    ans += s[:2]
                ans += s[i+2]

            
        return ans
        