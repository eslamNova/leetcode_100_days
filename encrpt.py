# O(N)

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        ans = ""
        l = len(s)

        for i, c in enumerate(s):
            ans += s[(i+k) % l]
        return ans
        