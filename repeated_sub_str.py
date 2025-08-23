class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        # c = Counter(s)
        # if len(s) < 2 or len(s) % 2 != 0:
        #     return False

        # st = 0
        # for n in c:
        #     st += c[n]
        # print(st)
        # sl = st // len(c)
        # print(sl)
        # nm = len(c)
        # print(nm)
        # print(s[:sl] * nm)
        # return s == s[:sl] * nm
        n = len(s)
        # Try all possible substring lengths
        for l in range(1, n // 2 + 1):
            if n % l == 0:  # substring length must divide the string length
                if s == s[:l] * (n // l):
                    return True
        return False
        