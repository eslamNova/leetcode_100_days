class Solution:
    def isFascinating(self, n: int) -> bool:

        a = 2 * n
        b = 3 * n

        d = str(a) + str(b) + str(n)
        if len(d) > 9:
            return False
        for i in range(1,10):
            if str(i) not in d:
                return False

        return True
        