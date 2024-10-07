# O(N^2)

class Solution:
    def minLength(self, s: str) -> int:
        while True:
            if s.find("AB") == -1:
                if s.find("CD") == -1:
                    break
                else:
                    s = s[:s.find("CD")] + s[s.find("CD")+2:]
            else:
                s = s[:s.find("AB")] + s[s.find("AB")+2:]
                
        return len(s)