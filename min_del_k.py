class Solution:
    def minDeletion(self, s: str, k: int) -> int:

        c = Counter(s)

        # print(c)

        if len(c) <= k:
            return 0
        c = c.most_common()
        # print(c)
        d  = 0 

        t = len(c) - k
        j = len(c)-1

        while j >= len(c)-t:
            d += c[j][1]
            j -= 1
        return d
        