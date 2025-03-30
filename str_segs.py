class Solution:
    def countSegments(self, s: str) -> int:
        ss = s.split(" ")
        a = 0
        for n in ss:
            if n.strip() != "":
                a += 1
        return a
        