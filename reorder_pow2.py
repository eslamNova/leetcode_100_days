class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = str(n)
        c = Counter(s)
        print(s)

        for i in range(31):
            k = str(2 ** i)

            if len(k) != len(s):
                continue

            if Counter(k) == c:
                return True
        return False