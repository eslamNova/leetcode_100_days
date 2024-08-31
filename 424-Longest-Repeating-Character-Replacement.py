class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = {}
        ans = 0 

        l = 0
        for r in range(len(s)):
            c[s[r]] = 1 + c.get(s[r], 0)

            while (r - l + 1) - max(c.values()) > k:
                c[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)

        return ans