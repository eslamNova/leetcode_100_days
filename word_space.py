# O(N)
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        i = 0
        for n in spaces:
            ans+= s[i:n]
            i = n
            ans += " "
        ans += s[spaces[-1]:]
        return ans
        