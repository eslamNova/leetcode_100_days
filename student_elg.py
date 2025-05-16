class Solution:
    def checkRecord(self, s: str) -> bool:

        c = Counter(s)

        if c['A'] < 2 and "LLL" not in s:
            return True
        return False
        