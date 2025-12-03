class Solution:
    def scoreBalance(self, s: str) -> bool:

        si = []
        for n in s:
            si.append(ord(n)-96)

        ss = sum(si)
        sso = 0
        for i in range(len(si)):
            sso += si[i]
            if sso == ss - sso:
                return True

        return False
        