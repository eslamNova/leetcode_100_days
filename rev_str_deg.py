class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            reverse = 26-(ord(s[i])-ord("a"))
            total+=reverse*(i+1)
        return total
        