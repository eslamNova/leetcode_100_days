class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        l = s.split(\ \)
        if len(set(pattern)) != len(set(l)) or len(pattern) != len(l):
            return False
        d = {}
        i = 0
        for n in pattern:
            if n in d:
                if d[n] != l[i]:
                    return False
            else:
                d[n] = l[i]
            i += 1
        return True

        