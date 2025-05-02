class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # c = Counter(deck)
        # a = set()
        # m = 10000
        # for n in c:
        #     if c[n] < m:
        #         m = c[n]
        #         print("m", m)
        #     if c[n] > m:
        #         a.add(c[n]% m)
        #     else:
        #         a.add(c[n])
        #     print(a)

        # return len(a) == 1 and len(deck) > 1
        count = Counter(deck).values()
        g = reduce(gcd, count)
        return g > 1