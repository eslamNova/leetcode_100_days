# O(N*M)

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        c = 0 
        for n in words:
            if s.startswith(n):
                c += 1
        return c
        